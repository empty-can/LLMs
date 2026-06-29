

# ImageSource
<a name="API_agent-runtime_ImageSource"></a>

The source for an image.

## Contents
<a name="API_agent-runtime_ImageSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bytes **   <a name="bedrock-Type-agent-runtime_ImageSource-bytes"></a>
 The raw image bytes for the image. If you use an AWS SDK, you don't need to encode the image bytes in base64.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1.  
Required: No

 ** s3Location **   <a name="bedrock-Type-agent-runtime_ImageSource-s3Location"></a>
The path to the Amazon S3 bucket where the image is stored.  
Type: [S3Location](API_agent-runtime_S3Location.md) object  
Required: No

## See Also
<a name="API_agent-runtime_ImageSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ImageSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ImageSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ImageSource) 