

# CreateApiKeyCredentialProvider
<a name="API_CreateApiKeyCredentialProvider"></a>

Creates a new API key credential provider.

## Request Syntax
<a name="API_CreateApiKeyCredentialProvider_RequestSyntax"></a>

```
POST /identities/CreateApiKeyCredentialProvider HTTP/1.1
Content-type: application/json

{
   "apiKey": "{{string}}",
   "apiKeySecretConfig": { 
      "jsonKey": "{{string}}",
      "secretId": "{{string}}"
   },
   "apiKeySecretSource": "{{string}}",
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateApiKeyCredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApiKeyCredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiKey](#API_CreateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-request-apiKey"></a>
The API key to use for authentication. This value is encrypted and stored securely.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 65536.  
Required: No

 ** [apiKeySecretConfig](#API_CreateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-request-apiKeySecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when `apiKeySecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** [apiKeySecretSource](#API_CreateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-request-apiKeySecretSource"></a>
The source type of the API key secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** [name](#API_CreateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-request-name"></a>
The name of the API key credential provider. The name must be unique within your account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [tags](#API_CreateApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-request-tags"></a>
A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateApiKeyCredentialProvider_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "apiKeySecretArn": { 
      "secretArn": "string"
   },
   "apiKeySecretJsonKey": "string",
   "apiKeySecretSource": "string",
   "credentialProviderArn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateApiKeyCredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [apiKeySecretArn](#API_CreateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-response-apiKeySecretArn"></a>
The Amazon Resource Name (ARN) of the secret containing the API key.  
Type: [Secret](API_Secret.md) object

 ** [apiKeySecretJsonKey](#API_CreateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-response-apiKeySecretJsonKey"></a>
The JSON key used to extract the API key value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [apiKeySecretSource](#API_CreateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-response-apiKeySecretSource"></a>
The source type of the API key secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL` 

 ** [credentialProviderArn](#API_CreateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the created API key credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+` 

 ** [name](#API_CreateApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateApiKeyCredentialProvider-response-name"></a>
The name of the created API key credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

## Errors
<a name="API_CreateApiKeyCredentialProvider_Errors"></a>

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
<a name="API_CreateApiKeyCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider) 