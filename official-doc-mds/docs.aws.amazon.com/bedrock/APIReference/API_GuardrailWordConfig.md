

# GuardrailWordConfig
<a name="API_GuardrailWordConfig"></a>

A word to configure for the guardrail.

## Contents
<a name="API_GuardrailWordConfig_Contents"></a>

 ** text **   <a name="bedrock-Type-GuardrailWordConfig-text"></a>
Text of the word configured for the guardrail to block.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** inputAction **   <a name="bedrock-Type-GuardrailWordConfig-inputAction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailWordConfig-inputEnabled"></a>
Specifies whether to enable guardrail evaluation on the intput. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailWordConfig-outputAction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailWordConfig-outputEnabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailWordConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailWordConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailWordConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailWordConfig) 