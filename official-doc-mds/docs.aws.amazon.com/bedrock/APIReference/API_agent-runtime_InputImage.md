

# InputImage
<a name="API_agent-runtime_InputImage"></a>

Contains the image data for multimodal knowledge base queries, including format and content.

This data type is used in the following API operations:
+  [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) – in the `image` field

## Contents
<a name="API_agent-runtime_InputImage_Contents"></a>

 ** format **   <a name="bedrock-Type-agent-runtime_InputImage-format"></a>
The format of the input image. Supported formats include png, gif, jpeg, and webp.  
Type: String  
Valid Values: `png | jpeg | gif | webp`   
Required: Yes

 ** inlineContent **   <a name="bedrock-Type-agent-runtime_InputImage-inlineContent"></a>
The base64-encoded image data for inline image content. Maximum size is 5MB.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 5242880.  
Required: Yes

## See Also
<a name="API_agent-runtime_InputImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InputImage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InputImage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InputImage) 