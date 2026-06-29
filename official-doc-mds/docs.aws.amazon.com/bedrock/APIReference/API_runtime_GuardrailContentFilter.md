

# GuardrailContentFilter
<a name="API_runtime_GuardrailContentFilter"></a>

The content filter for a guardrail.

## Contents
<a name="API_runtime_GuardrailContentFilter_Contents"></a>

 ** action **   <a name="bedrock-Type-runtime_GuardrailContentFilter-action"></a>
The guardrail action.  
Type: String  
Valid Values: `BLOCKED | NONE`   
Required: Yes

 ** confidence **   <a name="bedrock-Type-runtime_GuardrailContentFilter-confidence"></a>
The guardrail confidence.  
Type: String  
Valid Values: `NONE | LOW | MEDIUM | HIGH`   
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_GuardrailContentFilter-type"></a>
The guardrail type.  
Type: String  
Valid Values: `INSULTS | HATE | SEXUAL | VIOLENCE | MISCONDUCT | PROMPT_ATTACK`   
Required: Yes

 ** detected **   <a name="bedrock-Type-runtime_GuardrailContentFilter-detected"></a>
Indicates whether content that breaches the guardrail configuration is detected.  
Type: Boolean  
Required: No

 ** filterStrength **   <a name="bedrock-Type-runtime_GuardrailContentFilter-filterStrength"></a>
The filter strength setting for the guardrail content filter.  
Type: String  
Valid Values: `NONE | LOW | MEDIUM | HIGH`   
Required: No

## See Also
<a name="API_runtime_GuardrailContentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailContentFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailContentFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailContentFilter) 