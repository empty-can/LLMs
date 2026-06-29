

# RedshiftConfiguration
<a name="API_agent_RedshiftConfiguration"></a>

Contains configurations for an Amazon Redshift database. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_RedshiftConfiguration_Contents"></a>

 ** queryEngineConfiguration **   <a name="bedrock-Type-agent_RedshiftConfiguration-queryEngineConfiguration"></a>
Specifies configurations for an Amazon Redshift query engine.  
Type: [RedshiftQueryEngineConfiguration](API_agent_RedshiftQueryEngineConfiguration.md) object  
Required: Yes

 ** storageConfigurations **   <a name="bedrock-Type-agent_RedshiftConfiguration-storageConfigurations"></a>
Specifies configurations for Amazon Redshift database storage.  
Type: Array of [RedshiftQueryEngineStorageConfiguration](API_agent_RedshiftQueryEngineStorageConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** queryGenerationConfiguration **   <a name="bedrock-Type-agent_RedshiftConfiguration-queryGenerationConfiguration"></a>
Specifies configurations for generating queries.  
Type: [QueryGenerationConfiguration](API_agent_QueryGenerationConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_RedshiftConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftConfiguration) 