

# OAuthCredentialProvider
<a name="API_OAuthCredentialProvider"></a>

An OAuth credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint using OAuth.

## Contents
<a name="API_OAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="bedrockagentcorecontrol-Type-OAuthCredentialProvider-providerArn"></a>
The Amazon Resource Name (ARN) of the OAuth credential provider. This ARN identifies the provider in AWS.  
Type: String  
Pattern: `arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)`   
Required: Yes

 ** scopes **   <a name="bedrockagentcorecontrol-Type-OAuthCredentialProvider-scopes"></a>
The OAuth scopes for the credential provider. These scopes define the level of access requested from the OAuth provider.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** customParameters **   <a name="bedrockagentcorecontrol-Type-OAuthCredentialProvider-customParameters"></a>
The custom parameters for the OAuth credential provider. These parameters provide additional configuration for the OAuth authentication process.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Value Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** defaultReturnUrl **   <a name="bedrockagentcorecontrol-Type-OAuthCredentialProvider-defaultReturnUrl"></a>
The URL where the end user's browser is redirected after obtaining the authorization code. Generally points to the customer's application.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\w+:(\/?\/?)[^\s]+`   
Required: No

 ** grantType **   <a name="bedrockagentcorecontrol-Type-OAuthCredentialProvider-grantType"></a>
Specifies the kind of credentials to use for authorization:  
+  `CLIENT_CREDENTIALS` - Authorization with a client ID and secret.
+  `AUTHORIZATION_CODE` - Authorization with a token that is specific to an individual end user.
+  `TOKEN_EXCHANGE` - Authorization using on-behalf-of token exchange. An inbound user token is exchanged for a downstream access token scoped to the target audience.
Type: String  
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | TOKEN_EXCHANGE`   
Required: No

## See Also
<a name="API_OAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OAuthCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OAuthCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OAuthCredentialProvider) 