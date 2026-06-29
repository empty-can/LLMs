

# GetResourceOauth2Token
<a name="API_GetResourceOauth2Token"></a>

Returns the OAuth 2.0 token of the provided resource.

## Request Syntax
<a name="API_GetResourceOauth2Token_RequestSyntax"></a>

```
POST /identities/oauth2/token HTTP/1.1
Content-type: application/json

{
   "audiences": [ "{{string}}" ],
   "customParameters": { 
      "{{string}}" : "{{string}}" 
   },
   "customState": "{{string}}",
   "forceAuthentication": {{boolean}},
   "oauth2Flow": "{{string}}",
   "resourceCredentialProviderName": "{{string}}",
   "resourceOauth2ReturnUrl": "{{string}}",
   "resources": [ "{{string}}" ],
   "scopes": [ "{{string}}" ],
   "sessionUri": "{{string}}",
   "workloadIdentityToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetResourceOauth2Token_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourceOauth2Token_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audiences](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-audiences"></a>
The audiences to include in the token request. These are used to specify the intended recipients of the OAuth2 token.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [customParameters](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-customParameters"></a>
A map of custom parameters to include in the authorization request to the resource credential provider. These parameters are in addition to the standard OAuth 2.0 flow parameters, and will not override them.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Key Pattern: `[a-zA-Z0-9\-_\.]+`   
Value Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [customState](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-customState"></a>
An opaque string that will be sent back to the callback URL provided in resourceOauth2ReturnUrl. This state should be used to protect the callback URL of your application against CSRF attacks by ensuring the response corresponds to the original request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [forceAuthentication](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-forceAuthentication"></a>
Indicates whether to always initiate a new three-legged OAuth (3LO) flow, regardless of any existing session.  
Type: Boolean  
Required: No

 ** [oauth2Flow](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-oauth2Flow"></a>
The type of flow to be performed.  
Type: String  
Valid Values: `USER_FEDERATION | M2M | ON_BEHALF_OF_TOKEN_EXCHANGE`   
Required: Yes

 ** [resourceCredentialProviderName](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-resourceCredentialProviderName"></a>
The name of the resource's credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [resourceOauth2ReturnUrl](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-resourceOauth2ReturnUrl"></a>
The callback URL to redirect to after the OAuth 2.0 token retrieval is complete. This URL must be one of the provided URLs configured for the workload identity.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\w+:(\/?\/?)[^\s]+`   
Required: No

 ** [resources](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-resources"></a>
The resources to include in the token request. These are used to specify the target resources for which the OAuth2 token is being requested.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [scopes](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-scopes"></a>
The OAuth scopes being requested.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [sessionUri](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-sessionUri"></a>
Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `urn:ietf:params:oauth:request_uri:[a-zA-Z0-9-._~]+`   
Required: No

 ** [workloadIdentityToken](#API_GetResourceOauth2Token_RequestSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-request-workloadIdentityToken"></a>
The identity token of the workload from which you want to retrieve the OAuth2 token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Required: Yes

## Response Syntax
<a name="API_GetResourceOauth2Token_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessToken": "string",
   "authorizationUrl": "string",
   "sessionStatus": "string",
   "sessionUri": "string"
}
```

## Response Elements
<a name="API_GetResourceOauth2Token_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessToken](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-accessToken"></a>
The OAuth 2.0 access token to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.

 ** [authorizationUrl](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-authorizationUrl"></a>
The URL to initiate the authorization process, provided when the access token requires user authorization.  
Type: String  
Length Constraints: Minimum length of 1.

 ** [sessionStatus](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-sessionStatus"></a>
Status indicating whether the user's authorization session is in progress or has failed. This helps determine the next steps in the OAuth2 authentication flow.  
Type: String  
Valid Values: `IN_PROGRESS | FAILED` 

 ** [sessionUri](#API_GetResourceOauth2Token_ResponseSyntax) **   <a name="BedrockAgentCore-GetResourceOauth2Token-response-sessionUri"></a>
Unique identifier for the user's authorization session for retrieving OAuth2 tokens. This matches the sessionId from the request and can be used to track the session state.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `urn:ietf:params:oauth:request_uri:[a-zA-Z0-9-._~]+` 

## Errors
<a name="API_GetResourceOauth2Token_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_GetResourceOauth2Token_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetResourceOauth2Token) 