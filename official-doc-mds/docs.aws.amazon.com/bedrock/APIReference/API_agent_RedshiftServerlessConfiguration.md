

# RedshiftServerlessConfiguration
<a name="API_agent_RedshiftServerlessConfiguration"></a>

Contains configurations for authentication to Amazon Redshift Serverless.

## Contents
<a name="API_agent_RedshiftServerlessConfiguration_Contents"></a>

 ** authConfiguration **   <a name="bedrock-Type-agent_RedshiftServerlessConfiguration-authConfiguration"></a>
Specifies configurations for authentication to an Amazon Redshift provisioned data warehouse.  
Type: [RedshiftServerlessAuthConfiguration](API_agent_RedshiftServerlessAuthConfiguration.md) object  
Required: Yes

 ** workgroupArn **   <a name="bedrock-Type-agent_RedshiftServerlessConfiguration-workgroupArn"></a>
The ARN of the Amazon Redshift workgroup.  
Type: String  
Pattern: `(arn:(aws(-[a-z]+)*):redshift-serverless:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`   
Required: Yes

## See Also
<a name="API_agent_RedshiftServerlessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftServerlessConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftServerlessConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftServerlessConfiguration) 