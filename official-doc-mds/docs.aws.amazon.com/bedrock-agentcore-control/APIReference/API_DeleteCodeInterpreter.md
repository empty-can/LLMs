

# DeleteCodeInterpreter
<a name="API_DeleteCodeInterpreter"></a>

Deletes a custom code interpreter.

## Request Syntax
<a name="API_DeleteCodeInterpreter_RequestSyntax"></a>

```
DELETE /code-interpreters/{{codeInterpreterId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCodeInterpreter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteCodeInterpreter-request-uri-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}` 

 ** [codeInterpreterId](#API_DeleteCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteCodeInterpreter-request-uri-codeInterpreterId"></a>
The unique identifier of the code interpreter to delete.  
Pattern: `(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

## Request Body
<a name="API_DeleteCodeInterpreter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCodeInterpreter_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "codeInterpreterId": "string",
   "lastUpdatedAt": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteCodeInterpreter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [codeInterpreterId](#API_DeleteCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteCodeInterpreter-response-codeInterpreterId"></a>
The unique identifier of the deleted code interpreter.  
Type: String  
Pattern: `(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [lastUpdatedAt](#API_DeleteCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteCodeInterpreter-response-lastUpdatedAt"></a>
The timestamp when the code interpreter was last updated.  
Type: Timestamp

 ** [status](#API_DeleteCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteCodeInterpreter-response-status"></a>
The current status of the code interpreter deletion.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | READY | DELETING | DELETE_FAILED | DELETED` 

## Errors
<a name="API_DeleteCodeInterpreter_Errors"></a>

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

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCodeInterpreter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteCodeInterpreter) 