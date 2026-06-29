

# IncludedOauth2ProviderConfigInput
<a name="API_IncludedOauth2ProviderConfigInput"></a>

Configuration settings for connecting to a supported OAuth2 provider. This includes client credentials and OAuth2 discovery information for providers that have built-in support.

## Contents
<a name="API_IncludedOauth2ProviderConfigInput_Contents"></a>

 ** clientId **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-clientId"></a>
The client ID for the supported OAuth2 provider. This identifier is assigned by the OAuth2 provider when you register your application.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** authorizationEndpoint **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-authorizationEndpoint"></a>
OAuth2 authorization endpoint for your isolated OAuth2 application tenant. This is where users are redirected to authenticate and authorize access to their resources.  
Type: String  
Required: No

 ** clientSecret **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-clientSecret"></a>
The client secret for the supported OAuth2 provider. This secret is assigned by the OAuth2 provider and used along with the client ID to authenticate your application.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** clientSecretConfig **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-clientSecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** clientSecretSource **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-clientSecretSource"></a>
The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** issuer **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-issuer"></a>
Token issuer of your isolated OAuth2 application tenant. This URL identifies the authorization server that issues tokens for this provider.  
Type: String  
Required: No

 ** tokenEndpoint **   <a name="bedrockagentcorecontrol-Type-IncludedOauth2ProviderConfigInput-tokenEndpoint"></a>
OAuth2 token endpoint for your isolated OAuth2 application tenant. This is where authorization codes are exchanged for access tokens.  
Type: String  
Required: No

## See Also
<a name="API_IncludedOauth2ProviderConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/IncludedOauth2ProviderConfigInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/IncludedOauth2ProviderConfigInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/IncludedOauth2ProviderConfigInput) 