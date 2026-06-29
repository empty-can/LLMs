

# GetPaymentConnector
<a name="API_GetPaymentConnector"></a>

Retrieves information about a specific payment connector.

## Request Syntax
<a name="API_GetPaymentConnector_RequestSyntax"></a>

```
GET /payments/managers/{{paymentManagerId}}/connectors/{{paymentConnectorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPaymentConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [paymentConnectorId](#API_GetPaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-request-uri-paymentConnectorId"></a>
The unique identifier of the payment connector to retrieve.  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [paymentManagerId](#API_GetPaymentConnector_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-request-uri-paymentManagerId"></a>
The unique identifier of the parent payment manager.  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_GetPaymentConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPaymentConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "credentialProviderConfigurations": [ 
      { ... }
   ],
   "description": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "paymentConnectorId": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_GetPaymentConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-createdAt"></a>
The timestamp when the payment connector was created.  
Type: Timestamp

 ** [credentialProviderConfigurations](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-credentialProviderConfigurations"></a>
The credential provider configurations for the payment connector.  
Type: Array of [CredentialsProviderConfiguration](API_CredentialsProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.

 ** [description](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-description"></a>
The description of the payment connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[a-zA-Z0-9\s]+` 

 ** [lastUpdatedAt](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-lastUpdatedAt"></a>
The timestamp when the payment connector was last updated.  
Type: Timestamp

 ** [name](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-name"></a>
The name of the payment connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [paymentConnectorId](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-paymentConnectorId"></a>
The unique identifier of the payment connector.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [status](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-status"></a>
The current status of the payment connector. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [type](#API_GetPaymentConnector_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentConnector-response-type"></a>
The type of the payment connector, which determines the payment provider integration.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy` 

## Errors
<a name="API_GetPaymentConnector_Errors"></a>

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

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetPaymentConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetPaymentConnector) 