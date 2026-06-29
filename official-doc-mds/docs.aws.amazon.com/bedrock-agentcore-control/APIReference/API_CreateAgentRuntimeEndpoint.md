

# CreateAgentRuntimeEndpoint
<a name="API_CreateAgentRuntimeEndpoint"></a>

Creates an AgentCore Runtime endpoint.

## Request Syntax
<a name="API_CreateAgentRuntimeEndpoint_RequestSyntax"></a>

```
PUT /runtimes/{{agentRuntimeId}}/runtime-endpoints/ HTTP/1.1
Content-type: application/json

{
   "agentRuntimeVersion": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateAgentRuntimeEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeId](#API_CreateAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-request-uri-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime to create an endpoint for.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_CreateAgentRuntimeEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentRuntimeVersion](#API_CreateAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-request-agentRuntimeVersion"></a>
The version of the AgentCore Runtime to use for the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

 ** [clientToken](#API_CreateAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-request-description"></a>
The description of the AgentCore Runtime endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** [name](#API_CreateAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-request-name"></a>
The name of the AgentCore Runtime endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [tags](#API_CreateAgentRuntimeEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-request-tags"></a>
A map of tag keys and values to assign to the agent runtime endpoint. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateAgentRuntimeEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "agentRuntimeArn": "string",
   "agentRuntimeEndpointArn": "string",
   "agentRuntimeId": "string",
   "createdAt": "string",
   "endpointName": "string",
   "status": "string",
   "targetVersion": "string"
}
```

## Response Elements
<a name="API_CreateAgentRuntimeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentRuntimeArn](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [agentRuntimeEndpointArn](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-agentRuntimeEndpointArn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agentEndpoint/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}` 

 ** [agentRuntimeId](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-createdAt"></a>
The timestamp when the AgentCore Runtime endpoint was created.  
Type: Timestamp

 ** [endpointName](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-endpointName"></a>
The name of the AgentCore Runtime endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [status](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-status"></a>
The current status of the AgentCore Runtime endpoint.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING` 

 ** [targetVersion](#API_CreateAgentRuntimeEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntimeEndpoint-response-targetVersion"></a>
The target version of the AgentCore Runtime for the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

## Errors
<a name="API_CreateAgentRuntimeEndpoint_Errors"></a>

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
<a name="API_CreateAgentRuntimeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntimeEndpoint) 