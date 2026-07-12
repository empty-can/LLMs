#!/usr/bin/env python3
"""llms-full.txt から「カテゴリ適性」スコア付き用語ランキングを生成するプロトタイプ。

目的: 公式ドキュメント全体を横断する概念語（例: environment variable, command, hook）を
統計的に抽出し、変更点一覧のグルーピングに使う「カテゴリ候補」を機械的に得られるか検証する。

手法（外部パッケージ不使用・純 Python）:
  1. 候補抽出   : RAKE 流（ストップワード・句読点で分割した 1〜4 語の句を候補とする）
                  + 見出し・インラインコード由来の候補をマーク
  2. termhood   : C-value（長い句に包含される出現を割り引き、句としての独立性を測る）
  3. 横断性     : ページ被覆率のバンドパス（少数ページ特化でも全ページ遍在でもない中間帯を高評価）
                  + Gries の DP による出現分散の均一度
  4. 中心性     : ページ共起グラフ上の NPMI 重み付き次数中心性（多くの語と共起するハブ概念を高評価）
  5. 総合スコア : 上記の幾何平均 + ページ名/見出し出現の規定加算ボーナス
                  （ページ名・ページ内見出しはカテゴリの最有力候補という前提を直接反映する。
                   加算式なので、統計軸の弱い語でもページ名に立っていれば候補として浮上できる）

出力: Markdown のランキング表 + ページ被覆ベクトルの類似度によるカテゴリ素案クラスタ。
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# --- 1. パース -----------------------------------------------------------------

SOURCE_RE = re.compile(r"^Source:\s+(https?://\S+)")
HEADING_RE = re.compile(r"^(#{2,4})\s+(.*)")
CODE_SPAN_RE = re.compile(r"`([^`]+)`")
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
URL_RE = re.compile(r"https?://\S+")
TAG_RE = re.compile(r"</?[A-Za-z][^>]*>")


def parse_pages(text: str, exclude_prefixes: tuple[str, ...] = ("whats-new",)) -> list[dict]:
    """`# Title` 直後に `Source:` を伴うブロックを 1 ページとして分割する。

    exclude_prefixes: カテゴリ語彙の抽出元として不適切なページ（changelog 転載の
    whats-new/ 等。"Fixed"のような更新動詞が語彙統計を汚染する）を slug prefix で除外。
    """
    lines = text.splitlines()
    pages = []
    cur = None
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue  # フェンス内コードはノイズ源なので語彙集計から除外
        if line.startswith("# ") and i + 1 < len(lines):
            m = SOURCE_RE.match(lines[i + 1])
            if m:
                slug = m.group(1).split("/docs/en/")[-1]
                cur = {
                    "title": line[2:].strip(),
                    "slug": slug,
                    "body": [],
                    "headings": [],
                    "codespans": [],
                    "sections": [[]],  # h2 区切りの本文（セクション共起用）
                    "skip": any(slug.startswith(p) for p in exclude_prefixes),
                }
                if not cur["skip"]:
                    pages.append(cur)
                continue
        if cur is None or cur["skip"] or SOURCE_RE.match(line):
            continue
        hm = HEADING_RE.match(line)
        if hm:
            cur["headings"].append(hm.group(2))
            if hm.group(1) == "##":
                cur["sections"].append([])
        cur["codespans"].extend(CODE_SPAN_RE.findall(line))
        # リンクはアンカーテキストのみ残し、URL・HTML タグ・表罫線を落とす
        clean = LINK_RE.sub(r"\1", line)
        clean = URL_RE.sub(" ", clean)
        clean = TAG_RE.sub(" ", clean)
        clean = clean.replace("|", " . ").replace(":---", " ")
        cur["body"].append(clean)
        cur["sections"][-1].append(clean)
    return pages


# --- 2. 候補抽出（RAKE 流） -----------------------------------------------------

STOPWORDS = set(
    """
a an the and or but if then else when while for to of in on at by with from as is are was
were be been being am do does did done doing have has had having will would can could should
shall may might must not no nor so such that this these those there here it its it's you your
yours we our ours they their them he she his her i me my mine us who whom which what where why
how all any both each few more most other some own same than too very just also only over under
again further once because until about against between into through during before after above
below up down out off than via per each's let lets etc eg ie e.g i.e vs
new use uses used using make makes made making get gets got getting set sets setting run runs ran
running see sees saw seen add adds added adding need needs needed want wants show shows shown
work works worked working start starts started starting create creates created creating
enable enables enabled enabling disable disables disabled include includes included including
follow follows following provide provides provided change changes changed keep keeps
require requires required requiring ask asks asked asking return returns returned returning
allow allows allowed allowing configure configures configured configuring
specific additional multiple failed
one two first second next last every without within
example examples note tip warning available default defaults common instead now
claude code's anthropic
""".split()
)

# 単独では一般的すぎてカテゴリにならない語（n-gram の内部要素としては許可）
GENERIC_SINGLE = set(
    """
