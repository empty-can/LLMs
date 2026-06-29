

# RdsConfiguration
<a name="API_agent_RdsConfiguration"></a>

Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see [Create a vector index in Amazon RDS](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html).

## Contents
<a name="API_agent_RdsConfiguration_Contents"></a>

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_RdsConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that is linked to your Amazon RDS database.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** databaseName **   <a name="bedrock-Type-agent_RdsConfiguration-databaseName"></a>
The name of your Amazon RDS database.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

 ** fieldMapping **   <a name="bedrock-Type-agent_RdsConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [RdsFieldMapping](API_agent_RdsFieldMapping.md) object  
Required: Yes

 ** resourceArn **   <a name="bedrock-Type-agent_RdsConfiguration-resourceArn"></a>
The Amazon Resource Name (ARN) of the vector store.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):rds:[a-zA-Z0-9-]*:[0-9]{12}:cluster:[a-zA-Z0-9-]{1,63}`   
Required: Yes

 ** tableName **   <a name="bedrock-Type-agent_RdsConfiguration-tableName"></a>
The name of the table in the database.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\.\-]+`   
Required: Yes

## See Also
<a name="API_agent_RdsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RdsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RdsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RdsConfiguration) 