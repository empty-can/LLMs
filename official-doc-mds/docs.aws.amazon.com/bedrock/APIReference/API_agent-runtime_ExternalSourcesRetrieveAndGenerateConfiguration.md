

# ExternalSourcesRetrieveAndGenerateConfiguration
<a name="API_agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration"></a>

The configurations of the external source wrapper object in the `retrieveAndGenerate` function.

## Contents
<a name="API_agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration-modelArn"></a>
The model Amazon Resource Name (ARN) for the external source wrapper object in the `retrieveAndGenerate` function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** sources **   <a name="bedrock-Type-agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration-sources"></a>
The document for the external source wrapper object in the `retrieveAndGenerate` function.  
Type: Array of [ExternalSource](API_agent-runtime_ExternalSource.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** generationConfiguration **   <a name="bedrock-Type-agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration-generationConfiguration"></a>
The prompt used with the external source wrapper object with the `retrieveAndGenerate` function.  
Type: [ExternalSourcesGenerationConfiguration](API_agent-runtime_ExternalSourcesGenerationConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ExternalSourcesRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ExternalSourcesRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ExternalSourcesRetrieveAndGenerateConfiguration) 