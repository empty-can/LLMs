

# UpdatePaymentCredentialProvider
<a name="API_UpdatePaymentCredentialProvider"></a>

Updates an existing payment credential provider with new authentication credentials.

## Request Syntax
<a name="API_UpdatePaymentCredentialProvider_RequestSyntax"></a>

```
POST /identities/UpdatePaymentCredentialProvider HTTP/1.1
Content-type: application/json

{
   "credentialProviderVendor": "{{string}}",
   "name": "{{string}}",
   "providerConfigurationInput": { ... }
}
```

## URI Request Parameters
<a name="API_UpdatePaymentCredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePaymentCredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [credentialProviderVendor](#API_UpdatePaymentCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-request-credentialProviderVendor"></a>
The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy`   
Required: Yes

 ** [name](#API_UpdatePaymentCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-request-name"></a>
The name of the payment credential provider to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** [providerConfigurationInput](#API_UpdatePaymentCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-request-providerConfigurationInput"></a>
Configuration specific to the vendor, including API credentials.  
Type: [PaymentProviderConfigurationInput](API_PaymentProviderConfigurationInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_UpdatePaymentCredentialProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdTime": number,
   "credentialProviderArn": "string",
   "credentialProviderVendor": "string",
   "lastUpdatedTime": number,
   "name": "string",
   "providerConfigurationOutput": { ... }
}
```

## Response Elements
<a name="API_UpdatePaymentCredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTime](#API_UpdatePaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-response-createdTime"></a>
The timestamp when the payment credential provider was created.  
Type: Timestamp

 ** [credentialProviderArn](#API_UpdatePaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the updated payment credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/paymentcredentialprovider/[a-zA-Z0-9-.]+` 

 ** [credentialProviderVendor](#API_UpdatePaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-response-credentialProviderVendor"></a>
The vendor type for the updated payment credential provider.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy` 

 ** [lastUpdatedTime](#API_UpdatePaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-response-lastUpdatedTime"></a>
The timestamp when the payment credential provider was last updated.  
Type: Timestamp

 ** [name](#API_UpdatePaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-response-name"></a>
The name of the updated payment credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

 ** [providerConfigurationOutput](#API_UpdatePaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentCredentialProvider-response-providerConfigurationOutput"></a>
Output configuration (contains secret ARNs, excludes actual secret values).  
Type: [PaymentProviderConfigurationOutput](API_PaymentProviderConfigurationOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_UpdatePaymentCredentialProvider_Errors"></a>

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
<a name="API_UpdatePaymentCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatePaymentCredentialProvider) 