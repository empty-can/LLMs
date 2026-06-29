

# MongoDbAtlasConfiguration
<a name="API_agent_MongoDbAtlasConfiguration"></a>

Contains details about the storage configuration of the knowledge base in MongoDB Atlas. 

## Contents
<a name="API_agent_MongoDbAtlasConfiguration_Contents"></a>

 ** collectionName **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-collectionName"></a>
The collection name of the knowledge base in MongoDB Atlas.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `.*`   
Required: Yes

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that contains user credentials for your MongoDB Atlas cluster.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** databaseName **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-databaseName"></a>
The database name in your MongoDB Atlas cluster for your knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `.*`   
Required: Yes

 ** endpoint **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-endpoint"></a>
The endpoint URL of your MongoDB Atlas cluster for your knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

 ** fieldMapping **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [MongoDbAtlasFieldMapping](API_agent_MongoDbAtlasFieldMapping.md) object  
Required: Yes

 ** vectorIndexName **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-vectorIndexName"></a>
The name of the MongoDB Atlas vector search index.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

 ** endpointServiceName **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-endpointServiceName"></a>
The name of the VPC endpoint service in your account that is connected to your MongoDB Atlas cluster.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?:arn:aws(?:-us-gov|-cn|-iso|-iso-[a-z])*:.+:.*:\d+:.+/.+$|[a-zA-Z0-9*]+[a-zA-Z0-9._-]*)`   
Required: No

 ** textIndexName **   <a name="bedrock-Type-agent_MongoDbAtlasConfiguration-textIndexName"></a>
The name of the text search index in the MongoDB collection. This is required for using the hybrid search feature.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: No

## See Also
<a name="API_agent_MongoDbAtlasConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MongoDbAtlasConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MongoDbAtlasConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MongoDbAtlasConfiguration) 