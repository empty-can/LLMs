

# GetAgentRuntimeEndpoint
<a name="API_GetAgentRuntimeEndpoint"></a>

Gets information about an Amazon Secure AgentEndpoint.

## Request Syntax
<a name="API_GetAgentRuntimeEndpoint_RequestSyntax"></a>

```
GET /runtimes/{{agentRuntimeId}}/runtime-endpoints/{{endpointName}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentRuntimeEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeId](#API_GetAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-request-uri-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime associated with the endpoint.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [endpointName](#API_GetAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-request-uri-endpointName"></a>
The name of the AgentCore Runtime endpoint to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

## Request Body
<a name="API_GetAgentRuntimeEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentRuntimeEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentRuntimeArn": "string",
   "agentRuntimeEndpointArn": "string",
   "createdAt": "string",
   "description": "string",
   "failureReason": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "liveVersion": "string",
   "name": "string",
   "status": "string",
   "targetVersion": "string"
}
```

## Response Elements
<a name="API_GetAgentRuntimeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentRuntimeArn](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [agentRuntimeEndpointArn](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-agentRuntimeEndpointArn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agentEndpoint/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}` 

 ** [createdAt](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-createdAt"></a>
The timestamp when the AgentCore Runtime endpoint was created.  
Type: Timestamp

 ** [description](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-description"></a>
The description of the AgentCore Runtime endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [failureReason](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-failureReason"></a>
The reason for failure if the AgentCore Runtime endpoint is in a failed state.  
Type: String

 ** [id](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-id"></a>
The unique identifier of the AgentCore Runtime endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [lastUpdatedAt](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-lastUpdatedAt"></a>
The timestamp when the AgentCore Runtime endpoint was last updated.  
Type: Timestamp

 ** [liveVersion](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-liveVersion"></a>
The currently deployed version of the AgentCore Runtime on the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

 ** [name](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-name"></a>
The name of the AgentCore Runtime endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [status](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-status"></a>
The current status of the AgentCore Runtime endpoint.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING` 

 ** [targetVersion](#API_GetAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntimeEndpoint-response-targetVersion"></a>
The target version of the AgentCore Runtime for the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

## Errors
<a name="API_GetAgentRuntimeEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

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
<a name="API_GetAgentRuntimeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetAgentRuntimeEndpoint) 