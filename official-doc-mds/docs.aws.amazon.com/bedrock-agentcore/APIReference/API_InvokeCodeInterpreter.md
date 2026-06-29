

# InvokeCodeInterpreter
<a name="API_InvokeCodeInterpreter"></a>

Executes code within an active code interpreter session in Amazon Bedrock AgentCore. This operation processes the provided code, runs it in a secure environment, and returns the execution results including output, errors, and generated visualizations.

To execute code, you must specify the code interpreter identifier, session ID, and the code to run in the arguments parameter. The operation returns a stream containing the execution results, which can include text output, error messages, and data visualizations.

This operation is subject to request rate limiting based on your account's service quotas.

The following operations are related to `InvokeCodeInterpreter`:
+  [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html) 
+  [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html) 

## Request Syntax
<a name="API_InvokeCodeInterpreter_RequestSyntax"></a>

```
POST /code-interpreters/{{codeInterpreterIdentifier}}/tools/invoke HTTP/1.1
x-amzn-code-interpreter-session-id: {{sessionId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "arguments": { 
      "clearContext": {{boolean}},
      "code": "{{string}}",
      "command": "{{string}}",
      "content": [ 
         { 
            "blob": {{blob}},
            "path": "{{string}}",
            "text": "{{string}}"
         }
      ],
      "directoryPath": "{{string}}",
      "language": "{{string}}",
      "path": "{{string}}",
      "paths": [ "{{string}}" ],
      "runtime": "{{string}}",
      "taskId": "{{string}}"
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InvokeCodeInterpreter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with `StartCodeInterpreterSession`.  
Required: Yes

 ** [sessionId](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-sessionId"></a>
The unique identifier of the code interpreter session to use. This must be an active session created with `StartCodeInterpreterSession`. If the session has expired or been stopped, the request will fail.  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [traceId](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_InvokeCodeInterpreter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arguments](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-arguments"></a>
The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.  
Type: [ToolArguments](API_ToolArguments.md) object  
Required: No

 ** [name](#API_InvokeCodeInterpreter_RequestSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-request-name"></a>
The name of the code interpreter to invoke.  
Type: String  
Valid Values: `executeCode | executeCommand | readFiles | listFiles | removeFiles | writeFiles | startCommandExecution | getTask | stopTask`   
Required: Yes

## Response Syntax
<a name="API_InvokeCodeInterpreter_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-code-interpreter-session-id: {{sessionId}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "conflictException": { 
   },
   "internalServerException": { 
   },
   "resourceNotFoundException": { 
   },
   "result": { 
      "content": [ 
         { 
            "data": blob,
            "description": "string",
            "mimeType": "string",
            "name": "string",
            "resource": { 
               "blob": blob,
               "mimeType": "string",
               "text": "string",
               "type": "string",
               "uri": "string"
            },
            "size": number,
            "text": "string",
            "type": "string",
            "uri": "string"
         }
      ],
      "isError": boolean,
      "structuredContent": { 
         "executionTime": number,
         "exitCode": number,
         "stderr": "string",
         "stdout": "string",
         "taskId": "string",
         "taskStatus": "string"
      }
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_InvokeCodeInterpreter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [sessionId](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-sessionId"></a>
The identifier of the code interpreter session.  
Pattern: `[0-9a-zA-Z]{1,40}` 

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-accessDeniedException"></a>
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
Type: Exception  
HTTP Status Code: 403

 ** [conflictException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-conflictException"></a>
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
Type: Exception  
HTTP Status Code: 409

 ** [internalServerException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404

 ** [result](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-result"></a>
The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore. This structure contains the results of code execution, including textual output, structured data, and error information. Agents use these results to generate responses that incorporate computation, data analysis, and visualization.  
Type: [CodeInterpreterResult](API_CodeInterpreterResult.md) object

 ** [serviceQuotaExceededException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402

 ** [throttlingException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_InvokeCodeInterpreter_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeCodeInterpreter-response-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_InvokeCodeInterpreter_Errors"></a>

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

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_InvokeCodeInterpreter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeCodeInterpreter) 