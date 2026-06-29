

# HarnessGeminiModelConfig
<a name="API_HarnessGeminiModelConfig"></a>

Configuration for a Google Gemini model provider. Requires an API key stored in AgentCore Identity.

## Contents
<a name="API_HarnessGeminiModelConfig_Contents"></a>

 ** apiKeyArn **   <a name="bedrockagentcorecontrol-Type-HarnessGeminiModelConfig-apiKeyArn"></a>
The ARN of your Gemini API key on AgentCore Identity.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** modelId **   <a name="bedrockagentcorecontrol-Type-HarnessGeminiModelConfig-modelId"></a>
The Gemini model ID.  
Type: String  
Required: Yes

 ** maxTokens **   <a name="bedrockagentcorecontrol-Type-HarnessGeminiModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per model call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="bedrockagentcorecontrol-Type-HarnessGeminiModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topK **   <a name="bedrockagentcorecontrol-Type-HarnessGeminiModelConfig-topK"></a>
The topK set when calling the model.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 500.  
Required: No

 ** topP **   <a name="bedrockagentcorecontrol-Type-HarnessGeminiModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

## See Also
<a name="API_HarnessGeminiModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessGeminiModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessGeminiModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessGeminiModelConfig) 