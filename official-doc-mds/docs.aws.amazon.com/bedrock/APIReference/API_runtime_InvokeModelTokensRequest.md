

# InvokeModelTokensRequest
<a name="API_runtime_InvokeModelTokensRequest"></a>

The body of an `InvokeModel` API request for token counting. This structure mirrors the input format for the `InvokeModel` operation, allowing you to count tokens for raw text inference requests.

## Contents
<a name="API_runtime_InvokeModelTokensRequest_Contents"></a>

 ** body **   <a name="bedrock-Type-runtime_InvokeModelTokensRequest-body"></a>
The request body to count tokens for, formatted according to the model's expected input format. To learn about the input format for different models, see [Model inference parameters and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 0. Maximum length of 25000000.  
Required: Yes

## See Also
<a name="API_runtime_InvokeModelTokensRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/InvokeModelTokensRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/InvokeModelTokensRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/InvokeModelTokensRequest) 