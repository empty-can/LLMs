

# HarnessOpenAiModelConfig
<a name="API_HarnessOpenAiModelConfig"></a>

Configuration for an OpenAI model provider. Requires an API key stored in AgentCore Identity.

## Contents
<a name="API_HarnessOpenAiModelConfig_Contents"></a>

 ** apiKeyArn **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-apiKeyArn"></a>
The ARN of your OpenAI API key on AgentCore Identity.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** modelId **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-modelId"></a>
The OpenAI model ID.  
Type: String  
Required: Yes

 ** additionalParams **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.  
Type: JSON value  
Required: No

 ** apiFormat **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-apiFormat"></a>
The API format to use when calling the OpenAI provider.  
Type: String  
Valid Values: `chat_completions | responses`   
Required: No

 ** maxTokens **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per model call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topP **   <a name="bedrockagentcorecontrol-Type-HarnessOpenAiModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

## See Also
<a name="API_HarnessOpenAiModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessOpenAiModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessOpenAiModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessOpenAiModelConfig) 