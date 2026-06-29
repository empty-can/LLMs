

# CountTokensInput
<a name="API_runtime_CountTokensInput"></a>

The input value for token counting. The value should be either an `InvokeModel` or `Converse` request body. 

## Contents
<a name="API_runtime_CountTokensInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** converse **   <a name="bedrock-Type-runtime_CountTokensInput-converse"></a>
A `Converse` request for which to count tokens. Use this field when you want to count tokens for a conversation-based input that would be sent to the `Converse` operation.  
Type: [ConverseTokensRequest](API_runtime_ConverseTokensRequest.md) object  
Required: No

 ** invokeModel **   <a name="bedrock-Type-runtime_CountTokensInput-invokeModel"></a>
An `InvokeModel` request for which to count tokens. Use this field when you want to count tokens for a raw text input that would be sent to the `InvokeModel` operation.  
Type: [InvokeModelTokensRequest](API_runtime_InvokeModelTokensRequest.md) object  
Required: No

## See Also
<a name="API_runtime_CountTokensInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CountTokensInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CountTokensInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CountTokensInput) 