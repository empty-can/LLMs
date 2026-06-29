

# UpdateApiKeyCredentialProvider
<a name="API_UpdateApiKeyCredentialProvider"></a>

Updates an existing API key credential provider.

## Request Syntax
<a name="API_UpdateApiKeyCredentialProvider_RequestSyntax"></a>

```
POST /identities/UpdateApiKeyCredentialProvider HTTP/1.1
Content-type: application/json

{
   "apiKey": "{{string}}",
   "apiKeySecretConfig": { 
      "jsonKey": "{{string}}",
      "secretId": "{{string}}"
   },
   "apiKeySecretSource": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApiKeyCredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateApiKeyCredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiKey](#API_UpdateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-request-apiKey"></a>
The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 65536.  
Required: No

 ** [apiKeySecretConfig](#API_UpdateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-request-apiKeySecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when `apiKeySecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** [apiKeySecretSource](#API_UpdateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-request-apiKeySecretSource"></a>
The source type of the API key secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** [name](#API_UpdateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-request-name"></a>
The name of the API key credential provider to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

## Response Syntax
<a name="API_UpdateApiKeyCredentialProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiKeySecretArn": { 
      "secretArn": "string"
   },
   "apiKeySecretJsonKey": "string",
   "apiKeySecretSource": "string",
   "createdTime": number,
   "credentialProviderArn": "string",
   "lastUpdatedTime": number,
   "name": "string"
}
```

## Response Elements
<a name="API_UpdateApiKeyCredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeySecretArn](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-apiKeySecretArn"></a>
The Amazon Resource Name (ARN) of the API key secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object

 ** [apiKeySecretJsonKey](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-apiKeySecretJsonKey"></a>
The JSON key used to extract the API key value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [apiKeySecretSource](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-apiKeySecretSource"></a>
The source type of the API key secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL` 

 ** [createdTime](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-createdTime"></a>
The timestamp when the API key credential provider was created.  
Type: Timestamp

 ** [credentialProviderArn](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the API key credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+` 

 ** [lastUpdatedTime](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-lastUpdatedTime"></a>
The timestamp when the API key credential provider was last updated.  
Type: Timestamp

 ** [name](#API_UpdateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateApiKeyCredentialProvider-response-name"></a>
The name of the API key credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

## Errors
<a name="API_UpdateApiKeyCredentialProvider_Errors"></a>

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
<a name="API_UpdateApiKeyCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateApiKeyCredentialProvider) 