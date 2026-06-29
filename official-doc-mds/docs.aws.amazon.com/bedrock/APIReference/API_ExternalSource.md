

# ExternalSource
<a name="API_ExternalSource"></a>

The unique external source of the content contained in the wrapper object.

## Contents
<a name="API_ExternalSource_Contents"></a>

 ** sourceType **   <a name="bedrock-Type-ExternalSource-sourceType"></a>
The source type of the external source wrapper object.  
Type: String  
Valid Values: `S3 | BYTE_CONTENT`   
Required: Yes

 ** byteContent **   <a name="bedrock-Type-ExternalSource-byteContent"></a>
The identifier, content type, and data of the external source wrapper object.  
Type: [ByteContentDoc](API_ByteContentDoc.md) object  
Required: No

 ** s3Location **   <a name="bedrock-Type-ExternalSource-s3Location"></a>
The S3 location of the external source wrapper object.  
Type: [S3ObjectDoc](API_S3ObjectDoc.md) object  
Required: No

## See Also
<a name="API_ExternalSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ExternalSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ExternalSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ExternalSource) 