

# UpdateHarness
<a name="API_UpdateHarness"></a>

Operation to update a harness.

## Request Syntax
<a name="API_UpdateHarness_RequestSyntax"></a>

```
PATCH /harnesses/{{harnessId}} HTTP/1.1
Content-type: application/json

{
   "allowedTools": [ "{{string}}" ],
   "authorizerConfiguration": { 
      "optionalValue": { ... }
   },
   "clientToken": "{{string}}",
   "environment": { ... },
   "environmentArtifact": { 
      "optionalValue": { ... }
   },
   "environmentVariables": { 
      "{{string}}" : "{{string}}" 
   },
   "executionRoleArn": "{{string}}",
   "maxIterations": {{number}},
   "maxTokens": {{number}},
   "memory": { 
      "optionalValue": { ... }
   },
   "model": { ... },
   "skills": [ 
      { ... }
   ],
   "systemPrompt": [ 
      { ... }
   ],
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
<a name="API_UpdateHarness_RequestParameters"></a>

The request uses the following URI parameters.

 ** [harnessId](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-uri-harnessId"></a>
The ID of the harness to update.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateHarness_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedTools](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-allowedTools"></a>
The tools that the agent is allowed to use. If specified, this replaces all existing allowed tools. If not specified, the existing value is retained.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `(\*|@?[^/]+(/[^/]+)?)`   
Required: No

 ** [authorizerConfiguration](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-authorizerConfiguration"></a>
Wrapper for updating an optional AuthorizerConfiguration field with PATCH semantics. When present in an update request, the authorizer configuration is replaced with optionalValue. When absent, the authorizer configuration is left unchanged. To unset, include the wrapper with optionalValue not specified.  
Type: [UpdatedAuthorizerConfiguration](API_UpdatedAuthorizerConfiguration.md) object  
Required: No

 ** [clientToken](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [environment](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-environment"></a>
The compute environment configuration for the harness. If not specified, the existing value is retained.  
Type: [HarnessEnvironmentProviderRequest](API_HarnessEnvironmentProviderRequest.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [environmentArtifact](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-environmentArtifact"></a>
The environment artifact for the harness. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.  
Type: [UpdatedHarnessEnvironmentArtifact](API_UpdatedHarnessEnvironmentArtifact.md) object  
Required: No

 ** [environmentVariables](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-environmentVariables"></a>
Environment variables to set in the harness runtime environment. If specified, this replaces all existing environment variables. If not specified, the existing value is retained.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.  
Required: No

 ** [executionRoleArn](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-executionRoleArn"></a>
The ARN of the IAM role that the harness assumes when running. If not specified, the existing value is retained.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

 ** [maxIterations](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-maxIterations"></a>
The maximum number of iterations the agent loop can execute per invocation. If not specified, the existing value is retained.  
Type: Integer  
Required: No

 ** [maxTokens](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-maxTokens"></a>
The maximum total number of output tokens the agent can generate across all model calls within a single invocation. If not specified, the existing value is retained.  
Type: Integer  
Required: No

 ** [memory](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-memory"></a>
The AgentCore Memory configuration. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.  
Type: [UpdatedHarnessMemoryConfiguration](API_UpdatedHarnessMemoryConfiguration.md) object  
Required: No

 ** [model](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-model"></a>
The model configuration for the harness. If not specified, the existing value is retained.  
Type: [HarnessModelConfiguration](API_HarnessModelConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [skills](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-skills"></a>
The skills available to the agent. If specified, this replaces all existing skills. If not specified, the existing value is retained.  
Type: Array of [HarnessSkill](API_HarnessSkill.md) objects  
Required: No

 ** [systemPrompt](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-systemPrompt"></a>
The system prompt that defines the agent's behavior. If not specified, the existing value is retained.  
Type: Array of [HarnessSystemContentBlock](API_HarnessSystemContentBlock.md) objects  
Required: No

 ** [timeoutSeconds](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-timeoutSeconds"></a>
The maximum duration in seconds for the agent loop execution per invocation. If not specified, the existing value is retained.  
Type: Integer  
Required: No

 ** [tools](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-tools"></a>
The tools available to the agent. If specified, this replaces all existing tools. If not specified, the existing value is retained.  
Type: Array of [HarnessTool](API_HarnessTool.md) objects  
Required: No

 ** [truncation](#API_UpdateHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-request-truncation"></a>
The truncation configuration for managing conversation context. If not specified, the existing value is retained.  
Type: [HarnessTruncationConfiguration](API_HarnessTruncationConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_UpdateHarness_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateHarness_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [harness](#API_UpdateHarness_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateHarness-response-harness"></a>
The updated harness.  
Type: [Harness](API_Harness.md) object

## Errors
<a name="API_UpdateHarness_Errors"></a>

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
<a name="API_UpdateHarness_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateHarness) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateHarness) 