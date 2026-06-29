

# RedshiftQueryEngineConfiguration
<a name="API_agent_RedshiftQueryEngineConfiguration"></a>

Contains configurations for an Amazon Redshift query engine. Specify the type of query engine in `type` and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_RedshiftQueryEngineConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_RedshiftQueryEngineConfiguration-type"></a>
The type of query engine.  
Type: String  
Valid Values: `SERVERLESS | PROVISIONED`   
Required: Yes

 ** provisionedConfiguration **   <a name="bedrock-Type-agent_RedshiftQueryEngineConfiguration-provisionedConfiguration"></a>
Specifies configurations for a provisioned Amazon Redshift query engine.  
Type: [RedshiftProvisionedConfiguration](API_agent_RedshiftProvisionedConfiguration.md) object  
Required: No

 ** serverlessConfiguration **   <a name="bedrock-Type-agent_RedshiftQueryEngineConfiguration-serverlessConfiguration"></a>
Specifies configurations for a serverless Amazon Redshift query engine.  
Type: [RedshiftServerlessConfiguration](API_agent_RedshiftServerlessConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_RedshiftQueryEngineConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftQueryEngineConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftQueryEngineConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftQueryEngineConfiguration) 