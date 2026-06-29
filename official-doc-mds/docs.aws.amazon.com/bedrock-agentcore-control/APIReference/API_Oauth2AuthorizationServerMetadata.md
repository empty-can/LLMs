

# Oauth2AuthorizationServerMetadata
<a name="API_Oauth2AuthorizationServerMetadata"></a>

Contains the authorization server metadata for an OAuth2 provider.

## Contents
<a name="API_Oauth2AuthorizationServerMetadata_Contents"></a>

 ** authorizationEndpoint **   <a name="bedrockagentcorecontrol-Type-Oauth2AuthorizationServerMetadata-authorizationEndpoint"></a>
The authorization endpoint URL for the OAuth2 authorization server.  
Type: String  
Required: Yes

 ** issuer **   <a name="bedrockagentcorecontrol-Type-Oauth2AuthorizationServerMetadata-issuer"></a>
The issuer URL for the OAuth2 authorization server.  
Type: String  
Required: Yes

 ** tokenEndpoint **   <a name="bedrockagentcorecontrol-Type-Oauth2AuthorizationServerMetadata-tokenEndpoint"></a>
The token endpoint URL for the OAuth2 authorization server.  
Type: String  
Required: Yes

 ** responseTypes **   <a name="bedrockagentcorecontrol-Type-Oauth2AuthorizationServerMetadata-responseTypes"></a>
The supported response types for the OAuth2 authorization server.  
Type: Array of strings  
Required: No

 ** tokenEndpointAuthMethods **   <a name="bedrockagentcorecontrol-Type-Oauth2AuthorizationServerMetadata-tokenEndpointAuthMethods"></a>
The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Pattern: `(client_secret_post|client_secret_basic)`   
Required: No

## See Also
<a name="API_Oauth2AuthorizationServerMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Oauth2AuthorizationServerMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Oauth2AuthorizationServerMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Oauth2AuthorizationServerMetadata) 