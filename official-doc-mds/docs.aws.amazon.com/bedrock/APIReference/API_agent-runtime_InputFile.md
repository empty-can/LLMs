

# InputFile
<a name="API_agent-runtime_InputFile"></a>

Contains details of the source files.

## Contents
<a name="API_agent-runtime_InputFile_Contents"></a>

 ** name **   <a name="bedrock-Type-agent-runtime_InputFile-name"></a>
The name of the source file.  
Type: String  
Required: Yes

 ** source **   <a name="bedrock-Type-agent-runtime_InputFile-source"></a>
Specifies where the files are located.  
Type: [FileSource](API_agent-runtime_FileSource.md) object  
Required: Yes

 ** useCase **   <a name="bedrock-Type-agent-runtime_InputFile-useCase"></a>
Specifies how the source files will be used by the code interpreter.  
Type: String  
Valid Values: `CODE_INTERPRETER | CHAT`   
Required: Yes

## See Also
<a name="API_agent-runtime_InputFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InputFile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InputFile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InputFile) 