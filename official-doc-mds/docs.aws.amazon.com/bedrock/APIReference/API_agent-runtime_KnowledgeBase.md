

# KnowledgeBase
<a name="API_agent-runtime_KnowledgeBase"></a>

 Details of the knowledge base associated withe inline agent. 

## Contents
<a name="API_agent-runtime_KnowledgeBase_Contents"></a>

 ** description **   <a name="bedrock-Type-agent-runtime_KnowledgeBase-description"></a>
 The description of the knowledge base associated with the inline agent.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent-runtime_KnowledgeBase-knowledgeBaseId"></a>
 The unique identifier for a knowledge base associated with the inline agent.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** retrievalConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBase-retrievalConfiguration"></a>
 The configurations to apply to the knowledge base during query. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).   
Type: [KnowledgeBaseRetrievalConfiguration](API_agent-runtime_KnowledgeBaseRetrievalConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBase) 