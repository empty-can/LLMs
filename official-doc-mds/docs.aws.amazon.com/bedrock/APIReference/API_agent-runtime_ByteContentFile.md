

# ByteContentFile
<a name="API_agent-runtime_ByteContentFile"></a>

The property contains the file to chat with, along with its attributes.

## Contents
<a name="API_agent-runtime_ByteContentFile_Contents"></a>

 ** data **   <a name="bedrock-Type-agent-runtime_ByteContentFile-data"></a>
The raw bytes of the file to attach. The maximum size of all files that is attached is 10MB. You can attach a maximum of 5 files.   
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 10485760.  
Required: Yes

 ** mediaType **   <a name="bedrock-Type-agent-runtime_ByteContentFile-mediaType"></a>
The MIME type of data contained in the file used for chat.  
Type: String  
Required: Yes

## See Also
<a name="API_agent-runtime_ByteContentFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ByteContentFile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ByteContentFile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ByteContentFile) 