

# GuardrailConfiguration
<a name="API_agent_GuardrailConfiguration"></a>

Details about a guardrail associated with a resource.

## Contents
<a name="API_agent_GuardrailConfiguration_Contents"></a>

 ** guardrailIdentifier **   <a name="bedrock-Type-agent_GuardrailConfiguration-guardrailIdentifier"></a>
The unique identifier of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: No

 ** guardrailVersion **   <a name="bedrock-Type-agent_GuardrailConfiguration-guardrailVersion"></a>
The version of the guardrail.  
Type: String  
Pattern: `(([0-9]{1,8})|(DRAFT))`   
Required: No

## See Also
<a name="API_agent_GuardrailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GuardrailConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GuardrailConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GuardrailConfiguration) 