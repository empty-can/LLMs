

# OAuthCredentialProvider
<a name="API_OAuthCredentialProvider"></a>

Configuration for an OAuth 2.0 credential provider used to authenticate tool calls.

## Contents
<a name="API_OAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-providerArn"></a>
The ARN of the OAuth 2.0 credential provider in AgentCore Identity.  
Type: String  
Pattern: `arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)`   
Required: Yes

 ** scopes **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-scopes"></a>
The OAuth 2.0 scopes to request when obtaining an access token.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** customParameters **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-customParameters"></a>
Additional custom parameters to include in the OAuth 2.0 token request.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Value Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** defaultReturnUrl **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-defaultReturnUrl"></a>
The default return URL for the OAuth 2.0 authorization flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\w+:(\/?\/?)[^\s]+`   
Required: No

 ** grantType **   <a name="BedrockAgentCore-Type-OAuthCredentialProvider-grantType"></a>
The OAuth 2.0 grant type to use for authentication.  
Type: String  
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | TOKEN_EXCHANGE`   
Required: No

## See Also
<a name="API_OAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OAuthCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OAuthCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OAuthCredentialProvider) 