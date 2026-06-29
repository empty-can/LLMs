

# DataSource
<a name="API_agent_DataSource"></a>

Contains details about a data source.

## Contents
<a name="API_agent_DataSource_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent_DataSource-createdAt"></a>
The time at which the data source was created.  
Type: Timestamp  
Required: Yes

 ** dataSourceConfiguration **   <a name="bedrock-Type-agent_DataSource-dataSourceConfiguration"></a>
The connection configuration for the data source.  
Type: [DataSourceConfiguration](API_agent_DataSourceConfiguration.md) object  
Required: Yes

 ** dataSourceId **   <a name="bedrock-Type-agent_DataSource-dataSourceId"></a>
The unique identifier of the data source.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_DataSource-knowledgeBaseId"></a>
The unique identifier of the knowledge base to which the data source belongs.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_DataSource-name"></a>
The name of the data source.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_DataSource-status"></a>
The status of the data source. The following statuses are possible:  
+ Available – The data source has been created and is ready for ingestion into the knowledge base.
+ Deleting – The data source is being deleted.
Type: String  
Valid Values: `AVAILABLE | DELETING | DELETE_UNSUCCESSFUL | CREATING | UPDATING | FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_DataSource-updatedAt"></a>
The time at which the data source was last updated.  
Type: Timestamp  
Required: Yes

 ** dataDeletionPolicy **   <a name="bedrock-Type-agent_DataSource-dataDeletionPolicy"></a>
The data deletion policy for the data source.  
Type: String  
Valid Values: `RETAIN | DELETE`   
Required: No

 ** description **   <a name="bedrock-Type-agent_DataSource-description"></a>
The description of the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** failureReasons **   <a name="bedrock-Type-agent_DataSource-failureReasons"></a>
The detailed reasons on the failure to delete a data source.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** serverSideEncryptionConfiguration **   <a name="bedrock-Type-agent_DataSource-serverSideEncryptionConfiguration"></a>
Contains details about the configuration of the server-side encryption.  
Type: [ServerSideEncryptionConfiguration](API_agent_ServerSideEncryptionConfiguration.md) object  
Required: No

 ** vectorIngestionConfiguration **   <a name="bedrock-Type-agent_DataSource-vectorIngestionConfiguration"></a>
Contains details about how to ingest the documents in the data source.  
Type: [VectorIngestionConfiguration](API_agent_VectorIngestionConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DataSource) 