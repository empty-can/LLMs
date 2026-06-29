

# GetAgentRuntime
<a name="API_GetAgentRuntime"></a>

Gets an Amazon Bedrock AgentCore Runtime.

## Request Syntax
<a name="API_GetAgentRuntime_RequestSyntax"></a>

```
GET /runtimes/{{agentRuntimeId}}/?version={{agentRuntimeVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeId](#API_GetAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-request-uri-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [agentRuntimeVersion](#API_GetAgentRuntime_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-request-uri-agentRuntimeVersion"></a>
The version of the AgentCore Runtime to retrieve.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

## Request Body
<a name="API_GetAgentRuntime_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentRuntime_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentRuntimeArn": "string",
   "agentRuntimeArtifact": { ... },
   "agentRuntimeId": "string",
   "agentRuntimeName": "string",
   "agentRuntimeVersion": "string",
   "authorizerConfiguration": { ... },
   "createdAt": "string",
   "description": "string",
   "environmentVariables": { 
      "string" : "string" 
   },
   "failureReason": "string",
   "filesystemConfigurations": [ 
      { ... }
   ],
   "lastUpdatedAt": "string",
   "lifecycleConfiguration": { 
      "idleRuntimeSessionTimeout": number,
      "maxLifetime": number
   },
   "metadataConfiguration": { 
      "requireMMDSV2": boolean
   },
   "networkConfiguration": { 
      "networkMode": "string",
      "networkModeConfig": { 
         "requireServiceS3Endpoint": boolean,
         "securityGroups": [ "string" ],
         "subnets": [ "string" ]
      }
   },
   "protocolConfiguration": { 
      "serverProtocol": "string"
   },
   "requestHeaderConfiguration": { ... },
   "roleArn": "string",
   "status": "string",
   "workloadIdentityDetails": { 
      "workloadIdentityArn": "string"
   }
}
```

## Response Elements
<a name="API_GetAgentRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentRuntimeArn](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [agentRuntimeArtifact](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-agentRuntimeArtifact"></a>
The artifact of the AgentCore Runtime.  
Type: [AgentRuntimeArtifact](API_AgentRuntimeArtifact.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [agentRuntimeId](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [agentRuntimeName](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-agentRuntimeName"></a>
The name of the AgentCore Runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [agentRuntimeVersion](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-agentRuntimeVersion"></a>
The version of the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

 ** [authorizerConfiguration](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-authorizerConfiguration"></a>
The authorizer configuration for the AgentCore Runtime.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-createdAt"></a>
The timestamp when the AgentCore Runtime was created.  
Type: Timestamp

 ** [description](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-description"></a>
The description of the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [environmentVariables](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-environmentVariables"></a>
Environment variables set in the AgentCore Runtime environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.

 ** [failureReason](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-failureReason"></a>
The reason for failure if the AgentCore Runtime is in a failed state.  
Type: String

 ** [filesystemConfigurations](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-filesystemConfigurations"></a>
The filesystem configurations mounted into the AgentCore Runtime.  
Type: Array of [FilesystemConfiguration](API_FilesystemConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [lastUpdatedAt](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-lastUpdatedAt"></a>
The timestamp when the AgentCore Runtime was last updated.  
Type: Timestamp

 ** [lifecycleConfiguration](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-lifecycleConfiguration"></a>
The life cycle configuration for the AgentCore Runtime.  
Type: [LifecycleConfiguration](API_LifecycleConfiguration.md) object

 ** [metadataConfiguration](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-metadataConfiguration"></a>
Configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.  
Type: [RuntimeMetadataConfiguration](API_RuntimeMetadataConfiguration.md) object

 ** [networkConfiguration](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-networkConfiguration"></a>
The network configuration for the AgentCore Runtime.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object

 ** [protocolConfiguration](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-protocolConfiguration"></a>
The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.  
Type: [ProtocolConfiguration](API_ProtocolConfiguration.md) object

 ** [requestHeaderConfiguration](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-requestHeaderConfiguration"></a>
Configuration for HTTP request headers that will be passed through to the runtime.  
Type: [RequestHeaderConfiguration](API_RequestHeaderConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [roleArn](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-roleArn"></a>
The IAM role ARN that provides permissions for the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-status"></a>
The current status of the AgentCore Runtime.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING` 

 ** [workloadIdentityDetails](#API_GetAgentRuntime_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetAgentRuntime-response-workloadIdentityDetails"></a>
The workload identity details for the AgentCore Runtime.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_GetAgentRuntime_Errors"></a>

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
<a name="API_GetAgentRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetAgentRuntime) 