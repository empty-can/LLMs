

# ConverseTokensRequest
<a name="API_runtime_ConverseTokensRequest"></a>

The inputs from a `Converse` API request for token counting.

This structure mirrors the input format for the `Converse` operation, allowing you to count tokens for conversation-based inference requests.

## Contents
<a name="API_runtime_ConverseTokensRequest_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-runtime_ConverseTokensRequest-additionalModelRequestFields"></a>
The additionalModelRequestFields of Converse input request to count tokens for. Use this field when you want to pass additional parameters that the model supports.  
Type: JSON value  
Required: No

 ** messages **   <a name="bedrock-Type-runtime_ConverseTokensRequest-messages"></a>
An array of messages to count tokens for.  
Type: Array of [Message](API_runtime_Message.md) objects  
Required: No

 ** system **   <a name="bedrock-Type-runtime_ConverseTokensRequest-system"></a>
The system content blocks to count tokens for. System content provides instructions or context to the model about how it should behave or respond. The token count will include any system content provided.  
Type: Array of [SystemContentBlock](API_runtime_SystemContentBlock.md) objects  
Required: No

 ** toolConfig **   <a name="bedrock-Type-runtime_ConverseTokensRequest-toolConfig"></a>
The toolConfig of Converse input request to count tokens for. Configuration information for the tools that the model can use when generating a response.  
Type: [ToolConfiguration](API_runtime_ToolConfiguration.md) object  
Required: No

## See Also
<a name="API_runtime_ConverseTokensRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ConverseTokensRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ConverseTokensRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ConverseTokensRequest) 