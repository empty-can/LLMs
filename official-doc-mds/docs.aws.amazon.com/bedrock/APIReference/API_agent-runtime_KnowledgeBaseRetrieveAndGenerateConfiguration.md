

# KnowledgeBaseRetrieveAndGenerateConfiguration
<a name="API_agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration"></a>

Contains details about the resource being queried.

This data type is used in the following API operations:
+  [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) – in the `knowledgeBaseConfiguration` field
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) – in the `knowledgeBaseConfiguration` field

## Contents
<a name="API_agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration-knowledgeBaseId"></a>
The unique identifier of the knowledge base that is queried.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** modelArn **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration-modelArn"></a>
The ARN of the foundation model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) used to generate a response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** generationConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration-generationConfiguration"></a>
Contains configurations for response generation based on the knowledge base query results.  
Type: [GenerationConfiguration](API_agent-runtime_GenerationConfiguration.md) object  
Required: No

 ** orchestrationConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration-orchestrationConfiguration"></a>
Settings for how the model processes the prompt prior to retrieval and generation.  
Type: [OrchestrationConfiguration](API_agent-runtime_OrchestrationConfiguration.md) object  
Required: No

 ** retrievalConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration-retrievalConfiguration"></a>
Contains configurations for how to retrieve and return the knowledge base query.  
Type: [KnowledgeBaseRetrievalConfiguration](API_agent-runtime_KnowledgeBaseRetrievalConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseRetrieveAndGenerateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrieveAndGenerateConfiguration) 