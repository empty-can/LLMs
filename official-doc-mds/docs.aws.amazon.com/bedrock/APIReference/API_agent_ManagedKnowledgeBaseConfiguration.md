

# ManagedKnowledgeBaseConfiguration
<a name="API_agent_ManagedKnowledgeBaseConfiguration"></a>

Configurations for a managed knowledge base.

## Contents
<a name="API_agent_ManagedKnowledgeBaseConfiguration_Contents"></a>

 ** embeddingModelArn **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConfiguration-embeddingModelArn"></a>
The ARN for the embeddings model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: No

 ** embeddingModelConfiguration **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConfiguration-embeddingModelConfiguration"></a>
The configuration details for the embeddings model. Not required when choosing the MANAGED embeddingModelType.  
Type: [EmbeddingModelConfiguration](API_agent_EmbeddingModelConfiguration.md) object  
Required: No

 ** embeddingModelType **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConfiguration-embeddingModelType"></a>
Choose CUSTOM to provide your own Bedrock embedding model ARN. Choose MANAGED to use a service-managed embedding model.  
Type: String  
Valid Values: `CUSTOM | MANAGED`   
Required: No

 ** serverSideEncryptionConfiguration **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConfiguration-serverSideEncryptionConfiguration"></a>
Contains the configuration for server-side encryption for your managed knowledge base.  
Type: [ServerSideEncryptionConfiguration](API_agent_ServerSideEncryptionConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_ManagedKnowledgeBaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ManagedKnowledgeBaseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ManagedKnowledgeBaseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ManagedKnowledgeBaseConfiguration) 