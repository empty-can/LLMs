

# CreateAgentRuntime
<a name="API_CreateAgentRuntime"></a>

Creates an Amazon Bedrock AgentCore Runtime.

## Request Syntax
<a name="API_CreateAgentRuntime_RequestSyntax"></a>

```
PUT /runtimes/ HTTP/1.1
Content-type: application/json

{
   "agentRuntimeArtifact": { ... },
   "agentRuntimeName": "{{string}}",
   "authorizerConfiguration": { ... },
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "environmentVariables": { 
      "{{string}}" : "{{string}}" 
   },
   "filesystemConfigurations": [ 
      { ... }
   ],
   "lifecycleConfiguration": { 
      "idleRuntimeSessionTimeout": {{number}},
      "maxLifetime": {{number}}
   },
   "networkConfiguration": { 
      "networkMode": "{{string}}",
      "networkModeConfig": { 
         "requireServiceS3Endpoint": {{boolean}},
         "securityGroups": [ "{{string}}" ],
         "subnets": [ "{{string}}" ]
      }
   },
   "protocolConfiguration": { 
      "serverProtocol": "{{string}}"
   },
   "requestHeaderConfiguration": { ... },
   "roleArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateAgentRuntime_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentRuntime_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentRuntimeArtifact](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-agentRuntimeArtifact"></a>
The artifact of the AgentCore Runtime.  
Type: [AgentRuntimeArtifact](API_AgentRuntimeArtifact.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [agentRuntimeName](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-agentRuntimeName"></a>
The name of the AgentCore Runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [authorizerConfiguration](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-authorizerConfiguration"></a>
The authorizer configuration for the AgentCore Runtime.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [clientToken](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-description"></a>
The description of the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [environmentVariables](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-environmentVariables"></a>
Environment variables to set in the AgentCore Runtime environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.  
Required: No

 ** [filesystemConfigurations](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-filesystemConfigurations"></a>
The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.  
Type: Array of [FilesystemConfiguration](API_FilesystemConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

 ** [lifecycleConfiguration](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-lifecycleConfiguration"></a>
The life cycle configuration for the AgentCore Runtime.  
Type: [LifecycleConfiguration](API_LifecycleConfiguration.md) object  
Required: No

 ** [networkConfiguration](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-networkConfiguration"></a>
The network configuration for the AgentCore Runtime.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: Yes

 ** [protocolConfiguration](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-protocolConfiguration"></a>
The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.  
Type: [ProtocolConfiguration](API_ProtocolConfiguration.md) object  
Required: No

 ** [requestHeaderConfiguration](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-requestHeaderConfiguration"></a>
Configuration for HTTP request headers that will be passed through to the runtime.  
Type: [RequestHeaderConfiguration](API_RequestHeaderConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [roleArn](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-roleArn"></a>
The IAM role ARN that provides permissions for the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [tags](#API_CreateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-request-tags"></a>
A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateAgentRuntime_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "agentRuntimeArn": "string",
   "agentRuntimeId": "string",
   "agentRuntimeVersion": "string",
   "createdAt": "string",
   "status": "string",
   "workloadIdentityDetails": { 
      "workloadIdentityArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateAgentRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentRuntimeArn](#API_CreateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-response-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [agentRuntimeId](#API_CreateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-response-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [agentRuntimeVersion](#API_CreateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-response-agentRuntimeVersion"></a>
The version of the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

 ** [createdAt](#API_CreateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-response-createdAt"></a>
The timestamp when the AgentCore Runtime was created.  
Type: Timestamp

 ** [status](#API_CreateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-response-status"></a>
The current status of the AgentCore Runtime.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING` 

 ** [workloadIdentityDetails](#API_CreateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateAgentRuntime-response-workloadIdentityDetails"></a>
The workload identity details for the AgentCore Runtime.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_CreateAgentRuntime_Errors"></a>

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
<a name="API_CreateAgentRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateAgentRuntime) 