page pages doc docs documentation file files way ways time times user users case cases
option options step steps guide overview reference type types name names value values
list lists item items line lines detail details support version versions
""".split()
)

# --- 動詞・動名詞の除外（v3・作業指示者提案1） --------------------------------------
# 品詞タガーが無いため「この docs で動詞としてしか実質使われない語」を厳選し、
# 活用形（三単現/過去/進行形）を機械生成してストップワード扱いにする。
# 注意: plan(plan mode)/review(code review)/resume(session resume)/edit(Edit tool)/
# checkpoint/search/monitor/log/build 等、動詞同形だが本 docs では機能名詞である語は
# 意図的に含めない。'set' は doubling で setting(s) を殺すため含めない（素の set は
# STOPWORDS 側で処理済み）。
VERB_BASES = """
connect manage install uninstall remove delete ensure verify specify define apply
select choose click send receive pass fail skip cancel retry wait learn understand
avoid prevent happen appear become contain expect accept reject approve deny grant
open close load save fetch pull push merge finish complete begin continue try
update upgrade launch execute invoke call trigger emit publish subscribe
describe explain refer mention consider recommend suggest prefer
""".split()


def _inflections(base: str) -> set[str]:
    forms = {base, base + "s", base + "es", base + "d", base + "ed", base + "ing"}
    if base.endswith("e"):
        forms.add(base[:-1] + "ing")  # use → using
    if len(base) >= 3 and base[-1] not in "aeiouy" and base[-2] in "aeiou" and base[-3] not in "aeiou":
        forms |= {base + base[-1] + "ed", base + base[-1] + "ing"}  # skip → skipped/skipping
    if base.endswith("y") and base[-2] not in "aeiou":
        forms |= {base[:-1] + "ies", base[:-1] + "ied"}  # try → tries/tried
    return forms


for _b in VERB_BASES:
    STOPWORDS |= _inflections(_b)

# --- 一般名詞・非カテゴリ語の降格（v3・作業指示者提案3） ------------------------------
# 単体では一般名詞、または本 docs でカテゴリ的意味を持たない語。除外ではなく
# スコアを規定率で降格し、レビュー時に目視できる位置に残す（unigram のみ適用。
# "agent team" 等の複合語には適用しない）。
DEMOTE_GENERIC = set("setup team feature json server app ai bash md".split())
DEMOTE_MULT = 0.4
# コードスパン由来ページの比率が高い語は構文トークン（json/bash 等）の可能性が高い。
# ページ名に立っていない場合のみ降格する。閾値 0.7: 設定キーとして code span に
# 頻出するだけの実カテゴリ語（sandbox 等）を誤爆しない程度に高く取る。
CODE_RATIO_TH = 0.7
CODE_DEMOTE_MULT = 0.6

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_.\-]*")


def normalize(tok: str) -> str:
    return tok.lower().strip(".-_")


def phrases_from_text(text: str) -> list[tuple[str, ...]]:
    """ストップワード・句読点区切りで候補句（1〜4 語）を切り出す。"""
    out = []
    for chunk in re.split(r"[.,;:!?()\[\]{}\"“”‘’•=+*/\\<>&%$#@~^]|\s[-—–]\s|\n", text):
        toks = [normalize(t) for t in TOKEN_RE.findall(chunk)]
        run: list[str] = []
        for t in toks:
            if t in STOPWORDS or len(t) <= 1:
                if run:
                    out.extend(_subphrases(run))
                run = []
            else:
                run.append(t)
        if run:
            out.extend(_subphrases(run))
    return out


def _subphrases(run: list[str]) -> list[tuple[str, ...]]:
    """連続コンテンツ語の run から 1〜4 語の部分句を列挙する。"""
    res = []
    n = len(run)
    for size in range(1, min(4, n) + 1):
        for s in range(n - size + 1):
            res.append(tuple(run[s : s + size]))
    return res


def capitalization_counts(text: str, cap: Counter, tot: Counter) -> None:
    """文頭（チャンク先頭）以外での大文字始まり率を語単位で集計する（固有名詞推定用）。"""
    for chunk in re.split(r"[.,;:!?()\[\]{}\"“”‘’•=+*/\\<>&%$#@~^]|\s[-—–]\s|\n", text):
        toks = TOKEN_RE.findall(chunk)
        for i, t in enumerate(toks):
            n = normalize(t)
            if not n or n in STOPWORDS:
                continue
            if i == 0:
                continue  # チャンク先頭は文頭の可能性があるため判定から除外
            tot[n] += 1
            if t[0].isupper():
                cap[n] += 1


def build_counts(pages):
    """ページ毎の候補句カウントと、ページ名/見出し/コード由来フラグを集計する。"""
    page_tf: list[Counter] = []
    heading_pages: dict[tuple, set] = defaultdict(set)
    title_pages: dict[tuple, set] = defaultdict(set)
    code_pages: dict[tuple, set] = defaultdict(set)
    cap_cnt: Counter = Counter()
    cap_tot: Counter = Counter()
    for idx, p in enumerate(pages):
        tf = Counter()
        body = "\n".join(p["body"])
        capitalization_counts(body, cap_cnt, cap_tot)
        for ph in phrases_from_text(body):
            tf[ph] += 1
        for h in p["headings"]:
            for ph in phrases_from_text(h):
                tf[ph] += 1
                heading_pages[ph].add(idx)
        # ページ名シグナル: h1 タイトルと slug のトークン（slug は - / 区切りを語に展開）
        slug_text = re.sub(r"[-/]", " ", p["slug"])
        for src in (p["title"], slug_text):
            for ph in phrases_from_text(src):
                tf[ph] += 1
                title_pages[ph].add(idx)
        for c in p["codespans"]:
            for ph in phrases_from_text(c):
                code_pages[ph].add(idx)
        page_tf.append(tf)
    return page_tf, heading_pages, title_pages, code_pages, cap_cnt, cap_tot


def merge_plurals(page_tf, heading_pages, title_pages, code_pages, cap_cnt, cap_tot):
    """`commands`→`command` 等、単数形が十分な頻度で存在する場合のみ複数形を併合する。

    頻度ガード: 単数形が希少なのに複数形が高頻度の語（AWS→aw 等の頭字語）は
    偶然の同形であり併合しない。
    """
    vocab: Counter = Counter()
    for tf in page_tf:
        for ph, c in tf.items():
            vocab[ph] += c

    def singular(ph):
        last = ph[-1]
        if last.endswith("s") and not last.endswith(("ss", "us", "is")):
            cand = ph[:-1] + (last[:-1],)
            if cand in vocab and vocab[cand] >= max(3, vocab[ph] * 0.05):
                return cand
        return ph

    mapping = {ph: singular(ph) for ph in vocab}
    new_tfs = []
    for tf in page_tf:
        nt = Counter()
        for ph, c in tf.items():
            nt[mapping[ph]] += c
        new_tfs.append(nt)
    for d in (heading_pages, title_pages, code_pages):
        for ph in list(d):
            m = mapping.get(ph, ph)
            if m != ph:
                d[m] |= d.pop(ph)
    # 大文字率カウンタ（unigram）にも複数形併合を適用
    for c in (cap_cnt, cap_tot):
        for w in list(c):
            m = mapping.get((w,), (w,))
            if m != (w,):
                c[m[0]] += c.pop(w)
    return new_tfs, heading_pages, title_pages, code_pages, cap_cnt, cap_tot


# --- 3. スコアリング -------------------------------------------------------------


def cvalue(term, tf_total, nested_freq):
    """C-value: 長い句に包含される出現を割り引いた termhood。"""
    length_w = math.log2(1 + len(term))
    nf, cnt = nested_freq.get(term, (0, 0))
    adj = tf_total[term] - (nf / cnt if cnt else 0)
    return length_w * max(adj, 0.1)


def coverage_band(df_frac, peak=0.30, sigma=0.75):
    """被覆率のバンドパス。peak 付近（既定 30%）を 1.0 として対数正規で減衰。"""
    if df_frac <= 0:
        return 0.0
    return math.exp(-((math.log(df_frac) - math.log(peak)) ** 2) / (2 * sigma**2))


def gries_dp_evenness(term, page_tf, page_sizes, total_size):
    """1 - Gries' DP。出現がページサイズ比通りに均等なら 1、偏在なら 0 に近づく。"""
    total = sum(tf[term] for tf in page_tf)
    if total == 0:
        return 0.0
    dp = 0.5 * sum(
        abs((tf[term] / total) - (page_sizes[i] / total_size))
        for i, tf in enumerate(page_tf)
    )
    return 1 - dp


