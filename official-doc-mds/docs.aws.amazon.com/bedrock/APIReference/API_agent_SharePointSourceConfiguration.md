

# SharePointSourceConfiguration
<a name="API_agent_SharePointSourceConfiguration"></a>

The endpoint information to connect to your SharePoint data source.

## Contents
<a name="API_agent_SharePointSourceConfiguration_Contents"></a>

 ** authType **   <a name="bedrock-Type-agent_SharePointSourceConfiguration-authType"></a>
The supported authentication type to authenticate and connect to your SharePoint site/sites.  
Type: String  
Valid Values: `OAUTH2_CLIENT_CREDENTIALS | OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS`   
Required: Yes

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_SharePointSourceConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name of an AWS Secrets Manager secret that stores your authentication credentials for your SharePoint site/sites. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [SharePoint connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html#configuration-sharepoint-connector).  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** domain **   <a name="bedrock-Type-agent_SharePointSourceConfiguration-domain"></a>
The domain of your SharePoint instance or site URL/URLs.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** hostType **   <a name="bedrock-Type-agent_SharePointSourceConfiguration-hostType"></a>
The supported host type, whether online/cloud or server/on-premises.  
Type: String  
Valid Values: `ONLINE`   
Required: Yes

 ** siteUrls **   <a name="bedrock-Type-agent_SharePointSourceConfiguration-siteUrls"></a>
A list of one or more SharePoint site URLs.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Pattern: `https://[A-Za-z0-9][^\s]*`   
Required: Yes

 ** tenantId **   <a name="bedrock-Type-agent_SharePointSourceConfiguration-tenantId"></a>
The identifier of your Microsoft 365 tenant.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

## See Also
<a name="API_agent_SharePointSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SharePointSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SharePointSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SharePointSourceConfiguration) 