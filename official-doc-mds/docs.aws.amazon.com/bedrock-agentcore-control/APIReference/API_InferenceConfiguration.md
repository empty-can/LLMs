

# InferenceConfiguration
<a name="API_InferenceConfiguration"></a>

 The configuration parameters that control how the foundation model behaves during evaluation, including response generation settings. 

## Contents
<a name="API_InferenceConfiguration_Contents"></a>

 ** maxTokens **   <a name="bedrockagentcorecontrol-Type-InferenceConfiguration-maxTokens"></a>
 The maximum number of tokens to generate in the model response during evaluation.   
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** stopSequences **   <a name="bedrockagentcorecontrol-Type-InferenceConfiguration-stopSequences"></a>
 The list of sequences that will cause the model to stop generating tokens when encountered.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2500 items.  
Length Constraints: Minimum length of 1.  
Required: No

 ** temperature **   <a name="bedrockagentcorecontrol-Type-InferenceConfiguration-temperature"></a>
 The temperature value that controls randomness in the model's responses. Lower values produce more deterministic outputs.   
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** topP **   <a name="bedrockagentcorecontrol-Type-InferenceConfiguration-topP"></a>
 The top-p sampling parameter that controls the diversity of the model's responses by limiting the cumulative probability of token choices.   
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_InferenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InferenceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InferenceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InferenceConfiguration) 