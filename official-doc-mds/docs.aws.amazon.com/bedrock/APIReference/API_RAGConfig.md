

# RAGConfig
<a name="API_RAGConfig"></a>

Contains configuration details for retrieval of information and response generation.

## Contents
<a name="API_RAGConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** knowledgeBaseConfig **   <a name="bedrock-Type-RAGConfig-knowledgeBaseConfig"></a>
Contains configuration details for knowledge base retrieval and response generation.  
Type: [KnowledgeBaseConfig](API_KnowledgeBaseConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** precomputedRagSourceConfig **   <a name="bedrock-Type-RAGConfig-precomputedRagSourceConfig"></a>
Contains configuration details about the RAG source used to generate inference response data for a Knowledge Base evaluation job.  
Type: [EvaluationPrecomputedRagSourceConfig](API_EvaluationPrecomputedRagSourceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_RAGConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RAGConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RAGConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RAGConfig) 