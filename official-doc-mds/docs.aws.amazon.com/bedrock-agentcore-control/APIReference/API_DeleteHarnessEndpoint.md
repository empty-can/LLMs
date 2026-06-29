

# DeleteHarnessEndpoint
<a name="API_DeleteHarnessEndpoint"></a>

Operation to delete a harness endpoint.

## Request Syntax
<a name="API_DeleteHarnessEndpoint_RequestSyntax"></a>

```
DELETE /harnesses/{{harnessId}}/endpoints/{{endpointName}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteHarnessEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteHarnessEndpoint-request-uri-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}` 

 ** [endpointName](#API_DeleteHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteHarnessEndpoint-request-uri-endpointName"></a>
The name of the endpoint to delete.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [harnessId](#API_DeleteHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteHarnessEndpoint-request-uri-harnessId"></a>
The ID of the harness that the endpoint belongs to.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteHarnessEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteHarnessEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpoint": { 
      "arn": "string",
      "createdAt": "string",
      "description": "string",
      "endpointName": "string",
      "failureReason": "string",
      "harnessId": "string",
      "harnessName": "string",
      "liveVersion": "string",
      "status": "string",
      "targetVersion": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_DeleteHarnessEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_DeleteHarnessEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteHarnessEndpoint-response-endpoint"></a>
The endpoint that was deleted.  
Type: [HarnessEndpoint](API_HarnessEndpoint.md) object

## Errors
<a name="API_DeleteHarnessEndpoint_Errors"></a>

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

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteHarnessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteHarnessEndpoint) 