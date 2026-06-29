

# Record lifecycle
<a name="registry-record-lifecycle"></a>

## Status transitions
<a name="registry-status-transitions"></a>

```
Create → DRAFT → Submit → PENDING_APPROVAL → Approve → APPROVED
                               │                          │
                               │ Reject                   │ Edit (new DRAFT
                               ▼                          │  revision; approved
                          REJECTED ── Approve (direct) ───┘  stays in search)
                               │
                               └── Edit → DRAFT

         Any status → DEPRECATED (terminal)
```

## Transition details
<a name="registry-transition-details"></a>
+  **Create** → DRAFT. Edit freely before submitting.
+  **Submit** → PENDING\_APPROVAL. Auto-approval skips to APPROVED. Amazon EventBridge notification sent.
+  **Approve/Reject** → Curator uses UpdateRegistryRecordStatus. Can directly approve a REJECTED record.
+  **Deprecate** → Terminal from any status. Cannot be undone.

## How edits affect status
<a name="registry-edits-affect-status"></a>


| Current status | Effect of edit | 
| --- | --- | 
| DRAFT | Updated in place. Stays DRAFT. | 
| PENDING\_APPROVAL | New DRAFT revision. Pending revision discarded. Not visible in search (never approved). | 
| APPROVED | New DRAFT revision. Approved revision stays visible in search until new revision is approved. | 
| REJECTED | New DRAFT revision. Must go through normal submit-and-approve flow again. | 
| DEPRECATED | Deprecated Records cannot be edited; Deprecated is a Terminal state | 

## Dual-revision behavior
<a name="registry-dual-revision"></a>

Editing an APPROVED record creates a new DRAFT revision while the approved revision remains active:
+  **Search and MCP endpoint** — Returns the approved revision.
+  **Get and List APIs** — Returns the latest (DRAFT) revision.

Once the edited revision of the record is reviewed and approved, then Search and MCP Endpoint also start showing the new (approved) revision.

## Visibility rules
<a name="registry-visibility-rules"></a>


| API | Returns | 
| --- | --- | 
| SearchRegistryRecords | Only approved revisions | 
| InvokeRegistryMcp | Only approved revisions | 
| GetRegistryRecord | Latest revision (any status) | 
| ListRegistryRecords | Latest revision (any status) | 