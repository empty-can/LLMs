

# GuardrailRegexConfig
<a name="API_GuardrailRegexConfig"></a>

The regular expression to configure for the guardrail.

## Contents
<a name="API_GuardrailRegexConfig_Contents"></a>

 ** action **   <a name="bedrock-Type-GuardrailRegexConfig-action"></a>
The guardrail action to configure when matching regular expression is detected.  
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: Yes

 ** name **   <a name="bedrock-Type-GuardrailRegexConfig-name"></a>
The name of the regular expression to configure for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** pattern **   <a name="bedrock-Type-GuardrailRegexConfig-pattern"></a>
The regular expression pattern to configure for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

 ** description **   <a name="bedrock-Type-GuardrailRegexConfig-description"></a>
The description of the regular expression to configure for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** inputAction **   <a name="bedrock-Type-GuardrailRegexConfig-inputAction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailRegexConfig-inputEnabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailRegexConfig-outputAction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailRegexConfig-outputEnabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailRegexConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailRegexConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailRegexConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailRegexConfig) 