

# GetPaymentCredentialProvider
<a name="API_GetPaymentCredentialProvider"></a>

Retrieves information about a specific payment credential provider.

## Request Syntax
<a name="API_GetPaymentCredentialProvider_RequestSyntax"></a>

```
POST /identities/GetPaymentCredentialProvider HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetPaymentCredentialProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPaymentCredentialProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_GetPaymentCredentialProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-request-name"></a>
The name of the payment credential provider to retrieve.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

## Response Syntax
<a name="API_GetPaymentCredentialProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdTime": number,
   "credentialProviderArn": "string",
   "credentialProviderVendor": "string",
   "lastUpdatedTime": number,
   "name": "string",
   "providerConfigurationOutput": { ... },
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_GetPaymentCredentialProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTime](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-createdTime"></a>
The timestamp when the payment credential provider was created.  
Type: Timestamp

 ** [credentialProviderArn](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the payment credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/paymentcredentialprovider/[a-zA-Z0-9-.]+` 

 ** [credentialProviderVendor](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-credentialProviderVendor"></a>
The vendor type for the payment credential provider.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy` 

 ** [lastUpdatedTime](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-lastUpdatedTime"></a>
The timestamp when the payment credential provider was last updated.  
Type: Timestamp

 ** [name](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-name"></a>
The name of the payment credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+` 

 ** [providerConfigurationOutput](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-providerConfigurationOutput"></a>
Output configuration (contains secret ARNs, excludes actual secret values).  
Type: [PaymentProviderConfigurationOutput](API_PaymentProviderConfigurationOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [tags](#API_GetPaymentCredentialProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentCredentialProvider-response-tags"></a>
The tags associated with the payment credential provider.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

## Errors
<a name="API_GetPaymentCredentialProvider_Errors"></a>

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
<a name="API_GetPaymentCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetPaymentCredentialProvider) 