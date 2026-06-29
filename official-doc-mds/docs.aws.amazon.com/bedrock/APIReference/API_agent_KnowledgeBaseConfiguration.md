

# KnowledgeBaseConfiguration
<a name="API_agent_KnowledgeBaseConfiguration"></a>

Contains details about the vector embeddings configuration of the knowledge base.

## Contents
<a name="API_agent_KnowledgeBaseConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_KnowledgeBaseConfiguration-type"></a>
The type of data that the data source is converted into for the knowledge base. Choose `MANAGED` to create a managed knowledge base.  
Type: String  
Valid Values: `VECTOR | KENDRA | SQL | MANAGED`   
Required: Yes

 ** kendraKnowledgeBaseConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseConfiguration-kendraKnowledgeBaseConfiguration"></a>
Settings for an Amazon Kendra knowledge base.  
Type: [KendraKnowledgeBaseConfiguration](API_agent_KendraKnowledgeBaseConfiguration.md) object  
Required: No

 ** managedKnowledgeBaseConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseConfiguration-managedKnowledgeBaseConfiguration"></a>
Contains configuration details for a knowledge base that uses a vector store fully managed by Amazon Bedrock. Specify this object when the knowledge base type is MANAGED.  
Type: [ManagedKnowledgeBaseConfiguration](API_agent_ManagedKnowledgeBaseConfiguration.md) object  
Required: No

 ** sqlKnowledgeBaseConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseConfiguration-sqlKnowledgeBaseConfiguration"></a>
Specifies configurations for a knowledge base connected to an SQL database.  
Type: [SqlKnowledgeBaseConfiguration](API_agent_SqlKnowledgeBaseConfiguration.md) object  
Required: No

 ** vectorKnowledgeBaseConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseConfiguration-vectorKnowledgeBaseConfiguration"></a>
Contains details about the model that's used to convert the data source into vector embeddings.  
Type: [VectorKnowledgeBaseConfiguration](API_agent_VectorKnowledgeBaseConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_KnowledgeBaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/KnowledgeBaseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/KnowledgeBaseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/KnowledgeBaseConfiguration) 