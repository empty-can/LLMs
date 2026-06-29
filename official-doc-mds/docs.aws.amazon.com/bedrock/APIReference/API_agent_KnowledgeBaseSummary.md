

# KnowledgeBaseSummary
<a name="API_agent_KnowledgeBaseSummary"></a>

Contains details about a knowledge base.

## Contents
<a name="API_agent_KnowledgeBaseSummary_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_KnowledgeBaseSummary-knowledgeBaseId"></a>
The unique identifier of the knowledge base.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_KnowledgeBaseSummary-name"></a>
The name of the knowledge base.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_KnowledgeBaseSummary-status"></a>
The status of the knowledge base.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | FAILED | DELETE_UNSUCCESSFUL | UPDATE_UNSUCCESSFUL`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_KnowledgeBaseSummary-updatedAt"></a>
The time the knowledge base was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_KnowledgeBaseSummary-description"></a>
The description of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_KnowledgeBaseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/KnowledgeBaseSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/KnowledgeBaseSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/KnowledgeBaseSummary) 