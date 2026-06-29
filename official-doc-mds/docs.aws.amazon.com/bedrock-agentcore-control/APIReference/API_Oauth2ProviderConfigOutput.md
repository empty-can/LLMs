

# Oauth2ProviderConfigOutput
<a name="API_Oauth2ProviderConfigOutput"></a>

Contains the output configuration for an OAuth2 provider.

## Contents
<a name="API_Oauth2ProviderConfigOutput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** atlassianOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-atlassianOauth2ProviderConfig"></a>
The configuration details for the Atlassian OAuth2 provider.  
Type: [AtlassianOauth2ProviderConfigOutput](API_AtlassianOauth2ProviderConfigOutput.md) object  
Required: No

 ** customOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-customOauth2ProviderConfig"></a>
The output configuration for a custom OAuth2 provider.  
Type: [CustomOauth2ProviderConfigOutput](API_CustomOauth2ProviderConfigOutput.md) object  
Required: No

 ** githubOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-githubOauth2ProviderConfig"></a>
The output configuration for a GitHub OAuth2 provider.  
Type: [GithubOauth2ProviderConfigOutput](API_GithubOauth2ProviderConfigOutput.md) object  
Required: No

 ** googleOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-googleOauth2ProviderConfig"></a>
The output configuration for a Google OAuth2 provider.  
Type: [GoogleOauth2ProviderConfigOutput](API_GoogleOauth2ProviderConfigOutput.md) object  
Required: No

 ** includedOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-includedOauth2ProviderConfig"></a>
The configuration for a non-custom OAuth2 provider. This includes the configuration details for supported OAuth2 providers that have built-in integration support.  
Type: [IncludedOauth2ProviderConfigOutput](API_IncludedOauth2ProviderConfigOutput.md) object  
Required: No

 ** linkedinOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-linkedinOauth2ProviderConfig"></a>
The configuration details for the LinkedIn OAuth2 provider.  
Type: [LinkedinOauth2ProviderConfigOutput](API_LinkedinOauth2ProviderConfigOutput.md) object  
Required: No

 ** microsoftOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-microsoftOauth2ProviderConfig"></a>
The output configuration for a Microsoft OAuth2 provider.  
Type: [MicrosoftOauth2ProviderConfigOutput](API_MicrosoftOauth2ProviderConfigOutput.md) object  
Required: No

 ** salesforceOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-salesforceOauth2ProviderConfig"></a>
The output configuration for a Salesforce OAuth2 provider.  
Type: [SalesforceOauth2ProviderConfigOutput](API_SalesforceOauth2ProviderConfigOutput.md) object  
Required: No

 ** slackOauth2ProviderConfig **   <a name="bedrockagentcorecontrol-Type-Oauth2ProviderConfigOutput-slackOauth2ProviderConfig"></a>
The output configuration for a Slack OAuth2 provider.  
Type: [SlackOauth2ProviderConfigOutput](API_SlackOauth2ProviderConfigOutput.md) object  
Required: No

## See Also
<a name="API_Oauth2ProviderConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Oauth2ProviderConfigOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Oauth2ProviderConfigOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Oauth2ProviderConfigOutput) 