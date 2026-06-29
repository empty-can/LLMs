

# VectorKnowledgeBaseConfiguration
<a name="API_agent_VectorKnowledgeBaseConfiguration"></a>

Contains details about the model used to create vector embeddings for the knowledge base.

## Contents
<a name="API_agent_VectorKnowledgeBaseConfiguration_Contents"></a>

 ** embeddingModelArn **   <a name="bedrock-Type-agent_VectorKnowledgeBaseConfiguration-embeddingModelArn"></a>
The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** embeddingModelConfiguration **   <a name="bedrock-Type-agent_VectorKnowledgeBaseConfiguration-embeddingModelConfiguration"></a>
The embeddings model configuration details for the vector model used in Knowledge Base.  
Type: [EmbeddingModelConfiguration](API_agent_EmbeddingModelConfiguration.md) object  
Required: No

 ** supplementalDataStorageConfiguration **   <a name="bedrock-Type-agent_VectorKnowledgeBaseConfiguration-supplementalDataStorageConfiguration"></a>
If you include multimodal data from your data source, use this object to specify configurations for the storage location of the images extracted from your documents. These images can be retrieved and returned to the end user. They can also be used in generation when using [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html).  
Type: [SupplementalDataStorageConfiguration](API_agent_SupplementalDataStorageConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_VectorKnowledgeBaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/VectorKnowledgeBaseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/VectorKnowledgeBaseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/VectorKnowledgeBaseConfiguration) 