def npmi_degree(top_terms, term_pages, n_pages):
    """ページ共起の NPMI>0.1 の相手数を数える簡易ハブ度（0〜1 正規化）。"""
    deg = Counter()
    terms = list(top_terms)
    for i, a in enumerate(terms):
        pa = term_pages[a]
        for b in terms[i + 1 :]:
            pb = term_pages[b]
            inter = len(pa & pb)
            if inter < 2:
                continue
            p_ab = inter / n_pages
            pmi = math.log(p_ab / ((len(pa) / n_pages) * (len(pb) / n_pages)))
            npmi = pmi / -math.log(p_ab)
            if npmi > 0.1:
                deg[a] += 1
                deg[b] += 1
    mx = max(deg.values(), default=1)
    return {t: deg.get(t, 0) / mx for t in terms}


# ページ名/見出し由来の規定加算ボーナス（最大値）。
# ページ名はカテゴリの最有力候補なので最も重く、複数ページのページ名に出る語ほど加算を増す。
TITLE_BONUS_MAX = 0.25    # ページ名（h1/slug）: 3 ページ分で満額
HEADING_BONUS_MAX = 0.12  # ページ内見出し（h2〜h4）: 10 ページ分で満額
PROPN_BONUS_MAX = 0.10    # 文頭以外の大文字始まり率 100% で満額（固有名詞推定・v3 提案4）


def score_terms(pages, min_tf=8, min_df=4):
    page_tf, heading_pages, title_pages, code_pages, cap_cnt, cap_tot = merge_plurals(
        *build_counts(pages)
    )
    n_pages = len(page_tf)
    page_sizes = [sum(tf.values()) for tf in page_tf]
    total_size = sum(page_sizes)

    tf_total = Counter()
    term_pages: dict[tuple, set] = defaultdict(set)
    for i, tf in enumerate(page_tf):
        for ph, c in tf.items():
            tf_total[ph] += c
            term_pages[ph].add(i)

    # 候補の足切り: 頻度・ページ数・一般語
    cands = [
        ph
        for ph, c in tf_total.items()
        if c >= min_tf
        and len(term_pages[ph]) >= min_df
        and not (len(ph) == 1 and ph[0] in GENERIC_SINGLE)
    ]

    # C-value 用: 各候補を包含するより長い候補の頻度合計
    nested_freq: dict[tuple, tuple[int, int]] = {}
    cand_set = set(cands)
    for ph in cands:
        if len(ph) == 4:
            continue
        nf = cnt = 0
        for other in cand_set:
            if len(other) > len(ph) and any(
                other[s : s + len(ph)] == ph for s in range(len(other) - len(ph) + 1)
            ):
                nf += tf_total[other]
                cnt += 1
        if cnt:
            nested_freq[ph] = (nf, cnt)

    # 中心性は上位候補のみで計算（O(n^2) のため）
    top_by_tf = sorted(cands, key=lambda p: -tf_total[p])[:600]
    centrality = npmi_degree(top_by_tf, term_pages, n_pages)

    max_cv = max(cvalue(p, tf_total, nested_freq) for p in cands)
    rows = []
    for ph in cands:
        df = len(term_pages[ph])
        cv = cvalue(ph, tf_total, nested_freq) / max_cv
        band = coverage_band(df / n_pages)
        even = gries_dp_evenness(ph, page_tf, page_sizes, total_size)
        cent = centrality.get(ph, 0.0)
        h_pages = len(heading_pages.get(ph, ()))
        t_pages = len(title_pages.get(ph, ()))
        # 幾何平均: どれか 1 軸が壊滅的な語（特化語・遍在語・非用語）を落とす
        core = (max(cv, 1e-6) * max(band, 1e-6) * max(even, 1e-6) * max(cent, 1e-6)) ** 0.25
        # ページ名/見出し由来の規定加算。乗算でなく加算にすることで、
        # 統計軸が弱い語（被覆率の低いページ名語など）も候補として浮上させる
        title_bonus = TITLE_BONUS_MAX * min(t_pages, 3) / 3
        heading_bonus = HEADING_BONUS_MAX * min(h_pages, 10) / 10
        # 固有名詞推定: 文頭以外での大文字始まり率（句は構成語の平均）に応じて加算
        ratios = [
            cap_cnt.get(w, 0) / cap_tot[w] for w in ph if cap_tot.get(w, 0) >= 5
        ]
        cap_ratio = sum(ratios) / len(ratios) if ratios else 0.0
        propn_bonus = PROPN_BONUS_MAX * cap_ratio
        # 一般名詞・構文トークンの降格（unigram のみ）
        mult = 1.0
        if len(ph) == 1:
            if ph[0] in DEMOTE_GENERIC:
                mult *= DEMOTE_MULT
            code_ratio = len(code_pages.get(ph, ())) / df
            if code_ratio >= CODE_RATIO_TH and t_pages <= 1:
                mult *= CODE_DEMOTE_MULT
        rows.append(
            {
                "term": " ".join(ph),
                "len": len(ph),
                "tf": tf_total[ph],
                "df": df,
                "cv": cv,
                "band": band,
                "even": even,
                "cent": cent,
                "h_pages": h_pages,
                "t_pages": t_pages,
                "cap": cap_ratio,
                "mult": mult,
                "score": (core + title_bonus + heading_bonus + propn_bonus) * mult,
                "pages": term_pages[ph],
            }
        )
    rows.sort(key=lambda r: -r["score"])
    return rows, n_pages


