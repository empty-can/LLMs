

# GuardrailManagedWords
<a name="API_GuardrailManagedWords"></a>

The managed word list that was configured for the guardrail. (This is a list of words that are pre-defined and managed by guardrails only.)

## Contents
<a name="API_GuardrailManagedWords_Contents"></a>

 ** type **   <a name="bedrock-Type-GuardrailManagedWords-type"></a>
ManagedWords$type The managed word type that was configured for the guardrail. (For now, we only offer profanity word list)  
Type: String  
Valid Values: `PROFANITY`   
Required: Yes

 ** inputAction **   <a name="bedrock-Type-GuardrailManagedWords-inputAction"></a>
The action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailManagedWords-inputEnabled"></a>
Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailManagedWords-outputAction"></a>
The action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailManagedWords-outputEnabled"></a>
Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailManagedWords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailManagedWords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailManagedWords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailManagedWords) 