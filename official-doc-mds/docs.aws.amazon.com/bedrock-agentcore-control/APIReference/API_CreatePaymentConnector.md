

# CreatePaymentConnector
<a name="API_CreatePaymentConnector"></a>

Creates a new payment connector for a payment manager. A payment connector integrates with a supported payment provider to enable payment processing capabilities.

## Request Syntax
<a name="API_CreatePaymentConnector_RequestSyntax"></a>

```
POST /payments/managers/{{paymentManagerId}}/connectors HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "credentialProviderConfigurations": [ 
      { ... }
   ],
   "description": "{{string}}",
   "name": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePaymentConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [paymentManagerId](#API_CreatePaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-request-uri-paymentManagerId"></a>
The unique identifier of the payment manager to create the connector for.  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_CreatePaymentConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [credentialProviderConfigurations](#API_CreatePaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-request-credentialProviderConfigurations"></a>
The credential provider configurations for the payment connector. These configurations specify how the connector authenticates with the payment provider.  
Type: Array of [CredentialsProviderConfiguration](API_CredentialsProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [description](#API_CreatePaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-request-description"></a>
A description of the payment connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[a-zA-Z0-9\s]+`   
Required: No

 ** [name](#API_CreatePaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-request-name"></a>
The name of the payment connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [type](#API_CreatePaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-request-type"></a>
The type of payment connector, which determines the payment provider integration.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy`   
Required: Yes

## Response Syntax
<a name="API_CreatePaymentConnector_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "credentialProviderConfigurations": [ 
      { ... }
   ],
   "name": "string",
   "paymentConnectorId": "string",
   "paymentManagerId": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_CreatePaymentConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-createdAt"></a>
The timestamp when the payment connector was created.  
Type: Timestamp

 ** [credentialProviderConfigurations](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-credentialProviderConfigurations"></a>
The credential provider configurations for the created payment connector.  
Type: Array of [CredentialsProviderConfiguration](API_CredentialsProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.

 ** [name](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-name"></a>
The name of the created payment connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [paymentConnectorId](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-paymentConnectorId"></a>
The unique identifier of the created payment connector.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [paymentManagerId](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-paymentManagerId"></a>
The unique identifier of the parent payment manager.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [status](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-status"></a>
The current status of the payment connector. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [type](#API_CreatePaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentConnector-response-type"></a>
The type of the created payment connector.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy` 

## Errors
<a name="API_CreatePaymentConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

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

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreatePaymentConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreatePaymentConnector) 