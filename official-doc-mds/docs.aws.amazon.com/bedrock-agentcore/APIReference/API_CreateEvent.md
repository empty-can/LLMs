

# CreateEvent
<a name="API_CreateEvent"></a>

Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.

To use this operation, you must have the `bedrock-agentcore:CreateEvent` permission.

This operation is subject to request rate limiting.

## Request Syntax
<a name="API_CreateEvent_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/events HTTP/1.1
Content-type: application/json

{
   "actorId": "{{string}}",
   "branch": { 
      "name": "{{string}}",
      "rootEventId": "{{string}}"
   },
   "clientToken": "{{string}}",
   "eventTimestamp": {{number}},
   "extractionMode": "{{string}}",
   "metadata": { 
      "{{string}}" : { ... }
   },
   "payload": [ 
      { ... }
   ],
   "sessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource in which to create the event.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_CreateEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorId](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-actorId"></a>
The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [branch](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-branch"></a>
The branch information for this event. Branches allow for organizing events into different conversation threads or paths.  
Type: [Branch](API_Branch.md) object  
Required: No

 ** [clientToken](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.  
Type: String  
Required: No

 ** [eventTimestamp](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-eventTimestamp"></a>
The timestamp when the event occurred. If not specified, the current time is used.  
Type: Timestamp  
Required: Yes

 ** [extractionMode](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-extractionMode"></a>
Controls long-term memory extraction for this event. When set to `SKIP`, the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.  
Type: String  
Valid Values: `SKIP`   
Required: No

 ** [metadata](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-metadata"></a>
The key-value metadata to attach to the event.  
Type: String to [MetadataValue](API_MetadataValue.md) object map  
Map Entries: Minimum number of 0 items. Maximum number of 15 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [payload](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-payload"></a>
The content payload of the event. This can include conversational data or binary content.  
Type: Array of [PayloadType](API_PayloadType.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

 ** [sessionId](#API_CreateEvent_RequestSyntax) **   <a name="BedrockAgentCore-CreateEvent-request-sessionId"></a>
The identifier of the session in which this event occurs. A session represents a sequence of related events.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

## Response Syntax
<a name="API_CreateEvent_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "event": { 
      "actorId": "string",
      "branch": { 
         "name": "string",
         "rootEventId": "string"
      },
      "eventId": "string",
      "eventTimestamp": number,
      "memoryId": "string",
      "metadata": { 
         "string" : { ... }
      },
      "payload": [ 
         { ... }
      ],
      "sessionId": "string"
   }
}
```

## Response Elements
<a name="API_CreateEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [event](#API_CreateEvent_ResponseSyntax) **   <a name="BedrockAgentCore-CreateEvent-response-event"></a>
The event that was created.  
Type: [Event](API_Event.md) object

## Errors
<a name="API_CreateEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InvalidInputException **   
The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CreateEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CreateEvent) 