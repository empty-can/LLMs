

# GuardrailManagedWordsConfig
<a name="API_GuardrailManagedWordsConfig"></a>

The managed word list to configure for the guardrail.

## Contents
<a name="API_GuardrailManagedWordsConfig_Contents"></a>

 ** type **   <a name="bedrock-Type-GuardrailManagedWordsConfig-type"></a>
The managed word type to configure for the guardrail.  
Type: String  
Valid Values: `PROFANITY`   
Required: Yes

 ** inputAction **   <a name="bedrock-Type-GuardrailManagedWordsConfig-inputAction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailManagedWordsConfig-inputEnabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailManagedWordsConfig-outputAction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailManagedWordsConfig-outputEnabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailManagedWordsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailManagedWordsConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailManagedWordsConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailManagedWordsConfig) 