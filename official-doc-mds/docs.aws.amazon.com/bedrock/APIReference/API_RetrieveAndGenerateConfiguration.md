

# RetrieveAndGenerateConfiguration
<a name="API_RetrieveAndGenerateConfiguration"></a>

Contains configuration details for a knowledge base retrieval and response generation.

## Contents
<a name="API_RetrieveAndGenerateConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-RetrieveAndGenerateConfiguration-type"></a>
The type of resource that contains your data for retrieving information and generating responses.  
If you choose to use `EXTERNAL_SOURCES`, then currently only Claude 3 Sonnet models for knowledge bases are supported.  
Type: String  
Valid Values: `KNOWLEDGE_BASE | EXTERNAL_SOURCES`   
Required: Yes

 ** externalSourcesConfiguration **   <a name="bedrock-Type-RetrieveAndGenerateConfiguration-externalSourcesConfiguration"></a>
The configuration for the external source wrapper object in the `retrieveAndGenerate` function.  
Type: [ExternalSourcesRetrieveAndGenerateConfiguration](API_ExternalSourcesRetrieveAndGenerateConfiguration.md) object  
Required: No

 ** knowledgeBaseConfiguration **   <a name="bedrock-Type-RetrieveAndGenerateConfiguration-knowledgeBaseConfiguration"></a>
Contains configuration details for the knowledge base retrieval and response generation.  
Type: [KnowledgeBaseRetrieveAndGenerateConfiguration](API_KnowledgeBaseRetrieveAndGenerateConfiguration.md) object  
Required: No

## See Also
<a name="API_RetrieveAndGenerateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RetrieveAndGenerateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RetrieveAndGenerateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RetrieveAndGenerateConfiguration) 