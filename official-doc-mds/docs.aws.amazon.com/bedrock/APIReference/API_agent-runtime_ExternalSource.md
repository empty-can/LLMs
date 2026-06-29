

# ExternalSource
<a name="API_agent-runtime_ExternalSource"></a>

The unique external source of the content contained in the wrapper object.

## Contents
<a name="API_agent-runtime_ExternalSource_Contents"></a>

 ** sourceType **   <a name="bedrock-Type-agent-runtime_ExternalSource-sourceType"></a>
The source type of the external source wrapper object.  
Type: String  
Valid Values: `S3 | BYTE_CONTENT`   
Required: Yes

 ** byteContent **   <a name="bedrock-Type-agent-runtime_ExternalSource-byteContent"></a>
The identifier, contentType, and data of the external source wrapper object.  
Type: [ByteContentDoc](API_agent-runtime_ByteContentDoc.md) object  
Required: No

 ** s3Location **   <a name="bedrock-Type-agent-runtime_ExternalSource-s3Location"></a>
The S3 location of the external source wrapper object.  
Type: [S3ObjectDoc](API_agent-runtime_S3ObjectDoc.md) object  
Required: No

## See Also
<a name="API_agent-runtime_ExternalSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ExternalSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ExternalSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ExternalSource) 