# --- 3.5 包含・同義語の併合（v3・作業指示者提案2） ----------------------------------

COMPOUND_PREFIXES = ("sub", "super", "pre", "post", "multi", "non")


def merge_containment(rows, top_k=300):
    """包含関係にある語を代表語へ併合し、スコアを合計する。

    規則:
      (a) トークン部分列: 「mcp server」「managed settings」は「mcp」「settings」の特化形
          → より短い側（複数候補時は高スコア側）へ併合
      (b) 既知接頭辞の複合語: 「subagent」は「agent」の特化形 → 基底語へ併合
    併合された語は代表語の「周辺語彙」として保持する（taxonomy 確定時の同義語表の種）。
    """
    top = rows[:top_k]
    by_term = {r["term"]: r for r in top}

    def find_parent(r):
        toks = r["term"].split()
        best = None
        for cand in top:
            if cand is r:
                continue
            ct = cand["term"].split()
            if len(ct) >= len(toks):
                continue
            if any(toks[i : i + len(ct)] == ct for i in range(len(toks) - len(ct) + 1)):
                if best is None or cand["score"] > best["score"]:
                    best = cand
        if best is None and len(toks) == 1:
            for p in COMPOUND_PREFIXES:
                base = toks[0][len(p):]
                if toks[0].startswith(p) and len(base) >= 3 and base in by_term:
                    return by_term[base]
        return best

    # 長い句から順に親へ畳み込む（親自身がさらに親を持つ場合は連鎖の根に集約）
    parent_of: dict[str, str] = {}
    for r in sorted(top, key=lambda x: -len(x["term"].split())):
        p = find_parent(r)
        if p is not None:
            parent_of[r["term"]] = p["term"]

    def root(t):
        seen = set()
        while t in parent_of and t not in seen:
            seen.add(t)
            t = parent_of[t]
        return t

    groups: dict[str, dict] = {}
    for r in top:
        rep = root(r["term"])
        g = groups.setdefault(rep, {"rep": rep, "score": 0.0, "members": []})
        g["score"] += r["score"]
        if r["term"] != rep:
            g["members"].append(r["term"])
    merged = sorted(groups.values(), key=lambda g: -g["score"])
    for g in merged:
        g["rep_row"] = by_term[g["rep"]]
    return merged


# --- 4. カテゴリ素案クラスタリング -------------------------------------------------


def section_cooccurrence(pages, term_strs):
    """h2 セクションを窓としたセクション単位の共起 NPMI を計算する。

    ページ単位だと横断語同士はほぼ全て共起して弁別できないため、
    より狭い窓（セクション）で「同じ話題の中で一緒に語られるか」を測る。
    """
    term_set = {tuple(t.split()) for t in term_strs}
    sec_presence: dict[tuple, set[int]] = defaultdict(set)
    sec_id = 0
    for p in pages:
        for sec in p["sections"]:
            body = "\n".join(sec)
            if len(body) < 80:  # 極小セクションはスキップ
                continue
            present = {ph for ph in phrases_from_text(body) if ph in term_set}
            for ph in present:
                sec_presence[ph].add(sec_id)
            sec_id += 1
    n_sec = max(sec_id, 1)

    def npmi(a: str, b: str) -> float:
        pa = sec_presence.get(tuple(a.split()), set())
        pb = sec_presence.get(tuple(b.split()), set())
        inter = len(pa & pb)
        if inter < 3 or not pa or not pb:
            return 0.0
        p_ab = inter / n_sec
        pmi = math.log(p_ab / ((len(pa) / n_sec) * (len(pb) / n_sec)))
        return pmi / -math.log(p_ab)

    return npmi


