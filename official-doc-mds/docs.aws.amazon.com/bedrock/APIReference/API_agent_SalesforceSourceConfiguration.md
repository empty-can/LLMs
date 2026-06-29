

# SalesforceSourceConfiguration
<a name="API_agent_SalesforceSourceConfiguration"></a>

The endpoint information to connect to your Salesforce data source.

## Contents
<a name="API_agent_SalesforceSourceConfiguration_Contents"></a>

 ** authType **   <a name="bedrock-Type-agent_SalesforceSourceConfiguration-authType"></a>
The supported authentication type to authenticate and connect to your Salesforce instance.  
Type: String  
Valid Values: `OAUTH2_CLIENT_CREDENTIALS`   
Required: Yes

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_SalesforceSourceConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name of an AWS Secrets Manager secret that stores your authentication credentials for your Salesforce instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [Salesforce connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html#configuration-salesforce-connector).  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** hostUrl **   <a name="bedrock-Type-agent_SalesforceSourceConfiguration-hostUrl"></a>
The Salesforce host URL or instance URL.  
Type: String  
Pattern: `https://[A-Za-z0-9][^\s]*`   
Required: Yes

## See Also
<a name="API_agent_SalesforceSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SalesforceSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SalesforceSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SalesforceSourceConfiguration) 