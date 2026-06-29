

# CustomOauth2ProviderConfigInput
<a name="API_CustomOauth2ProviderConfigInput"></a>

Input configuration for a custom OAuth2 provider.

## Contents
<a name="API_CustomOauth2ProviderConfigInput_Contents"></a>

 ** oauthDiscovery **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-oauthDiscovery"></a>
The OAuth2 discovery information for the custom provider.  
Type: [Oauth2Discovery](API_Oauth2Discovery.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** clientAuthenticationMethod **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-clientAuthenticationMethod"></a>
The client authentication method to use when authenticating with the token endpoint.  
Type: String  
Valid Values: `CLIENT_SECRET_BASIC | CLIENT_SECRET_POST | AWS_IAM_ID_TOKEN_JWT`   
Required: No

 ** clientId **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-clientId"></a>
The client ID for the custom OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** clientSecret **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-clientSecret"></a>
The client secret for the custom OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** clientSecretConfig **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-clientSecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** clientSecretSource **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-clientSecretSource"></a>
The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** onBehalfOfTokenExchangeConfig **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-onBehalfOfTokenExchangeConfig"></a>
The configuration for on-behalf-of token exchange. This enables authentication flows that use RFC 8693 token exchange or RFC 7523 JWT authorization grants.  
Type: [OnBehalfOfTokenExchangeConfigType](API_OnBehalfOfTokenExchangeConfigType.md) object  
Required: No

 ** privateEndpoint **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-privateEndpoint"></a>
The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** privateEndpointOverrides **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigInput-privateEndpointOverrides"></a>
The private endpoint overrides for the custom OAuth2 provider configuration.  
Type: Array of [PrivateEndpointOverride](API_PrivateEndpointOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_CustomOauth2ProviderConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomOauth2ProviderConfigInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomOauth2ProviderConfigInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomOauth2ProviderConfigInput) 