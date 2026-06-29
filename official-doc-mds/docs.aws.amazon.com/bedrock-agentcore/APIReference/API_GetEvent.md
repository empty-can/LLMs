

# GetEvent
<a name="API_GetEvent"></a>

Retrieves information about a specific event in an AgentCore Memory resource.

To use this operation, you must have the `bedrock-agentcore:GetEvent` permission.

## Request Syntax
<a name="API_GetEvent_RequestSyntax"></a>

```
GET /memories/{{memoryId}}/actor/{{actorId}}/sessions/{{sessionId}}/events/{{eventId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actorId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-actorId"></a>
The identifier of the actor associated with the event.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [eventId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-eventId"></a>
The identifier of the event to retrieve.  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: Yes

 ** [memoryId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource containing the event.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_GetEvent_RequestSyntax) **   <a name="BedrockAgentCore-GetEvent-request-uri-sessionId"></a>
The identifier of the session containing the event.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

## Request Body
<a name="API_GetEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [event](#API_GetEvent_ResponseSyntax) **   <a name="BedrockAgentCore-GetEvent-response-event"></a>
The requested event information.  
Type: [Event](API_Event.md) object

## Errors
<a name="API_GetEvent_Errors"></a>

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
<a name="API_GetEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetEvent) 