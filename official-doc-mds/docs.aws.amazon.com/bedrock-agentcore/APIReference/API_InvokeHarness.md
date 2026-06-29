

# InvokeHarness
<a name="API_InvokeHarness"></a>

Operation to invoke a Harness.

## Request Syntax
<a name="API_InvokeHarness_RequestSyntax"></a>

```
POST /harnesses/invoke?harnessArn={{harnessArn}}&qualifier={{qualifier}} HTTP/1.1
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
X-Amzn-Bedrock-AgentCore-Runtime-User-Id: {{runtimeUserId}}
Content-type: application/json

{
   "actorId": "{{string}}",
   "allowedTools": [ "{{string}}" ],
   "maxIterations": {{number}},
   "maxTokens": {{number}},
   "messages": [ 
      { 
         "content": [ 
            { ... }
         ],
         "role": "{{string}}"
      }
   ],
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
   ]
}
```

## URI Request Parameters
<a name="API_InvokeHarness_RequestParameters"></a>

The request uses the following URI parameters.

 ** [harnessArn](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-uri-harnessArn"></a>
The ARN of the harness to invoke.  
Pattern: `arn:([^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:harness/[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [qualifier](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-uri-qualifier"></a>
The endpoint name to invoke. If omitted, the DEFAULT endpoint is used.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [runtimeSessionId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-runtimeSessionId"></a>
The session ID for the invocation. Use the same session ID across requests to continue a conversation.  
Length Constraints: Minimum length of 33. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** [runtimeUserId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-runtimeUserId"></a>
An identifier for the end user making the request. This value is passed through to the runtime container.

## Request Body
<a name="API_InvokeHarness_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorId](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-actorId"></a>
The actor ID for memory operations. Overrides the actor ID configured on the harness.  
Type: String  
Required: No

 ** [allowedTools](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-allowedTools"></a>
The tools that the agent is allowed to use for this invocation. If specified, overrides the harness default.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `(\*|@?[^/]+(/[^/]+)?)`   
Required: No

 ** [maxIterations](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-maxIterations"></a>
The maximum number of iterations the agent loop can execute. If specified, overrides the harness default.  
Type: Integer  
Required: No

 ** [maxTokens](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-maxTokens"></a>
The maximum number of tokens the agent can generate per iteration. If specified, overrides the harness default.  
Type: Integer  
Required: No

 ** [messages](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-messages"></a>
The messages to send to the agent.  
Type: Array of [HarnessMessage](API_HarnessMessage.md) objects  
Required: Yes

 ** [model](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-model"></a>
The model configuration to use for this invocation. If specified, overrides the harness default.  
Type: [HarnessModelConfiguration](API_HarnessModelConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [skills](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-skills"></a>
The skills available to the agent for this invocation. If specified, overrides the harness default.  
Type: Array of [HarnessSkill](API_HarnessSkill.md) objects  
Required: No

 ** [systemPrompt](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-systemPrompt"></a>
The system prompt to use for this invocation. If specified, overrides the harness default.  
Type: Array of [HarnessSystemContentBlock](API_HarnessSystemContentBlock.md) objects  
Required: No

 ** [timeoutSeconds](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-timeoutSeconds"></a>
The maximum duration in seconds for the agent loop execution. If specified, overrides the harness default.  
Type: Integer  
Required: No

 ** [tools](#API_InvokeHarness_RequestSyntax) **   <a name="BedrockAgentCore-InvokeHarness-request-tools"></a>
The tools available to the agent for this invocation. If specified, overrides the harness default.  
Type: Array of [HarnessTool](API_HarnessTool.md) objects  
Required: No

## Response Syntax
<a name="API_InvokeHarness_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contentBlockDelta": { 
      "contentBlockIndex": number,
      "delta": { ... }
   },
   "contentBlockStart": { 
      "contentBlockIndex": number,
      "start": { ... }
   },
   "contentBlockStop": { 
      "contentBlockIndex": number
   },
   "internalServerException": { 
   },
   "messageStart": { 
      "role": "string"
   },
   "messageStop": { 
      "stopReason": "string"
   },
   "metadata": { 
      "metrics": { 
         "latencyMs": number
      },
      "usage": { 
         "cacheReadInputTokens": number,
         "cacheWriteInputTokens": number,
         "inputTokens": number,
         "outputTokens": number,
         "totalTokens": number
      }
   },
   "runtimeClientError": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_InvokeHarness_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contentBlockDelta](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-contentBlockDelta"></a>
A delta update to the current content block.  
Type: [HarnessContentBlockDeltaEvent](API_HarnessContentBlockDeltaEvent.md) object

 ** [contentBlockStart](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-contentBlockStart"></a>
Indicates the start of a new content block.  
Type: [HarnessContentBlockStartEvent](API_HarnessContentBlockStartEvent.md) object

 ** [contentBlockStop](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-contentBlockStop"></a>
Indicates the end of the current content block.  
Type: [HarnessContentBlockStopEvent](API_HarnessContentBlockStopEvent.md) object

 ** [internalServerException](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500

 ** [messageStart](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-messageStart"></a>
Indicates the start of a new message from the agent.  
Type: [HarnessMessageStartEvent](API_HarnessMessageStartEvent.md) object

 ** [messageStop](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-messageStop"></a>
Indicates the end of the current message.  
Type: [HarnessMessageStopEvent](API_HarnessMessageStopEvent.md) object

 ** [metadata](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-metadata"></a>
Token usage and latency metrics for the invocation.  
Type: [HarnessMetadataEvent](API_HarnessMetadataEvent.md) object

 ** [runtimeClientError](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-runtimeClientError"></a>
An error returned by the runtime container during agent execution.  
Type: Exception  
HTTP Status Code: 424

 ** [validationException](#API_InvokeHarness_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeHarness-response-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_InvokeHarness_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_InvokeHarness_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeHarness) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeHarness) 