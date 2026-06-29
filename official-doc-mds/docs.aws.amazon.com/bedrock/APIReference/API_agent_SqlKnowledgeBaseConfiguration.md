

# SqlKnowledgeBaseConfiguration
<a name="API_agent_SqlKnowledgeBaseConfiguration"></a>

Contains configurations for a knowledge base connected to an SQL database. Specify the SQL database type in the `type` field and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_SqlKnowledgeBaseConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_SqlKnowledgeBaseConfiguration-type"></a>
The type of SQL database to connect to the knowledge base.  
Type: String  
Valid Values: `REDSHIFT`   
Required: Yes

 ** redshiftConfiguration **   <a name="bedrock-Type-agent_SqlKnowledgeBaseConfiguration-redshiftConfiguration"></a>
Specifies configurations for a knowledge base connected to an Amazon Redshift database.  
Type: [RedshiftConfiguration](API_agent_RedshiftConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_SqlKnowledgeBaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SqlKnowledgeBaseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SqlKnowledgeBaseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SqlKnowledgeBaseConfiguration) 