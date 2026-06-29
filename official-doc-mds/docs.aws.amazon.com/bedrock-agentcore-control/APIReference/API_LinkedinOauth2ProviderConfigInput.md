

# LinkedinOauth2ProviderConfigInput
<a name="API_LinkedinOauth2ProviderConfigInput"></a>

Configuration settings for connecting to LinkedIn services using OAuth2 authentication. This includes the client credentials required to authenticate with LinkedIn's OAuth2 authorization server.

## Contents
<a name="API_LinkedinOauth2ProviderConfigInput_Contents"></a>

 ** clientId **   <a name="bedrockagentcorecontrol-Type-LinkedinOauth2ProviderConfigInput-clientId"></a>
The client ID for the LinkedIn OAuth2 provider. This identifier is assigned by LinkedIn when you register your application.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** clientSecret **   <a name="bedrockagentcorecontrol-Type-LinkedinOauth2ProviderConfigInput-clientSecret"></a>
The client secret for the LinkedIn OAuth2 provider. This secret is assigned by LinkedIn and used along with the client ID to authenticate your application.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** clientSecretConfig **   <a name="bedrockagentcorecontrol-Type-LinkedinOauth2ProviderConfigInput-clientSecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** clientSecretSource **   <a name="bedrockagentcorecontrol-Type-LinkedinOauth2ProviderConfigInput-clientSecretSource"></a>
The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

## See Also
<a name="API_LinkedinOauth2ProviderConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LinkedinOauth2ProviderConfigInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LinkedinOauth2ProviderConfigInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LinkedinOauth2ProviderConfigInput) 