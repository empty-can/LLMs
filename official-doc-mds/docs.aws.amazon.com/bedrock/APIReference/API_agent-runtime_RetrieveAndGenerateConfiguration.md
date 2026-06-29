

# RetrieveAndGenerateConfiguration
<a name="API_agent-runtime_RetrieveAndGenerateConfiguration"></a>

Contains details about the resource being queried.

This data type is used in the following API operations:
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) – in the `retrieveAndGenerateConfiguration` field

## Contents
<a name="API_agent-runtime_RetrieveAndGenerateConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateConfiguration-type"></a>
The type of resource that contains your data for retrieving information and generating responses.  
If you choose to use `EXTERNAL_SOURCES`, then currently only Anthropic Claude 3 Sonnet models for knowledge bases are supported.
Type: String  
Valid Values: `KNOWLEDGE_BASE | EXTERNAL_SOURCES`   
Required: Yes

 ** externalSourcesConfiguration **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateConfiguration-externalSourcesConfiguration"></a>
The configuration for the external source wrapper object in the `retrieveAndGenerate` function.  
Type: [ExternalSourcesRetrieveAndGenerateConfiguration](API_agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration.md) object  
Required: No

 ** knowledgeBaseConfiguration **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateConfiguration-knowledgeBaseConfiguration"></a>
Contains details about the knowledge base for retrieving information and generating responses.  
Type: [KnowledgeBaseRetrieveAndGenerateConfiguration](API_agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_RetrieveAndGenerateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateConfiguration) 