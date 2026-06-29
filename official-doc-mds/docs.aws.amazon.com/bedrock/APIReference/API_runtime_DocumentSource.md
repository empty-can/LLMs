

# DocumentSource
<a name="API_runtime_DocumentSource"></a>

Contains the content of a document.

## Contents
<a name="API_runtime_DocumentSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bytes **   <a name="bedrock-Type-runtime_DocumentSource-bytes"></a>
The raw bytes for the document. If you use an AWS SDK, you don't need to encode the bytes in base64.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1.  
Required: No

 ** content **   <a name="bedrock-Type-runtime_DocumentSource-content"></a>
The structured content of the document source, which may include various content blocks such as text, images, or other document elements.  
Type: Array of [DocumentContentBlock](API_runtime_DocumentContentBlock.md) objects  
Required: No

 ** s3Location **   <a name="bedrock-Type-runtime_DocumentSource-s3Location"></a>
The location of a document object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).  
Type: [S3Location](API_runtime_S3Location.md) object  
Required: No

 ** text **   <a name="bedrock-Type-runtime_DocumentSource-text"></a>
The text content of the document source.  
Type: String  
Required: No

## See Also
<a name="API_runtime_DocumentSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/DocumentSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/DocumentSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/DocumentSource) 