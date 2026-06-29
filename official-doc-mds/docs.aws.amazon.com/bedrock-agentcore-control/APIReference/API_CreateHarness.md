

# CreateHarness
<a name="API_CreateHarness"></a>

Operation to create a harness.

## Request Syntax
<a name="API_CreateHarness_RequestSyntax"></a>

```
POST /harnesses HTTP/1.1
Content-type: application/json

{
   "allowedTools": [ "{{string}}" ],
   "authorizerConfiguration": { ... },
   "clientToken": "{{string}}",
   "environment": { ... },
   "environmentArtifact": { ... },
   "environmentVariables": { 
      "{{string}}" : "{{string}}" 
   },
   "executionRoleArn": "{{string}}",
   "harnessName": "{{string}}",
   "maxIterations": {{number}},
   "maxTokens": {{number}},
   "memory": { ... },
   "model": { ... },
   "skills": [ 
      { ... }
   ],
   "systemPrompt": [ 
      { ... }
   ],
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "timeoutSeconds": {{number}},
   "tools": [ 
      { 
         "config": { ... },
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "truncation": { 
      "config": { ... },
      "strategy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateHarness_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateHarness_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedTools](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-allowedTools"></a>
The tools that the agent is allowed to use. Supports glob patterns such as \* for all tools, @builtin for all built-in tools, or @serverName/toolName for specific MCP server tools.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `(\*|@?[^/]+(/[^/]+)?)`   
Required: No

 ** [authorizerConfiguration](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-authorizerConfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.   
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [clientToken](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [environment](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-environment"></a>
The compute environment configuration for the harness, including network and lifecycle settings.  
Type: [HarnessEnvironmentProviderRequest](API_HarnessEnvironmentProviderRequest.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [environmentArtifact](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-environmentArtifact"></a>
The environment artifact for the harness, such as a custom container image containing additional dependencies.  
Type: [HarnessEnvironmentArtifact](API_HarnessEnvironmentArtifact.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [environmentVariables](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-environmentVariables"></a>
Environment variables to set in the harness runtime environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.  
Required: No

 ** [executionRoleArn](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-executionRoleArn"></a>
The ARN of the IAM role that the harness assumes when running. This role must have permissions for the services the agent needs to access, such as Amazon Bedrock for model invocation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [harnessName](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-harnessName"></a>
The name of the harness. Must start with a letter and contain only alphanumeric characters and underscores.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}`   
Required: Yes

 ** [maxIterations](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-maxIterations"></a>
The maximum number of iterations the agent loop can execute per invocation.  
Type: Integer  
Required: No

 ** [maxTokens](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-maxTokens"></a>
The maximum total number of output tokens the agent can generate across all model calls within a single invocation.  
Type: Integer  
Required: No

 ** [memory](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-memory"></a>
The AgentCore Memory configuration for persisting conversation context across sessions.  
Type: [HarnessMemoryConfiguration](API_HarnessMemoryConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [model](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-model"></a>
The model configuration for the harness. Supports Amazon Bedrock, OpenAI, and Google Gemini model providers.  
Type: [HarnessModelConfiguration](API_HarnessModelConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [skills](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-skills"></a>
The skills available to the agent. Skills are bundles of files that the agent can pull into its context on demand.  
Type: Array of [HarnessSkill](API_HarnessSkill.md) objects  
Required: No

 ** [systemPrompt](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-systemPrompt"></a>
The system prompt that defines the agent's behavior and instructions.  
Type: Array of [HarnessSystemContentBlock](API_HarnessSystemContentBlock.md) objects  
Required: No

 ** [tags](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-tags"></a>
Tags to apply to the harness resource.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [timeoutSeconds](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-timeoutSeconds"></a>
The maximum duration in seconds for the agent loop execution per invocation.  
Type: Integer  
Required: No

 ** [tools](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-tools"></a>
The tools available to the agent, such as remote MCP servers, AgentCore Gateway, AgentCore Browser, Code Interpreter, or inline functions.  
Type: Array of [HarnessTool](API_HarnessTool.md) objects  
Required: No

 ** [truncation](#API_CreateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-request-truncation"></a>
The truncation configuration for managing conversation context when it exceeds model limits.  
Type: [HarnessTruncationConfiguration](API_HarnessTruncationConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_CreateHarness_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "harness": { 
      "allowedTools": [ "string" ],
      "arn": "string",
      "authorizerConfiguration": { ... },
      "createdAt": "string",
      "environment": { ... },
      "environmentArtifact": { ... },
      "environmentVariables": { 
         "string" : "string" 
      },
      "executionRoleArn": "string",
      "failureReason": "string",
      "harnessId": "string",
      "harnessName": "string",
      "harnessVersion": "string",
      "maxIterations": number,
      "maxTokens": number,
      "memory": { ... },
      "model": { ... },
      "skills": [ 
         { ... }
      ],
      "status": "string",
      "systemPrompt": [ 
         { ... }
      ],
      "timeoutSeconds": number,
      "tools": [ 
         { 
            "config": { ... },
            "name": "string",
            "type": "string"
         }
      ],
      "truncation": { 
         "config": { ... },
         "strategy": "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateHarness_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [harness](#API_CreateHarness_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateHarness-response-harness"></a>
The harness that was created.  
Type: [Harness](API_Harness.md) object

## Errors
<a name="API_CreateHarness_Errors"></a>

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
<a name="API_CreateHarness_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateHarness) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateHarness) 