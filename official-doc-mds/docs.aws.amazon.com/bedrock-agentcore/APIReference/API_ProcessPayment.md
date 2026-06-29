

# ProcessPayment
<a name="API_ProcessPayment"></a>

Processes a payment using a payment instrument within a payment session.

## Request Syntax
<a name="API_ProcessPayment_RequestSyntax"></a>

```
POST /payments/processPayment HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "clientToken": "{{string}}",
   "paymentInput": { ... },
   "paymentInstrumentId": "{{string}}",
   "paymentManagerArn": "{{string}}",
   "paymentSessionId": "{{string}}",
   "paymentType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ProcessPayment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-userId"></a>
The user ID associated with this payment.  
Length Constraints: Minimum length of 0. Maximum length of 120.

## Request Body
<a name="API_ProcessPayment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [paymentInput](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentInput"></a>
The payment input details specific to the payment type.  
Type: [PaymentInput](API_PaymentInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [paymentInstrumentId](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentInstrumentId"></a>
The ID of the payment instrument to use.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentManagerArn](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentManagerArn"></a>
The ARN of the payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** [paymentSessionId](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentSessionId"></a>
The ID of the payment session.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** [paymentType](#API_ProcessPayment_RequestSyntax) **   <a name="BedrockAgentCore-ProcessPayment-request-paymentType"></a>
The type of payment to process.  
Type: String  
Valid Values: `CRYPTO_X402`   
Required: Yes

## Response Syntax
<a name="API_ProcessPayment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "paymentInstrumentId": "string",
   "paymentManagerArn": "string",
   "paymentOutput": { ... },
   "paymentSessionId": "string",
   "paymentType": "string",
   "processPaymentId": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_ProcessPayment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-createdAt"></a>
The timestamp when the payment was created.  
Type: Timestamp

 ** [paymentInstrumentId](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentInstrumentId"></a>
The ID of the payment instrument used.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}` 

 ** [paymentManagerArn](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentManagerArn"></a>
The ARN of the payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}` 

 ** [paymentOutput](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentOutput"></a>
The payment output details specific to the payment type.  
Type: [PaymentOutput](API_PaymentOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [paymentSessionId](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentSessionId"></a>
The ID of the payment session used.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}` 

 ** [paymentType](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-paymentType"></a>
The type of payment processed.  
Type: String  
Valid Values: `CRYPTO_X402` 

 ** [processPaymentId](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-processPaymentId"></a>
The unique identifier of the processed payment.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}` 

 ** [status](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-status"></a>
The status of the payment.  
Type: String  
Valid Values: `PROOF_GENERATED` 

 ** [updatedAt](#API_ProcessPayment_ResponseSyntax) **   <a name="BedrockAgentCore-ProcessPayment-response-updatedAt"></a>
The timestamp when the payment was last updated.  
Type: Timestamp

## Errors
<a name="API_ProcessPayment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_ProcessPayment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ProcessPayment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProcessPayment) 