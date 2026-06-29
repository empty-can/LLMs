

# InferenceConfiguration
<a name="API_agent-runtime_InferenceConfiguration"></a>

Specifications about the inference parameters that were provided alongside the prompt. These are specified in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) object that was set when the agent was created or updated. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

## Contents
<a name="API_agent-runtime_InferenceConfiguration_Contents"></a>

 ** maximumLength **   <a name="bedrock-Type-agent-runtime_InferenceConfiguration-maximumLength"></a>
The maximum number of tokens allowed in the generated response.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 8192.  
Required: No

 ** stopSequences **   <a name="bedrock-Type-agent-runtime_InferenceConfiguration-stopSequences"></a>
A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 4 items.  
Required: No

 ** temperature **   <a name="bedrock-Type-agent-runtime_InferenceConfiguration-temperature"></a>
The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** topK **   <a name="bedrock-Type-agent-runtime_InferenceConfiguration-topK"></a>
While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for `topK` is the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set `topK` to 50, the model selects the next token from among the top 50 most likely choices.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 500.  
Required: No

 ** topP **   <a name="bedrock-Type-agent-runtime_InferenceConfiguration-topP"></a>
While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for `Top P` determines the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set `topP` to 0.8, the model only selects the next token from the top 80% of the probability distribution of next tokens.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_agent-runtime_InferenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InferenceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InferenceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InferenceConfiguration) 