

# DeleteMemory
<a name="API_DeleteMemory"></a>

Deletes an Amazon Bedrock AgentCore Memory resource.

## Request Syntax
<a name="API_DeleteMemory_RequestSyntax"></a>

```
DELETE /memories/{{memoryId}}/delete?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMemory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteMemory-request-uri-clientToken"></a>
A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.  
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [memoryId](#API_DeleteMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteMemory-request-uri-memoryId"></a>
The unique identifier of the memory to delete.  
Length Constraints: Minimum length of 12.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteMemory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMemory_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "memoryId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [memoryId](#API_DeleteMemory_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteMemory-response-memoryId"></a>
The unique identifier of the deleted AgentCore Memory resource.  
Type: String  
Length Constraints: Minimum length of 12.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteMemory_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteMemory-response-status"></a>
The current status of the AgentCore Memory resource deletion.  
Type: String  
Valid Values: `CREATING | ACTIVE | FAILED | DELETING | UPDATING` 

## Errors
<a name="API_DeleteMemory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ThrottledException **   
API rate limit has been exceeded.  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteMemory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteMemory) 