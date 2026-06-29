

# AgenticRetrieveBedrockGuardrailConfiguration
<a name="API_agent-runtime_AgenticRetrieveBedrockGuardrailConfiguration"></a>

Configuration for a Bedrock guardrail applied during agentic retrieval.

## Contents
<a name="API_agent-runtime_AgenticRetrieveBedrockGuardrailConfiguration_Contents"></a>

 ** guardrailId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveBedrockGuardrailConfiguration-guardrailId"></a>
The unique identifier of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: Yes

 ** guardrailVersion **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveBedrockGuardrailConfiguration-guardrailVersion"></a>
The version of the guardrail to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))`   
Required: Yes

## See Also
<a name="API_agent-runtime_AgenticRetrieveBedrockGuardrailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveBedrockGuardrailConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveBedrockGuardrailConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveBedrockGuardrailConfiguration) 