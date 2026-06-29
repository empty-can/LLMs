

# RedisEnterpriseCloudConfiguration
<a name="API_agent_RedisEnterpriseCloudConfiguration"></a>

Contains details about the storage configuration of the knowledge base in Redis Enterprise Cloud. For more information, see [Create a vector index in Redis Enterprise Cloud](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html).

## Contents
<a name="API_agent_RedisEnterpriseCloudConfiguration_Contents"></a>

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_RedisEnterpriseCloudConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that is linked to your Redis Enterprise Cloud database.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** endpoint **   <a name="bedrock-Type-agent_RedisEnterpriseCloudConfiguration-endpoint"></a>
The endpoint URL of the Redis Enterprise Cloud database.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

 ** fieldMapping **   <a name="bedrock-Type-agent_RedisEnterpriseCloudConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [RedisEnterpriseCloudFieldMapping](API_agent_RedisEnterpriseCloudFieldMapping.md) object  
Required: Yes

 ** vectorIndexName **   <a name="bedrock-Type-agent_RedisEnterpriseCloudConfiguration-vectorIndexName"></a>
The name of the vector index.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

## See Also
<a name="API_agent_RedisEnterpriseCloudConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedisEnterpriseCloudConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedisEnterpriseCloudConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedisEnterpriseCloudConfiguration) 