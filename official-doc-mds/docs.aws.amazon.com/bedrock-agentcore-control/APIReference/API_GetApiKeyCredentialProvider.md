

# GetApiKeyCredentialProvider
<a name="API_GetApiKeyCredentialProvider"></a>

Retrieves information about an API key credential provider.

## Request Syntax
<a name="API_GetApiKeyCredentialProvider_RequestSyntax"></a>

```
POST /identities/GetApiKeyCredentialProvider HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetApiKeyCredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetApiKeyCredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_GetApiKeyCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-request-name"></a>
The name of the API key credential provider to retrieve.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

## Response Syntax
<a name="API_GetApiKeyCredentialProvider_ResponseSyntax"></a>

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
<a name="API_GetApiKeyCredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeySecretArn](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-apiKeySecretArn"></a>
The Amazon Resource Name (ARN) of the API key secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object

 ** [apiKeySecretJsonKey](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-apiKeySecretJsonKey"></a>
The JSON key used to extract the API key value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [apiKeySecretSource](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-apiKeySecretSource"></a>
The source type of the API key secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL` 

 ** [createdTime](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-createdTime"></a>
The timestamp when the API key credential provider was created.  
Type: Timestamp

 ** [credentialProviderArn](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the API key credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+` 

 ** [lastUpdatedTime](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-lastUpdatedTime"></a>
The timestamp when the API key credential provider was last updated.  
Type: Timestamp

 ** [name](#API_GetApiKeyCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetApiKeyCredentialProvider-response-name"></a>
The name of the API key credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

## Errors
<a name="API_GetApiKeyCredentialProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** DecryptionFailure **   
Exception thrown when decryption of a secret fails.  
HTTP Status Code: 400

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

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
<a name="API_GetApiKeyCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetApiKeyCredentialProvider) 