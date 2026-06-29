

# InferenceConfiguration
<a name="API_InferenceConfiguration"></a>

Inference parameters for a model.

## Contents
<a name="API_InferenceConfiguration_Contents"></a>

 ** maxTokens **   <a name="bedrock-Type-InferenceConfiguration-maxTokens"></a>
The maximum number of tokens to generate.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** stopSequences **   <a name="bedrock-Type-InferenceConfiguration-stopSequences"></a>
Stop sequences that end generation.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2500 items.  
Length Constraints: Minimum length of 1.  
Required: No

 ** temperature **   <a name="bedrock-Type-InferenceConfiguration-temperature"></a>
The temperature for sampling.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** topP **   <a name="bedrock-Type-InferenceConfiguration-topP"></a>
The top-p value for nucleus sampling.  
Type: Float  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_InferenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/InferenceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/InferenceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/InferenceConfiguration) 