

# ManagedKnowledgeBaseConnectorConfiguration
<a name="API_agent_ManagedKnowledgeBaseConnectorConfiguration"></a>

Configuration for managed knowledge base connector data sources.

## Contents
<a name="API_agent_ManagedKnowledgeBaseConnectorConfiguration_Contents"></a>

 ** connectorParameters **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConnectorConfiguration-connectorParameters"></a>
Connector-specific parameters. For more information, see [Connect a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-connect-ds.html).  
Type: JSON value  
Required: No

 ** deletionProtectionConfiguration **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConnectorConfiguration-deletionProtectionConfiguration"></a>
A safeguard against accidental bulk deletion of indexed content.  
Type: [DeletionProtectionConfiguration](API_agent_DeletionProtectionConfiguration.md) object  
Required: No

 ** mediaExtractionConfiguration **   <a name="bedrock-Type-agent_ManagedKnowledgeBaseConnectorConfiguration-mediaExtractionConfiguration"></a>
Configuration for extracting media (images, audio, video) from data source files.  
Type: [MediaExtractionConfiguration](API_agent_MediaExtractionConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_ManagedKnowledgeBaseConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ManagedKnowledgeBaseConnectorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ManagedKnowledgeBaseConnectorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ManagedKnowledgeBaseConnectorConfiguration) 