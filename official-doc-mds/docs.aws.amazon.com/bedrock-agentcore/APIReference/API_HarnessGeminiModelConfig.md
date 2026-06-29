

# HarnessGeminiModelConfig
<a name="API_HarnessGeminiModelConfig"></a>

Configuration for a Google Gemini model provider. Requires an API key stored in AgentCore Identity.

## Contents
<a name="API_HarnessGeminiModelConfig_Contents"></a>

 ** apiKeyArn **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-apiKeyArn"></a>
The ARN of your Gemini API key on AgentCore Identity.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** modelId **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-modelId"></a>
The Gemini model ID.  
Type: String  
Required: Yes

 ** maxTokens **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topK **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-topK"></a>
The topK set when calling the model.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 500.  
Required: No

 ** topP **   <a name="BedrockAgentCore-Type-HarnessGeminiModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

## See Also
<a name="API_HarnessGeminiModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessGeminiModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessGeminiModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessGeminiModelConfig) 