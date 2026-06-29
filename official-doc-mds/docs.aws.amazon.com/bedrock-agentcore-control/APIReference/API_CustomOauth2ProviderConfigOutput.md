

# CustomOauth2ProviderConfigOutput
<a name="API_CustomOauth2ProviderConfigOutput"></a>

Output configuration for a custom OAuth2 provider.

## Contents
<a name="API_CustomOauth2ProviderConfigOutput_Contents"></a>

 ** oauthDiscovery **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigOutput-oauthDiscovery"></a>
The OAuth2 discovery information for the custom provider.  
Type: [Oauth2Discovery](API_Oauth2Discovery.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** clientAuthenticationMethod **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigOutput-clientAuthenticationMethod"></a>
The client authentication method used when authenticating with the token endpoint.  
Type: String  
Valid Values: `CLIENT_SECRET_BASIC | CLIENT_SECRET_POST | AWS_IAM_ID_TOKEN_JWT`   
Required: No

 ** clientId **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigOutput-clientId"></a>
The client ID for the custom OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** onBehalfOfTokenExchangeConfig **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigOutput-onBehalfOfTokenExchangeConfig"></a>
The configuration for on-behalf-of token exchange.  
Type: [OnBehalfOfTokenExchangeConfigType](API_OnBehalfOfTokenExchangeConfigType.md) object  
Required: No

 ** privateEndpoint **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigOutput-privateEndpoint"></a>
The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** privateEndpointOverrides **   <a name="bedrockagentcorecontrol-Type-CustomOauth2ProviderConfigOutput-privateEndpointOverrides"></a>
The private endpoint overrides for the custom OAuth2 provider configuration.  
Type: Array of [PrivateEndpointOverride](API_PrivateEndpointOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_CustomOauth2ProviderConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomOauth2ProviderConfigOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomOauth2ProviderConfigOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomOauth2ProviderConfigOutput) 