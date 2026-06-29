

# DataSourceConfiguration
<a name="API_agent_DataSourceConfiguration"></a>

The connection configuration for the data source.

## Contents
<a name="API_agent_DataSourceConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_DataSourceConfiguration-type"></a>
The type of data source.  
Type: String  
Valid Values: `S3 | WEB | CONFLUENCE | SALESFORCE | SHAREPOINT | CUSTOM | REDSHIFT_METADATA | MANAGED_KNOWLEDGE_BASE_CONNECTOR`   
Required: Yes

 ** confluenceConfiguration **   <a name="bedrock-Type-agent_DataSourceConfiguration-confluenceConfiguration"></a>
The configuration information to connect to Confluence as your data source for self-managed knowledge bases.  
To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html). Confluence data source connector for self-managed knowledge bases is in preview release and is subject to change.
Type: [ConfluenceDataSourceConfiguration](API_agent_ConfluenceDataSourceConfiguration.md) object  
Required: No

 ** managedKnowledgeBaseConnectorConfiguration **   <a name="bedrock-Type-agent_DataSourceConfiguration-managedKnowledgeBaseConnectorConfiguration"></a>
Contains the configuration for a data source that connects a managed knowledge base to a supported data source connector. Specify this object when the data source type is `MANAGED_KNOWLEDGE_BASE_CONNECTOR`.  
Type: [ManagedKnowledgeBaseConnectorConfiguration](API_agent_ManagedKnowledgeBaseConnectorConfiguration.md) object  
Required: No

 ** s3Configuration **   <a name="bedrock-Type-agent_DataSourceConfiguration-s3Configuration"></a>
The configuration information to connect to Amazon S3 as your data source for self-managed knowledge bases. To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html).  
Type: [S3DataSourceConfiguration](API_agent_S3DataSourceConfiguration.md) object  
Required: No

 ** salesforceConfiguration **   <a name="bedrock-Type-agent_DataSourceConfiguration-salesforceConfiguration"></a>
The configuration information to connect to Salesforce as your data source.  
Salesforce data source connector for self-managed knowledge bases is in preview release and is subject to change.
Type: [SalesforceDataSourceConfiguration](API_agent_SalesforceDataSourceConfiguration.md) object  
Required: No

 ** sharePointConfiguration **   <a name="bedrock-Type-agent_DataSourceConfiguration-sharePointConfiguration"></a>
The configuration information to connect to SharePoint as your data source for self-managed knowledge bases.  
To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html). SharePoint data source connector for self-managed knowledge bases is in preview release and is subject to change.
Type: [SharePointDataSourceConfiguration](API_agent_SharePointDataSourceConfiguration.md) object  
Required: No

 ** webConfiguration **   <a name="bedrock-Type-agent_DataSourceConfiguration-webConfiguration"></a>
The configuration of web URLs to crawl for your data source. You should be authorized to crawl the URLs.  
To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html). Web crawler data source connector for self-managed knowledge bases is in preview release and is subject to change.
Type: [WebDataSourceConfiguration](API_agent_WebDataSourceConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DataSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DataSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DataSourceConfiguration) 