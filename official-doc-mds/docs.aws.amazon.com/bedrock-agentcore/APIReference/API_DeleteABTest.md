

# DeleteABTest
<a name="API_DeleteABTest"></a>

Deletes an A/B test and its associated gateway rules.

## Request Syntax
<a name="API_DeleteABTest_RequestSyntax"></a>

```
DELETE /ab-tests/{{abTestId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteABTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [abTestId](#API_DeleteABTest_RequestSyntax) **   <a name="BedrockAgentCore-DeleteABTest-request-uri-abTestId"></a>
The unique identifier of the A/B test to delete.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteABTest_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteABTest_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_DeleteABTest_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the deleted A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_DeleteABTest_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteABTest-response-abTestId"></a>
The unique identifier of the deleted A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteABTest_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteABTest-response-status"></a>
The status of the A/B test deletion operation.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

## Errors
<a name="API_DeleteABTest_Errors"></a>

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

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteABTest) 