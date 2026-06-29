

# DeletePaymentManager
<a name="API_DeletePaymentManager"></a>

Deletes a payment manager. All payment connectors associated with the payment manager must be deleted before the payment manager can be deleted. This operation initiates the deletion process asynchronously.

## Request Syntax
<a name="API_DeletePaymentManager_RequestSyntax"></a>

```
DELETE /payments/managers/{{paymentManagerId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePaymentManager_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeletePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeletePaymentManager-request-uri-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}` 

 ** [paymentManagerId](#API_DeletePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeletePaymentManager-request-uri-paymentManagerId"></a>
The unique identifier of the payment manager to delete.  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_DeletePaymentManager_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePaymentManager_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "paymentManagerId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeletePaymentManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [paymentManagerId](#API_DeletePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePaymentManager-response-paymentManagerId"></a>
The unique identifier of the deleted payment manager.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [status](#API_DeletePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePaymentManager-response-status"></a>
The current status of the payment manager, set to `DELETING` when deletion is initiated. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

## Errors
<a name="API_DeletePaymentManager_Errors"></a>

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

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

## See Also
<a name="API_DeletePaymentManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeletePaymentManager) 