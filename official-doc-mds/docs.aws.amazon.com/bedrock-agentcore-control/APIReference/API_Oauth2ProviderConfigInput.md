

# Oauth2ProviderConfigInput
<a name="API_Oauth2ProviderConfigInput"></a>

Contains the input configuration for an OAuth2 provider.

## Contents
<a name="API_Oauth2ProviderConfigInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** atlassianOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-atlassianOauth2ProviderConfig"></a>
Configuration settings for Atlassian OAuth2 provider integration.  
Type: [AtlassianOauth2ProviderConfigInput](API_AtlassianOauth2ProviderConfigInput.md) object  
Required: No

 ** customOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-customOauth2ProviderConfig"></a>
The configuration for a custom OAuth2 provider.  
Type: [CustomOauth2ProviderConfigInput](API_CustomOauth2ProviderConfigInput.md) object  
Required: No

 ** githubOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-githubOauth2ProviderConfig"></a>
The configuration for a GitHub OAuth2 provider.  
Type: [GithubOauth2ProviderConfigInput](API_GithubOauth2ProviderConfigInput.md) object  
Required: No

 ** googleOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-googleOauth2ProviderConfig"></a>
The configuration for a Google OAuth2 provider.  
Type: [GoogleOauth2ProviderConfigInput](API_GoogleOauth2ProviderConfigInput.md) object  
Required: No

 ** includedOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-includedOauth2ProviderConfig"></a>
The configuration for a non-custom OAuth2 provider. This includes settings for supported OAuth2 providers that have built-in integration support.  
Type: [IncludedOauth2ProviderConfigInput](API_IncludedOauth2ProviderConfigInput.md) object  
Required: No

 ** linkedinOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-linkedinOauth2ProviderConfig"></a>
Configuration settings for LinkedIn OAuth2 provider integration.  
Type: [LinkedinOauth2ProviderConfigInput](API_LinkedinOauth2ProviderConfigInput.md) object  
Required: No

 ** microsoftOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-microsoftOauth2ProviderConfig"></a>
The configuration for a Microsoft OAuth2 provider.  
Type: [MicrosoftOauth2ProviderConfigInput](API_MicrosoftOauth2ProviderConfigInput.md) object  
Required: No

 ** salesforceOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-salesforceOauth2ProviderConfig"></a>
The configuration for a Salesforce OAuth2 provider.  
Type: [SalesforceOauth2ProviderConfigInput](API_SalesforceOauth2ProviderConfigInput.md) object  
Required: No

 ** slackOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigInput-slackOauth2ProviderConfig"></a>
The configuration for a Slack OAuth2 provider.  
Type: [SlackOauth2ProviderConfigInput](API_SlackOauth2ProviderConfigInput.md) object  
Required: No

## See Also
<a name="API_Oauth2ProviderConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Oauth2ProviderConfigInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Oauth2ProviderConfigInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Oauth2ProviderConfigInput) 