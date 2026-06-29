

# UpdateABTest
<a name="API_UpdateABTest"></a>

Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.

## Request Syntax
<a name="API_UpdateABTest_RequestSyntax"></a>

```
PUT /ab-tests/{{abTestId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "evaluationConfig": { ... },
   "executionStatus": "{{string}}",
   "gatewayFilter": { 
      "targetPaths": [ "{{string}}" ]
   },
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "variants": [ 
      { 
         "name": "{{string}}",
         "variantConfiguration": { 
            "configurationBundle": { 
               "bundleArn": "{{string}}",
               "bundleVersion": "{{string}}"
            },
            "target": { 
               "name": "{{string}}"
            }
         },
         "weight": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateABTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [abTestId](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-uri-abTestId"></a>
The unique identifier of the A/B test to update.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateABTest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-description"></a>
The updated description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [evaluationConfig](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-evaluationConfig"></a>
The updated evaluation configuration.  
Type: [ABTestEvaluationConfig](API_ABTestEvaluationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [executionStatus](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-executionStatus"></a>
The updated execution status to enable or disable the A/B test.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED`   
Required: No

 ** [gatewayFilter](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-gatewayFilter"></a>
The updated gateway filter.  
Type: [GatewayFilter](API_GatewayFilter.md) object  
Required: No

 ** [name](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-name"></a>
The updated name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: No

 ** [roleArn](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-roleArn"></a>
The updated IAM role ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

 ** [variants](#API_UpdateABTest_RequestSyntax) **   <a name="BedrockAgentCore-UpdateABTest-request-variants"></a>
The updated list of variants.  
Type: Array of [Variant](API_Variant.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

## Response Syntax
<a name="API_UpdateABTest_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "executionStatus": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the updated A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-abTestId"></a>
The unique identifier of the updated A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [executionStatus](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-executionStatus"></a>
The execution status of the A/B test.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED` 

 ** [status](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-status"></a>
The status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

 ** [updatedAt](#API_UpdateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateABTest-response-updatedAt"></a>
The timestamp when the A/B test was updated.  
Type: Timestamp

## Errors
<a name="API_UpdateABTest_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

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
<a name="API_UpdateABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/UpdateABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UpdateABTest) 