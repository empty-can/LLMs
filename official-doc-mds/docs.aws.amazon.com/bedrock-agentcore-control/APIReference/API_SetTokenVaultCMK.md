

# SetTokenVaultCMK
<a name="API_SetTokenVaultCMK"></a>

Sets the customer master key (CMK) for a token vault.

## Request Syntax
<a name="API_SetTokenVaultCMK_RequestSyntax"></a>

```
POST /identities/set-token-vault-cmk HTTP/1.1
Content-type: application/json

{
   "kmsConfiguration": { 
      "keyType": "{{string}}",
      "kmsKeyArn": "{{string}}"
   },
   "tokenVaultId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SetTokenVaultCMK_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SetTokenVaultCMK_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [kmsConfiguration](#API_SetTokenVaultCMK_RequestSyntax) **   <a name="bedrockagentcorecontrol-SetTokenVaultCMK-request-kmsConfiguration"></a>
The AWS KMS configuration for the token vault, including the key type and AWS KMS key ARN.  
Type: [KmsConfiguration](API_KmsConfiguration.md) object  
Required: Yes

 ** [tokenVaultId](#API_SetTokenVaultCMK_RequestSyntax) **   <a name="bedrockagentcorecontrol-SetTokenVaultCMK-request-tokenVaultId"></a>
The unique identifier of the token vault to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: No

## Response Syntax
<a name="API_SetTokenVaultCMK_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kmsConfiguration": { 
      "keyType": "string",
      "kmsKeyArn": "string"
   },
   "lastModifiedDate": number,
   "tokenVaultId": "string"
}
```

## Response Elements
<a name="API_SetTokenVaultCMK_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsConfiguration](#API_SetTokenVaultCMK_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SetTokenVaultCMK-response-kmsConfiguration"></a>
The KMS configuration for the token vault.  
Type: [KmsConfiguration](API_KmsConfiguration.md) object

 ** [lastModifiedDate](#API_SetTokenVaultCMK_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SetTokenVaultCMK-response-lastModifiedDate"></a>
The timestamp when the token vault was last modified.  
Type: Timestamp

 ** [tokenVaultId](#API_SetTokenVaultCMK_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SetTokenVaultCMK-response-tokenVaultId"></a>
The ID of the token vault.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9\-_]+` 

## Errors
<a name="API_SetTokenVaultCMK_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConcurrentModificationException **   
Exception thrown when a resource is modified concurrently by multiple requests.  
HTTP Status Code: 409

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
<a name="API_SetTokenVaultCMK_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SetTokenVaultCMK) 