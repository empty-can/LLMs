

# CreateOauth2CredentialProvider
<a name="API_CreateOauth2CredentialProvider"></a>

Creates a new OAuth2 credential provider.

## Request Syntax
<a name="API_CreateOauth2CredentialProvider_RequestSyntax"></a>

```
POST /identities/CreateOauth2CredentialProvider HTTP/1.1
Content-type: application/json

{
   "credentialProviderVendor": "{{string}}",
   "name": "{{string}}",
   "oauth2ProviderConfigInput": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateOauth2CredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOauth2CredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [credentialProviderVendor](#API_CreateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-request-credentialProviderVendor"></a>
The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.  
Type: String  
Valid Values: `GoogleOauth2 | GithubOauth2 | SlackOauth2 | SalesforceOauth2 | MicrosoftOauth2 | CustomOauth2 | AtlassianOauth2 | LinkedinOauth2 | XOauth2 | OktaOauth2 | OneLoginOauth2 | PingOneOauth2 | FacebookOauth2 | YandexOauth2 | RedditOauth2 | ZoomOauth2 | TwitchOauth2 | SpotifyOauth2 | DropboxOauth2 | NotionOauth2 | HubspotOauth2 | CyberArkOauth2 | FusionAuthOauth2 | Auth0Oauth2 | CognitoOauth2`   
Required: Yes

 ** [name](#API_CreateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-request-name"></a>
The name of the OAuth2 credential provider. The name must be unique within your account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [oauth2ProviderConfigInput](#API_CreateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-request-oauth2ProviderConfigInput"></a>
The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.  
Type: [Oauth2ProviderConfigInput](API_Oauth2ProviderConfigInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_CreateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-request-tags"></a>
A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateOauth2CredentialProvider_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "callbackUrl": "string",
   "clientSecretArn": { 
      "secretArn": "string"
   },
   "clientSecretJsonKey": "string",
   "clientSecretSource": "string",
   "credentialProviderArn": "string",
   "name": "string",
   "oauth2ProviderConfigOutput": { ... },
   "status": "string"
}
```

## Response Elements
<a name="API_CreateOauth2CredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [callbackUrl](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-callbackUrl"></a>
Callback URL to register on the OAuth2 credential provider as an allowed callback URL. This URL is where the OAuth2 authorization server redirects users after they complete the authorization flow.  
Type: String

 ** [clientSecretArn](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-clientSecretArn"></a>
The Amazon Resource Name (ARN) of the client secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object

 ** [clientSecretJsonKey](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-clientSecretJsonKey"></a>
The JSON key used to extract the client secret value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [clientSecretSource](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-clientSecretSource"></a>
The source type of the client secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL` 

 ** [credentialProviderArn](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the OAuth2 credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/oauth2credentialprovider/[a-zA-Z0-9-.]+` 

 ** [name](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-name"></a>
The name of the OAuth2 credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

 ** [oauth2ProviderConfigOutput](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-oauth2ProviderConfigOutput"></a>
Contains the output configuration for an OAuth2 provider.  
Type: [Oauth2ProviderConfigOutput](API_Oauth2ProviderConfigOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_CreateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOauth2CredentialProvider-response-status"></a>
The current status of the OAuth2 credential provider.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED` 

## Errors
<a name="API_CreateOauth2CredentialProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** DecryptionFailure **   
Exception thrown when decryption of a secret fails.  
HTTP Status Code: 400

 ** EncryptionFailure **   
Exception thrown when encryption of a secret fails.  
HTTP Status Code: 400

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceLimitExceededException **   
Exception thrown when a resource limit is exceeded.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateOauth2CredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider) 