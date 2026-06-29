

# FileSource
<a name="API_agent-runtime_FileSource"></a>

The source file of the content contained in the wrapper object.

## Contents
<a name="API_agent-runtime_FileSource_Contents"></a>

 ** sourceType **   <a name="bedrock-Type-agent-runtime_FileSource-sourceType"></a>
The source type of the files to attach.  
Type: String  
Valid Values: `S3 | BYTE_CONTENT`   
Required: Yes

 ** byteContent **   <a name="bedrock-Type-agent-runtime_FileSource-byteContent"></a>
The data and the text of the attached files.  
Type: [ByteContentFile](API_agent-runtime_ByteContentFile.md) object  
Required: No

 ** s3Location **   <a name="bedrock-Type-agent-runtime_FileSource-s3Location"></a>
The s3 location of the files to attach.  
Type: [S3ObjectFile](API_agent-runtime_S3ObjectFile.md) object  
Required: No

## See Also
<a name="API_agent-runtime_FileSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FileSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FileSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FileSource) 