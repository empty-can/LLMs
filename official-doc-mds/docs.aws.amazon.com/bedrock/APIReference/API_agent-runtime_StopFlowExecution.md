

# StopFlowExecution
<a name="API_agent-runtime_StopFlowExecution"></a>

Stops an Amazon Bedrock flow's execution. This operation prevents further processing of the flow and changes the execution status to `Aborted`.

## Request Syntax
<a name="API_agent-runtime_StopFlowExecution_RequestSyntax"></a>

```
POST /flows/{{flowIdentifier}}/aliases/{{flowAliasIdentifier}}/executions/{{executionIdentifier}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_StopFlowExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionIdentifier](#API_agent-runtime_StopFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StopFlowExecution-request-uri-executionIdentifier"></a>
The unique identifier of the flow execution to stop.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})`   
Required: Yes

 ** [flowAliasIdentifier](#API_agent-runtime_StopFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StopFlowExecution-request-uri-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [flowIdentifier](#API_agent-runtime_StopFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StopFlowExecution-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_StopFlowExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_StopFlowExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_agent-runtime_StopFlowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionArn](#API_agent-runtime_StopFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_StopFlowExecution-response-executionArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the flow execution that was stopped.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})` 

 ** [status](#API_agent-runtime_StopFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_StopFlowExecution-response-status"></a>
The updated status of the flow execution after the stop request. This will typically be ABORTED if the execution was successfully stopped.  
Type: String  
Valid Values: `Running | Succeeded | Failed | TimedOut | Aborted` 

## Errors
<a name="API_agent-runtime_StopFlowExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_agent-runtime_StopFlowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/StopFlowExecution) 