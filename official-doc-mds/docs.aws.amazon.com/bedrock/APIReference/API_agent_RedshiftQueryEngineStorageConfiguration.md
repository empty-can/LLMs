

# RedshiftQueryEngineStorageConfiguration
<a name="API_agent_RedshiftQueryEngineStorageConfiguration"></a>

Contains configurations for Amazon Redshift data storage. Specify the data storage service to use in the `type` field and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_RedshiftQueryEngineStorageConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_RedshiftQueryEngineStorageConfiguration-type"></a>
The data storage service to use.  
Type: String  
Valid Values: `REDSHIFT | AWS_DATA_CATALOG`   
Required: Yes

 ** awsDataCatalogConfiguration **   <a name="bedrock-Type-agent_RedshiftQueryEngineStorageConfiguration-awsDataCatalogConfiguration"></a>
Specifies configurations for storage in AWS Glue Data Catalog.  
Type: [RedshiftQueryEngineAwsDataCatalogStorageConfiguration](API_agent_RedshiftQueryEngineAwsDataCatalogStorageConfiguration.md) object  
Required: No

 ** redshiftConfiguration **   <a name="bedrock-Type-agent_RedshiftQueryEngineStorageConfiguration-redshiftConfiguration"></a>
Specifies configurations for storage in Amazon Redshift.  
Type: [RedshiftQueryEngineRedshiftStorageConfiguration](API_agent_RedshiftQueryEngineRedshiftStorageConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_RedshiftQueryEngineStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftQueryEngineStorageConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftQueryEngineStorageConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftQueryEngineStorageConfiguration) 