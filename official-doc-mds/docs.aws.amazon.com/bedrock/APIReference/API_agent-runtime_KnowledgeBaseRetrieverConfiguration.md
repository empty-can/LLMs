

# KnowledgeBaseRetrieverConfiguration
<a name="API_agent-runtime_KnowledgeBaseRetrieverConfiguration"></a>

Configuration for retrieving from a Bedrock knowledge base.

## Contents
<a name="API_agent-runtime_KnowledgeBaseRetrieverConfiguration_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieverConfiguration-knowledgeBaseId"></a>
The unique identifier of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** retrievalOverrides **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrieverConfiguration-retrievalOverrides"></a>
Overrides for retrieval behavior such as filters and result limits.  
Type: [RetrievalOverrides](API_agent-runtime_RetrievalOverrides.md) object  
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseRetrieverConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrieverConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrieverConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrieverConfiguration) 