def cluster_terms(rows, pages, top_n=60, sim_th=0.25):
    """セクション共起 NPMI の平均リンク法（貪欲）で上位語をクラスタリングする。"""
    top = rows[:top_n]
    npmi = section_cooccurrence(pages, [r["term"] for r in top])
    clusters: list[dict] = []
    for r in top:
        best, best_sim = None, 0.0
        for cl in clusters:
            sims = [npmi(r["term"], t) for t in cl["terms"]]
            avg = sum(sims) / len(sims)
            if avg > best_sim:
                best, best_sim = cl, avg
        if best is not None and best_sim >= sim_th:
            best["terms"].append(r["term"])
        else:
            clusters.append({"terms": [r["term"]]})
    return clusters


# --- 5. 出力 ---------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="official-llms-txts/code.claude.com/docs/llms-full.txt")
    ap.add_argument("--out", default="work/categorize-algorithm/output/term-scores.md")
    ap.add_argument("--top", type=int, default=100)
    ap.add_argument("--probe", nargs="*", default=[], help="順位を確認したい語")
    args = ap.parse_args()

    text = Path(args.input).read_text(encoding="utf-8", errors="replace")
    pages = parse_pages(text)
    rows, n_pages = score_terms(pages)

    lines = [
        "# カテゴリ適性スコアリング結果（プロトタイプ）",
        "",
        f"入力: `{args.input}`（{n_pages} ページ） / 候補語数: {len(rows)}",
        "",
        "スコア = ( 幾何平均(C-value, 被覆バンド, 分散均一度, 共起中心性)"
        f" + ページ名加算(最大{TITLE_BONUS_MAX}) + 見出し加算(最大{HEADING_BONUS_MAX})"
        f" + 固有名詞加算(最大{PROPN_BONUS_MAX}) ) × 降格率",
        "",
        f"## 上位 {args.top} 語",
        "",
        "| # | term | TF | DF | C-val | band | even | cent | ページ名p | 見出しp | 大文字率 | 降格 | score |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(rows[: args.top], 1):
        lines.append(
            f"| {i} | {r['term']} | {r['tf']} | {r['df']} | {r['cv']:.2f} | {r['band']:.2f}"
            f" | {r['even']:.2f} | {r['cent']:.2f} | {r['t_pages']} | {r['h_pages']}"
            f" | {r['cap']:.2f} | {r['mult']:.2f} | {r['score']:.3f} |"
        )

    merged = merge_containment(rows)
    lines += [
        "",
        "## 包含併合後のカテゴリ候補（上位 40 グループ）",
        "",
        "併合規則: トークン部分列（mcp ⊂ mcp server）と既知接頭辞複合語（sub+agent）。スコアはグループ合計。",
        "",
        "| # | 代表語 | Σscore | 併合された語 |",
        "|---:|---|---:|---|",
    ]
    for i, g in enumerate(merged[:40], 1):
        mem = ", ".join(g["members"][:8]) or "—"
        if len(g["members"]) > 8:
            mem += f" ほか{len(g['members']) - 8}語"
        lines.append(f"| {i} | {g['rep']} | {g['score']:.3f} | {mem} |")

    if args.probe:
        lines += ["", "## 指定語の順位確認", ""]
        index = {r["term"]: (i, r) for i, r in enumerate(rows, 1)}
        for q in args.probe:
            hit = index.get(q.lower())
            if hit:
                i, r = hit
                lines.append(f"- `{q}`: **{i} 位** (TF={r['tf']}, DF={r['df']}, score={r['score']:.3f})")
            else:
                lines.append(f"- `{q}`: 候補に無し（頻度/ページ数の足切り未満か、抽出されず）")

    clusters = cluster_terms(rows, pages)
    lines += ["", "## カテゴリ素案クラスタ（上位60語・ページ共起ベース）", ""]
    for i, cl in enumerate(clusters, 1):
        lines.append(f"{i}. **{cl['terms'][0]}** — {', '.join(cl['terms'][1:]) or '(単独)'}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"written: {out} (candidates={len(rows)}, pages={n_pages})")


if __name__ == "__main__":
    sys.exit(main())
