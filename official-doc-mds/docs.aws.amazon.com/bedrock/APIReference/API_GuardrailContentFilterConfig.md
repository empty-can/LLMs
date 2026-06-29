

# GuardrailContentFilterConfig
<a name="API_GuardrailContentFilterConfig"></a>

Contains filter strengths for harmful content. Guardrails support the following content filters to detect and filter harmful user inputs and FM-generated outputs.
+  **Hate** – Describes language or a statement that discriminates, criticizes, insults, denounces, or dehumanizes a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
+  **Insults** – Describes language or a statement that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
+  **Sexual** – Describes language or a statement that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
+  **Violence** – Describes language or a statement that includes glorification of or threats to inflict physical pain, hurt, or injury toward a person, group or thing.

Content filtering depends on the confidence classification of user inputs and FM responses across each of the four harmful categories. All input and output statements are classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each harmful category. For example, if a statement is classified as *Hate* with HIGH confidence, the likelihood of the statement representing hateful content is high. A single statement can be classified across multiple categories with varying confidence levels. For example, a single statement can be classified as *Hate* with HIGH confidence, *Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

For more information, see [Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-filters.html).

## Contents
<a name="API_GuardrailContentFilterConfig_Contents"></a>

 ** inputStrength **   <a name="bedrock-Type-GuardrailContentFilterConfig-inputStrength"></a>
The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.  
Type: String  
Valid Values: `NONE | LOW | MEDIUM | HIGH`   
Required: Yes

 ** outputStrength **   <a name="bedrock-Type-GuardrailContentFilterConfig-outputStrength"></a>
The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.  
Type: String  
Valid Values: `NONE | LOW | MEDIUM | HIGH`   
Required: Yes

 ** type **   <a name="bedrock-Type-GuardrailContentFilterConfig-type"></a>
The harmful category that the content filter is applied to.  
Type: String  
Valid Values: `SEXUAL | VIOLENCE | HATE | INSULTS | MISCONDUCT | PROMPT_ATTACK`   
Required: Yes

 ** inputAction **   <a name="bedrock-Type-GuardrailContentFilterConfig-inputAction"></a>
Specifies the action to take when harmful content is detected. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailContentFilterConfig-inputEnabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** inputModalities **   <a name="bedrock-Type-GuardrailContentFilterConfig-inputModalities"></a>
The input modalities selected for the guardrail content filter configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Valid Values: `TEXT | IMAGE`   
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailContentFilterConfig-outputAction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailContentFilterConfig-outputEnabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputModalities **   <a name="bedrock-Type-GuardrailContentFilterConfig-outputModalities"></a>
The output modalities selected for the guardrail content filter configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Valid Values: `TEXT | IMAGE`   
Required: No

## See Also
<a name="API_GuardrailContentFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContentFilterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContentFilterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContentFilterConfig) 