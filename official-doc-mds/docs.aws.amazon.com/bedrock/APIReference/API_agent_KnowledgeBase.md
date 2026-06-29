

# KnowledgeBase
<a name="API_agent_KnowledgeBase"></a>

Contains information about a knowledge base.

## Contents
<a name="API_agent_KnowledgeBase_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent_KnowledgeBase-createdAt"></a>
The time the knowledge base was created.  
Type: Timestamp  
Required: Yes

 ** knowledgeBaseArn **   <a name="bedrock-Type-agent_KnowledgeBase-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+`   
Required: Yes

 ** knowledgeBaseConfiguration **   <a name="bedrock-Type-agent_KnowledgeBase-knowledgeBaseConfiguration"></a>
Contains details about the embeddings configuration of the knowledge base.  
Type: [KnowledgeBaseConfiguration](API_agent_KnowledgeBaseConfiguration.md) object  
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_KnowledgeBase-knowledgeBaseId"></a>
The unique identifier of the knowledge base.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_KnowledgeBase-name"></a>
The name of the knowledge base.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** roleArn **   <a name="bedrock-Type-agent_KnowledgeBase-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_KnowledgeBase-status"></a>
The status of the knowledge base. The following statuses are possible:  
+ CREATING – The knowledge base is being created.
+ ACTIVE – The knowledge base is ready to be queried.
+ DELETING – The knowledge base is being deleted.
+ UPDATING – The knowledge base is being updated.
+ FAILED – The knowledge base API operation failed.
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | FAILED | DELETE_UNSUCCESSFUL | UPDATE_UNSUCCESSFUL`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_KnowledgeBase-updatedAt"></a>
The time the knowledge base was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_KnowledgeBase-description"></a>
The description of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** failureReasons **   <a name="bedrock-Type-agent_KnowledgeBase-failureReasons"></a>
A list of reasons that the API operation on the knowledge base failed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** storageConfiguration **   <a name="bedrock-Type-agent_KnowledgeBase-storageConfiguration"></a>
Contains details about the storage configuration of the knowledge base.  
Type: [StorageConfiguration](API_agent_StorageConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_KnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/KnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/KnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/KnowledgeBase) 