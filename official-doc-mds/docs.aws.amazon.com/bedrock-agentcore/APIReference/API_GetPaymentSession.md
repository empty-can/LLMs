

# GetPaymentSession
<a name="API_GetPaymentSession"></a>

Get a payment session.

## Request Syntax
<a name="API_GetPaymentSession_RequestSyntax"></a>

```
POST /payments/getPaymentSession HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "paymentManagerArn": "{{string}}",
   "paymentSessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetPaymentSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-userId"></a>
The user ID associated with this payment session.  
Length Constraints: Minimum length of 0. Maximum length of 120.

## Request Body
<a name="API_GetPaymentSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [paymentManagerArn](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** [paymentSessionId](#API_GetPaymentSession_RequestSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-request-paymentSessionId"></a>
The ID of the payment session to retrieve.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

## Response Syntax
<a name="API_GetPaymentSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "paymentSession": { 
      "availableLimits": { 
         "availableSpendAmount": { 
            "currency": "string",
            "value": "string"
         },
         "updatedAt": "string"
      },
      "createdAt": "string",
      "expiryTimeInMinutes": number,
      "limits": { 
         "maxSpendAmount": { 
            "currency": "string",
            "value": "string"
         }
      },
      "paymentManagerArn": "string",
      "paymentSessionId": "string",
      "updatedAt": "string",
      "userId": "string"
   }
}
```

## Response Elements
<a name="API_GetPaymentSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [paymentSession](#API_GetPaymentSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetPaymentSession-response-paymentSession"></a>
The payment session details.  
Type: [PaymentSession](API_PaymentSession.md) object

## Errors
<a name="API_GetPaymentSession_Errors"></a>

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
<a name="API_GetPaymentSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetPaymentSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetPaymentSession) 