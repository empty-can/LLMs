

# InferenceConfiguration
<a name="API_runtime_InferenceConfiguration"></a>

Base inference parameters to pass to a model in a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html). For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

If you need to pass additional parameters that the model supports, use the `additionalModelRequestFields` request field in the call to `Converse` or `ConverseStream`. For more information, see [Model parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

## Contents
<a name="API_runtime_InferenceConfiguration_Contents"></a>

 ** maxTokens **   <a name="bedrock-Type-runtime_InferenceConfiguration-maxTokens"></a>
The maximum number of tokens to allow in the generated response. The default value is the maximum allowed value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).   
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** stopSequences **   <a name="bedrock-Type-runtime_InferenceConfiguration-stopSequences"></a>
A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2500 items.  
Length Constraints: Minimum length of 1.  
Required: No

 ** temperature **   <a name="bedrock-Type-runtime_InferenceConfiguration-temperature"></a>
The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.  
The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).   
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** topP **   <a name="bedrock-Type-runtime_InferenceConfiguration-topP"></a>
The percentage of most-likely candidates that the model considers for the next token. For example, if you choose a value of 0.8 for `topP`, the model selects from the top 80% of the probability distribution of tokens that could be next in the sequence.  
The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).   
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_runtime_InferenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/InferenceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/InferenceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/InferenceConfiguration) 