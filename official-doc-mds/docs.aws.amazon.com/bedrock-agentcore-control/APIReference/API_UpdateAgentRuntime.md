

# UpdateAgentRuntime
<a name="API_UpdateAgentRuntime"></a>

Updates an existing Amazon Secure Agent.

## Request Syntax
<a name="API_UpdateAgentRuntime_RequestSyntax"></a>

```
PUT /runtimes/{{agentRuntimeId}}/ HTTP/1.1
Content-type: application/json

{
   "agentRuntimeArtifact": { ... },
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
   "metadataConfiguration": { 
      "requireMMDSV2": {{boolean}}
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
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgentRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeId](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-uri-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime to update.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateAgentRuntime_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentRuntimeArtifact](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-agentRuntimeArtifact"></a>
The updated artifact of the AgentCore Runtime.  
Type: [AgentRuntimeArtifact](API_AgentRuntimeArtifact.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [authorizerConfiguration](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-authorizerConfiguration"></a>
The updated authorizer configuration for the AgentCore Runtime.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [clientToken](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-description"></a>
The updated description of the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [environmentVariables](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-environmentVariables"></a>
Updated environment variables to set in the AgentCore Runtime environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.  
Required: No

 ** [filesystemConfigurations](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-filesystemConfigurations"></a>
The updated filesystem configurations to mount into the AgentCore Runtime.  
Type: Array of [FilesystemConfiguration](API_FilesystemConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

 ** [lifecycleConfiguration](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-lifecycleConfiguration"></a>
The updated life cycle configuration for the AgentCore Runtime.  
Type: [LifecycleConfiguration](API_LifecycleConfiguration.md) object  
Required: No

 ** [metadataConfiguration](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-metadataConfiguration"></a>
The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.  
Type: [RuntimeMetadataConfiguration](API_RuntimeMetadataConfiguration.md) object  
Required: No

 ** [networkConfiguration](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-networkConfiguration"></a>
The updated network configuration for the AgentCore Runtime.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: Yes

 ** [protocolConfiguration](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-protocolConfiguration"></a>
The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.  
Type: [ProtocolConfiguration](API_ProtocolConfiguration.md) object  
Required: No

 ** [requestHeaderConfiguration](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-requestHeaderConfiguration"></a>
The updated configuration for HTTP request headers that will be passed through to the runtime.  
Type: [RequestHeaderConfiguration](API_RequestHeaderConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [roleArn](#API_UpdateAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-request-roleArn"></a>
The updated IAM role ARN that provides permissions for the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

## Response Syntax
<a name="API_UpdateAgentRuntime_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "agentRuntimeArn": "string",
   "agentRuntimeId": "string",
   "agentRuntimeVersion": "string",
   "createdAt": "string",
   "lastUpdatedAt": "string",
   "status": "string",
   "workloadIdentityDetails": { 
      "workloadIdentityArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdateAgentRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentRuntimeArn](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the updated AgentCore Runtime.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [agentRuntimeId](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-agentRuntimeId"></a>
The unique identifier of the updated AgentCore Runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [agentRuntimeVersion](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-agentRuntimeVersion"></a>
The version of the updated AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

 ** [createdAt](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-createdAt"></a>
The timestamp when the AgentCore Runtime was created.  
Type: Timestamp

 ** [lastUpdatedAt](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-lastUpdatedAt"></a>
The timestamp when the AgentCore Runtime was last updated.  
Type: Timestamp

 ** [status](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-status"></a>
The current status of the updated AgentCore Runtime.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING` 

 ** [workloadIdentityDetails](#API_UpdateAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateAgentRuntime-response-workloadIdentityDetails"></a>
The workload identity details for the updated AgentCore Runtime.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_UpdateAgentRuntime_Errors"></a>

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
<a name="API_UpdateAgentRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateAgentRuntime) 