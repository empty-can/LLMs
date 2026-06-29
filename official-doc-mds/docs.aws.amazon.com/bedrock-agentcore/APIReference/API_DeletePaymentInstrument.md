

# DeletePaymentInstrument
<a name="API_DeletePaymentInstrument"></a>

Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.

## Request Syntax
<a name="API_DeletePaymentInstrument_RequestSyntax"></a>

```
POST /payments/deletePaymentInstrument HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
Content-type: application/json

{
   "paymentConnectorId": "{{string}}",
   "paymentInstrumentId": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeletePaymentInstrument_RequestParameters"></a>

The request uses the following URI parameters.

 ** [userId](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-userId"></a>
The user ID making the delete request. Must match the instrument's userId.  
Length Constraints: Minimum length of 0. Maximum length of 120.

## Request Body
<a name="API_DeletePaymentInstrument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentConnectorId](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-paymentConnectorId"></a>
The payment connector ID. Must match the instrument's paymentConnectorId.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [paymentInstrumentId](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-paymentInstrumentId"></a>
The payment instrument ID to delete.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentManagerArn](#API_DeletePaymentInstrument_RequestSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-request-paymentManagerArn"></a>
The payment manager ARN. Must match the instrument's paymentManagerArn.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

## Response Syntax
<a name="API_DeletePaymentInstrument_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_DeletePaymentInstrument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeletePaymentInstrument_ResponseSyntax) **   <a name="BedrockAgentCore-DeletePaymentInstrument-response-status"></a>
The status of the instrument after deletion. Always DELETED for successful soft delete.  
Type: String  
Valid Values: `INITIATED | ACTIVE | FAILED | DELETED` 

## Errors
<a name="API_DeletePaymentInstrument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_DeletePaymentInstrument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeletePaymentInstrument) 