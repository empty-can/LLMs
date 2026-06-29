

# KnowledgeBaseRetrievalConfiguration
<a name="API_agent-runtime_KnowledgeBaseRetrievalConfiguration"></a>

Contains configurations for knowledge base query. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).

This data type is used in the following API operations:
+  [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) – in the `retrievalConfiguration` field
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) – in the `retrievalConfiguration` field

## Contents
<a name="API_agent-runtime_KnowledgeBaseRetrievalConfiguration_Contents"></a>

 ** managedSearchConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalConfiguration-managedSearchConfiguration"></a>
Contains configurations for managed search. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).  
Type: [ManagedSearchConfiguration](API_agent-runtime_ManagedSearchConfiguration.md) object  
Required: No

 ** vectorSearchConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalConfiguration-vectorSearchConfiguration"></a>
Contains details about how the results from the vector search should be returned. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).  
Type: [KnowledgeBaseVectorSearchConfiguration](API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseRetrievalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrievalConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrievalConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrievalConfiguration) 