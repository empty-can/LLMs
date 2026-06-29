

# ListPaymentCredentialProviders
<a name="API_ListPaymentCredentialProviders"></a>

Lists all payment credential providers in the account.

## Request Syntax
<a name="API_ListPaymentCredentialProviders_RequestSyntax"></a>

```
POST /identities/ListPaymentCredentialProviders HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPaymentCredentialProviders_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPaymentCredentialProviders_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPaymentCredentialProviders_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPaymentCredentialProviders-request-maxResults"></a>
Maximum number of results to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 20.  
Required: No

 ** [nextToken](#API_ListPaymentCredentialProviders_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPaymentCredentialProviders-request-nextToken"></a>
Pagination token.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListPaymentCredentialProviders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "credentialProviders": [ 
      { 
         "createdTime": number,
         "credentialProviderArn": "string",
         "credentialProviderVendor": "string",
         "lastUpdatedTime": number,
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPaymentCredentialProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentialProviders](#API_ListPaymentCredentialProviders_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPaymentCredentialProviders-response-credentialProviders"></a>
The list of payment credential providers.  
Type: Array of [PaymentCredentialProviderItem](API_PaymentCredentialProviderItem.md) objects

 ** [nextToken](#API_ListPaymentCredentialProviders_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPaymentCredentialProviders-response-nextToken"></a>
Pagination token for the next page of results.  
Type: String

## Errors
<a name="API_ListPaymentCredentialProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

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
<a name="API_ListPaymentCredentialProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListPaymentCredentialProviders) 