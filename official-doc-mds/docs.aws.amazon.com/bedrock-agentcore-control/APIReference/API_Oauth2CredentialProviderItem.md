

# Oauth2CredentialProviderItem
<a name="API_Oauth2CredentialProviderItem"></a>

Contains information about an OAuth2 credential provider.

## Contents
<a name="API_Oauth2CredentialProviderItem_Contents"></a>

 ** createdTime **   <a name="bedrockagentcorecontrol-Type-Oauth2CredentialProviderItem-createdTime"></a>
The timestamp when the OAuth2 credential provider was created.  
Type: Timestamp  
Required: Yes

 ** credentialProviderArn **   <a name="bedrockagentcorecontrol-Type-Oauth2CredentialProviderItem-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the OAuth2 credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/oauth2credentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** credentialProviderVendor **   <a name="bedrockagentcorecontrol-Type-Oauth2CredentialProviderItem-credentialProviderVendor"></a>
The vendor of the OAuth2 credential provider.  
Type: String  
Valid Values: `GoogleOauth2 | GithubOauth2 | SlackOauth2 | SalesforceOauth2 | MicrosoftOauth2 | CustomOauth2 | AtlassianOauth2 | LinkedinOauth2 | XOauth2 | OktaOauth2 | OneLoginOauth2 | PingOneOauth2 | FacebookOauth2 | YandexOauth2 | RedditOauth2 | ZoomOauth2 | TwitchOauth2 | SpotifyOauth2 | DropboxOauth2 | NotionOauth2 | HubspotOauth2 | CyberArkOauth2 | FusionAuthOauth2 | Auth0Oauth2 | CognitoOauth2`   
Required: Yes

 ** lastUpdatedTime **   <a name="bedrockagentcorecontrol-Type-Oauth2CredentialProviderItem-lastUpdatedTime"></a>
The timestamp when the OAuth2 credential provider was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-Oauth2CredentialProviderItem-name"></a>
The name of the OAuth2 credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

## See Also
<a name="API_Oauth2CredentialProviderItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Oauth2CredentialProviderItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Oauth2CredentialProviderItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Oauth2CredentialProviderItem) 