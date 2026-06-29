

# StorageConfiguration
<a name="API_agent_StorageConfiguration"></a>

Contains the storage configuration of the knowledge base.

## Contents
<a name="API_agent_StorageConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_StorageConfiguration-type"></a>
The vector store service in which the knowledge base is stored.  
Type: String  
Valid Values: `OPENSEARCH_SERVERLESS | PINECONE | REDIS_ENTERPRISE_CLOUD | RDS | MONGO_DB_ATLAS | NEPTUNE_ANALYTICS | OPENSEARCH_MANAGED_CLUSTER | S3_VECTORS`   
Required: Yes

 ** mongoDbAtlasConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-mongoDbAtlasConfiguration"></a>
Contains the storage configuration of the knowledge base in MongoDB Atlas.  
Type: [MongoDbAtlasConfiguration](API_agent_MongoDbAtlasConfiguration.md) object  
Required: No

 ** neptuneAnalyticsConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-neptuneAnalyticsConfiguration"></a>
Contains details about the Neptune Analytics configuration of the knowledge base in Amazon Neptune. For more information, see [Create a vector index in Amazon Neptune Analytics.](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html).  
Type: [NeptuneAnalyticsConfiguration](API_agent_NeptuneAnalyticsConfiguration.md) object  
Required: No

 ** opensearchManagedClusterConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-opensearchManagedClusterConfiguration"></a>
Contains details about the storage configuration of the knowledge base in OpenSearch Managed Cluster. For more information, see [Create a vector index in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html).  
Type: [OpenSearchManagedClusterConfiguration](API_agent_OpenSearchManagedClusterConfiguration.md) object  
Required: No

 ** opensearchServerlessConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-opensearchServerlessConfiguration"></a>
Contains the storage configuration of the knowledge base in Amazon OpenSearch Service.  
Type: [OpenSearchServerlessConfiguration](API_agent_OpenSearchServerlessConfiguration.md) object  
Required: No

 ** pineconeConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-pineconeConfiguration"></a>
Contains the storage configuration of the knowledge base in Pinecone.  
Type: [PineconeConfiguration](API_agent_PineconeConfiguration.md) object  
Required: No

 ** rdsConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-rdsConfiguration"></a>
Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see [Create a vector index in Amazon RDS](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html).  
Type: [RdsConfiguration](API_agent_RdsConfiguration.md) object  
Required: No

 ** redisEnterpriseCloudConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-redisEnterpriseCloudConfiguration"></a>
Contains the storage configuration of the knowledge base in Redis Enterprise Cloud.  
Type: [RedisEnterpriseCloudConfiguration](API_agent_RedisEnterpriseCloudConfiguration.md) object  
Required: No

 ** s3VectorsConfiguration **   <a name="bedrock-Type-agent_StorageConfiguration-s3VectorsConfiguration"></a>
The configuration settings for storing knowledge base data using S3 vectors. This includes vector index information and S3 bucket details for vector storage.  
Type: [S3VectorsConfiguration](API_agent_S3VectorsConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_StorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/StorageConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/StorageConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/StorageConfiguration) 