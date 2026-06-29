

# ListEvents
<a name="API_ListEvents"></a>

Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:ListEvents` permission.

## Request Syntax
<a name="API_ListEvents_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/actor/{{actorId}}/sessions/{{sessionId}} HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "branch": { 
         "includeParentBranches": {{boolean}},
         "name": "{{string}}"
      },
      "eventMetadata": [ 
         { 
            "left": { ... },
            "operator": "{{string}}",
            "right": { ... }
         }
      ]
   },
   "includePayloads": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actorId](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-uri-actorId"></a>
The identifier of the actor for which to list events.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [memoryId](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource for which to list events.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-uri-sessionId"></a>
The identifier of the session for which to list events.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

## Request Body
<a name="API_ListEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-filter"></a>
Filter criteria to apply when listing events.  
Type: [FilterInput](API_FilterInput.md) object  
Required: No

 ** [includePayloads](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-includePayloads"></a>
Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.  
Type: Boolean  
Required: No

 ** [maxResults](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListEvents_RequestSyntax) **   <a name="BedrockAgentCore-ListEvents-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "events": [ 
      { 
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListEvents_ResponseSyntax) **   <a name="BedrockAgentCore-ListEvents-response-events"></a>
The list of events that match the specified criteria.  
Type: Array of [Event](API_Event.md) objects

 ** [nextToken](#API_ListEvents_ResponseSyntax) **   <a name="BedrockAgentCore-ListEvents-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

## Errors
<a name="API_ListEvents_Errors"></a>

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
<a name="API_ListEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListEvents) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListEvents) 