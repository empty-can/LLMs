

# UpdateOauth2CredentialProvider
<a name="API_UpdateOauth2CredentialProvider"></a>

Updates an existing OAuth2 credential provider.

## Request Syntax
<a name="API_UpdateOauth2CredentialProvider_RequestSyntax"></a>

```
POST /identities/UpdateOauth2CredentialProvider HTTP/1.1
Content-type: application/json

{
   "credentialProviderVendor": "{{string}}",
   "name": "{{string}}",
   "oauth2ProviderConfigInput": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateOauth2CredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateOauth2CredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [credentialProviderVendor](#API_UpdateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-request-credentialProviderVendor"></a>
The vendor of the OAuth2 credential provider.  
Type: String  
Valid Values: `GoogleOauth2 | GithubOauth2 | SlackOauth2 | SalesforceOauth2 | MicrosoftOauth2 | CustomOauth2 | AtlassianOauth2 | LinkedinOauth2 | XOauth2 | OktaOauth2 | OneLoginOauth2 | PingOneOauth2 | FacebookOauth2 | YandexOauth2 | RedditOauth2 | ZoomOauth2 | TwitchOauth2 | SpotifyOauth2 | DropboxOauth2 | NotionOauth2 | HubspotOauth2 | CyberArkOauth2 | FusionAuthOauth2 | Auth0Oauth2 | CognitoOauth2`   
Required: Yes

 ** [name](#API_UpdateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-request-name"></a>
The name of the OAuth2 credential provider to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [oauth2ProviderConfigInput](#API_UpdateOauth2CredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-request-oauth2ProviderConfigInput"></a>
The configuration input for the OAuth2 provider.  
Type: [Oauth2ProviderConfigInput](API_Oauth2ProviderConfigInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_UpdateOauth2CredentialProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "callbackUrl": "string",
   "clientSecretArn": { 
      "secretArn": "string"
   },
   "clientSecretJsonKey": "string",
   "clientSecretSource": "string",
   "createdTime": number,
   "credentialProviderArn": "string",
   "credentialProviderVendor": "string",
   "lastUpdatedTime": number,
   "name": "string",
   "oauth2ProviderConfigOutput": { ... },
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateOauth2CredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [callbackUrl](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-callbackUrl"></a>
Callback URL to register on the OAuth2 credential provider as an allowed callback URL. This URL is where the OAuth2 authorization server redirects users after they complete the authorization flow.  
Type: String

 ** [clientSecretArn](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-clientSecretArn"></a>
The Amazon Resource Name (ARN) of the client secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object

 ** [clientSecretJsonKey](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-clientSecretJsonKey"></a>
The JSON key used to extract the client secret value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [clientSecretSource](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-clientSecretSource"></a>
The source type of the client secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL` 

 ** [createdTime](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-createdTime"></a>
The timestamp when the OAuth2 credential provider was created.  
Type: Timestamp

 ** [credentialProviderArn](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the OAuth2 credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/oauth2credentialprovider/[a-zA-Z0-9-.]+` 

 ** [credentialProviderVendor](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-credentialProviderVendor"></a>
The vendor of the OAuth2 credential provider.  
Type: String  
Valid Values: `GoogleOauth2 | GithubOauth2 | SlackOauth2 | SalesforceOauth2 | MicrosoftOauth2 | CustomOauth2 | AtlassianOauth2 | LinkedinOauth2 | XOauth2 | OktaOauth2 | OneLoginOauth2 | PingOneOauth2 | FacebookOauth2 | YandexOauth2 | RedditOauth2 | ZoomOauth2 | TwitchOauth2 | SpotifyOauth2 | DropboxOauth2 | NotionOauth2 | HubspotOauth2 | CyberArkOauth2 | FusionAuthOauth2 | Auth0Oauth2 | CognitoOauth2` 

 ** [lastUpdatedTime](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-lastUpdatedTime"></a>
The timestamp when the OAuth2 credential provider was last updated.  
Type: Timestamp

 ** [name](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-name"></a>
The name of the OAuth2 credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

 ** [oauth2ProviderConfigOutput](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-oauth2ProviderConfigOutput"></a>
The configuration output for the OAuth2 provider.  
Type: [Oauth2ProviderConfigOutput](API_Oauth2ProviderConfigOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_UpdateOauth2CredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOauth2CredentialProvider-response-status"></a>
The current status of the updated OAuth2 credential provider.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED` 

## Errors
<a name="API_UpdateOauth2CredentialProvider_Errors"></a>

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
<a name="API_UpdateOauth2CredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateOauth2CredentialProvider) 