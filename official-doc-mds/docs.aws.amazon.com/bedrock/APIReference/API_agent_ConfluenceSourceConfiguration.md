

# ConfluenceSourceConfiguration
<a name="API_agent_ConfluenceSourceConfiguration"></a>

The endpoint information to connect to your Confluence data source.

## Contents
<a name="API_agent_ConfluenceSourceConfiguration_Contents"></a>

 ** authType **   <a name="bedrock-Type-agent_ConfluenceSourceConfiguration-authType"></a>
The supported authentication type to authenticate and connect to your Confluence instance.  
Type: String  
Valid Values: `BASIC | OAUTH2_CLIENT_CREDENTIALS`   
Required: Yes

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_ConfluenceSourceConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name of an AWS Secrets Manager secret that stores your authentication credentials for your Confluence instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [Confluence connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html#configuration-confluence-connector).  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** hostType **   <a name="bedrock-Type-agent_ConfluenceSourceConfiguration-hostType"></a>
The supported host type, whether online/cloud or server/on-premises.  
Type: String  
Valid Values: `SAAS`   
Required: Yes

 ** hostUrl **   <a name="bedrock-Type-agent_ConfluenceSourceConfiguration-hostUrl"></a>
The Confluence host URL or instance URL.  
Type: String  
Pattern: `https://[A-Za-z0-9][^\s]*`   
Required: Yes

## See Also
<a name="API_agent_ConfluenceSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ConfluenceSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ConfluenceSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ConfluenceSourceConfiguration) 