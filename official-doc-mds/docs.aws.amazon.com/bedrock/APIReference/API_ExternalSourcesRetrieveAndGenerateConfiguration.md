

# ExternalSourcesRetrieveAndGenerateConfiguration
<a name="API_ExternalSourcesRetrieveAndGenerateConfiguration"></a>

The configuration of the external source wrapper object in the `retrieveAndGenerate` function.

## Contents
<a name="API_ExternalSourcesRetrieveAndGenerateConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-ExternalSourcesRetrieveAndGenerateConfiguration-modelArn"></a>
The Amazon Resource Name (ARN) of the foundation model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) used to generate responses.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** sources **   <a name="bedrock-Type-ExternalSourcesRetrieveAndGenerateConfiguration-sources"></a>
The document for the external source wrapper object in the `retrieveAndGenerate` function.  
Type: Array of [ExternalSource](API_ExternalSource.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** generationConfiguration **   <a name="bedrock-Type-ExternalSourcesRetrieveAndGenerateConfiguration-generationConfiguration"></a>
Contains configurations details for response generation based on retrieved text chunks.  
Type: [ExternalSourcesGenerationConfiguration](API_ExternalSourcesGenerationConfiguration.md) object  
Required: No

## See Also
<a name="API_ExternalSourcesRetrieveAndGenerateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ExternalSourcesRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ExternalSourcesRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ExternalSourcesRetrieveAndGenerateConfiguration) 