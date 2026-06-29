

# HarnessLiteLlmModelConfig
<a name="API_HarnessLiteLlmModelConfig"></a>

Configuration for a LiteLLM model provider, enabling connection to third-party model providers.

## Contents
<a name="API_HarnessLiteLlmModelConfig_Contents"></a>

 ** modelId **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-modelId"></a>
The LiteLLM model identifier (e.g., "anthropic/claude-3-sonnet").  
Type: String  
Required: Yes

 ** additionalParams **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.  
Type: JSON value  
Required: No

 ** apiBase **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-apiBase"></a>
The base URL for the model provider's API endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16383.  
Required: No

 ** apiKeyArn **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-apiKeyArn"></a>
The ARN of the API key in AgentCore Identity for authenticating with the model provider.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: No

 ** maxTokens **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topP **   <a name="bedrockagentcorecontrol-Type-HarnessLiteLlmModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

## See Also
<a name="API_HarnessLiteLlmModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessLiteLlmModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessLiteLlmModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessLiteLlmModelConfig) 