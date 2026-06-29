

# HarnessBedrockModelConfig
<a name="API_HarnessBedrockModelConfig"></a>

Configuration for an Amazon Bedrock model provider.

## Contents
<a name="API_HarnessBedrockModelConfig_Contents"></a>

 ** modelId **   <a name="bedrockagentcorecontrol-Type-HarnessBedrockModelConfig-modelId"></a>
The Bedrock model ID.  
Type: String  
Required: Yes

 ** additionalParams **   <a name="bedrockagentcorecontrol-Type-HarnessBedrockModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.  
Type: JSON value  
Required: No

 ** apiFormat **   <a name="bedrockagentcorecontrol-Type-HarnessBedrockModelConfig-apiFormat"></a>
The API format to use when calling the Bedrock provider.  
Type: String  
Valid Values: `converse_stream | responses | chat_completions`   
Required: No

 ** maxTokens **   <a name="bedrockagentcorecontrol-Type-HarnessBedrockModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per model call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** temperature **   <a name="bedrockagentcorecontrol-Type-HarnessBedrockModelConfig-temperature"></a>
The temperature to set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 2.0.  
Required: No

 ** topP **   <a name="bedrockagentcorecontrol-Type-HarnessBedrockModelConfig-topP"></a>
The topP set when calling the model.  
Type: Float  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

## See Also
<a name="API_HarnessBedrockModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessBedrockModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessBedrockModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessBedrockModelConfig) 