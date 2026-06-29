

# PromptModelInferenceConfiguration
<a name="API_agent_PromptModelInferenceConfiguration"></a>

Contains inference configurations related to model inference for a prompt. For more information, see [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html).

## Contents
<a name="API_agent_PromptModelInferenceConfiguration_Contents"></a>

 ** maxTokens **   <a name="bedrock-Type-agent_PromptModelInferenceConfiguration-maxTokens"></a>
The maximum number of tokens to return in the response.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** stopSequences **   <a name="bedrock-Type-agent_PromptModelInferenceConfiguration-stopSequences"></a>
A list of strings that define sequences after which the model will stop generating.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 4 items.  
Required: No

 ** temperature **   <a name="bedrock-Type-agent_PromptModelInferenceConfiguration-temperature"></a>
Controls the randomness of the response. Choose a lower value for more predictable outputs and a higher value for more surprising outputs.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** topP **   <a name="bedrock-Type-agent_PromptModelInferenceConfiguration-topP"></a>
The percentage of most-likely candidates that the model considers for the next token.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_agent_PromptModelInferenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptModelInferenceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptModelInferenceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptModelInferenceConfiguration) 