

# ListPaymentSessions
<a name="API_ListPaymentSessions"></a>

List payment sessions.

## Request Syntax
<a name="API_ListPaymentSessions_RequestSyntax"></a>

```
POST /payments/listPaymentSessions HTTP/1.1
X-Amzn-Bedrock-AgentCore-Payments-User-Id: {{userId}}
X-Amzn-Bedrock-AgentCore-Payments-Agent-Name: {{agentName}}
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "paymentManagerArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPaymentSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentName](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-agentName"></a>
The agent name associated with this request, used for observability.  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [userId](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-userId"></a>
The user ID associated with the payment sessions.  
Length Constraints: Minimum length of 0. Maximum length of 120.

## Request Body
<a name="API_ListPaymentSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-maxResults"></a>
Maximum number of results to return in a single response.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-nextToken"></a>
Token for pagination to retrieve the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [paymentManagerArn](#API_ListPaymentSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-request-paymentManagerArn"></a>
The ARN of the payment manager that owns the sessions.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

## Response Syntax
<a name="API_ListPaymentSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "paymentSessions": [ 
      { 
         "createdAt": "string",
         "expiryTimeInMinutes": number,
         "paymentManagerArn": "string",
         "paymentSessionId": "string",
         "updatedAt": "string",
         "userId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPaymentSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPaymentSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-response-nextToken"></a>
Token for pagination to retrieve the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [paymentSessions](#API_ListPaymentSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListPaymentSessions-response-paymentSessions"></a>
List of payment session summaries matching the request criteria.  
Type: Array of [PaymentSessionSummary](API_PaymentSessionSummary.md) objects

## Errors
<a name="API_ListPaymentSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_ListPaymentSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListPaymentSessions) 