

# GuardrailRegex
<a name="API_GuardrailRegex"></a>

The regular expression configured for the guardrail.

## Contents
<a name="API_GuardrailRegex_Contents"></a>

 ** action **   <a name="bedrock-Type-GuardrailRegex-action"></a>
The action taken when a match to the regular expression is detected.  
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: Yes

 ** name **   <a name="bedrock-Type-GuardrailRegex-name"></a>
The name of the regular expression for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** pattern **   <a name="bedrock-Type-GuardrailRegex-pattern"></a>
The pattern of the regular expression configured for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

 ** description **   <a name="bedrock-Type-GuardrailRegex-description"></a>
The description of the regular expression for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** inputAction **   <a name="bedrock-Type-GuardrailRegex-inputAction"></a>
The action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailRegex-inputEnabled"></a>
Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailRegex-outputAction"></a>
The action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailRegex-outputEnabled"></a>
Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailRegex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailRegex) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailRegex) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailRegex) 