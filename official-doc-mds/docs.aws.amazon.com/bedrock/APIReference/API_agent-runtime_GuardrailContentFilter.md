

# GuardrailContentFilter
<a name="API_agent-runtime_GuardrailContentFilter"></a>

Details of the content filter used in the Guardrail.

## Contents
<a name="API_agent-runtime_GuardrailContentFilter_Contents"></a>

 ** action **   <a name="bedrock-Type-agent-runtime_GuardrailContentFilter-action"></a>
The action placed on the content by the Guardrail filter.  
Type: String  
Valid Values: `BLOCKED`   
Required: No

 ** confidence **   <a name="bedrock-Type-agent-runtime_GuardrailContentFilter-confidence"></a>
The confidence level regarding the content detected in the filter by the Guardrail.  
Type: String  
Valid Values: `NONE | LOW | MEDIUM | HIGH`   
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_GuardrailContentFilter-type"></a>
The type of content detected in the filter by the Guardrail.  
Type: String  
Valid Values: `INSULTS | HATE | SEXUAL | VIOLENCE | MISCONDUCT | PROMPT_ATTACK`   
Required: No

## See Also
<a name="API_agent-runtime_GuardrailContentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GuardrailContentFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GuardrailContentFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GuardrailContentFilter) 