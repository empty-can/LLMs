

# PutInvocationStep
<a name="API_agent-runtime_PutInvocationStep"></a>

Add an invocation step to an invocation in a session. An invocation step stores fine-grained state checkpoints, including text and images, for each interaction. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

Related APIs:
+  [GetInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetInvocationStep.html) 
+  [ListInvocationSteps](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocationSteps.html) 
+  [ListInvocations](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html) 
+  [ListSessions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html) 

## Request Syntax
<a name="API_agent-runtime_PutInvocationStep_RequestSyntax"></a>

```
PUT /sessions/{{sessionIdentifier}}/invocationSteps/ HTTP/1.1
Content-type: application/json

{
   "invocationIdentifier": "{{string}}",
   "invocationStepId": "{{string}}",
   "invocationStepTime": "{{string}}",
   "payload": { ... }
}
```

## URI Request Parameters
<a name="API_agent-runtime_PutInvocationStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionIdentifier](#API_agent-runtime_PutInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_PutInvocationStep-request-uri-sessionIdentifier"></a>
The unique identifier for the session to add the invocation step to. You can specify either the session's `sessionId` or its Amazon Resource Name (ARN).  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_PutInvocationStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [invocationIdentifier](#API_agent-runtime_PutInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_PutInvocationStep-request-invocationIdentifier"></a>
The unique identifier (in UUID format) of the invocation to add the invocation step to.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** [invocationStepId](#API_agent-runtime_PutInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_PutInvocationStep-request-invocationStepId"></a>
The unique identifier of the invocation step in UUID format.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

 ** [invocationStepTime](#API_agent-runtime_PutInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_PutInvocationStep-request-invocationStepTime"></a>
The timestamp for when the invocation step occurred.  
Type: Timestamp  
Required: Yes

 ** [payload](#API_agent-runtime_PutInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_PutInvocationStep-request-payload"></a>
The payload for the invocation step, including text and images for the interaction.  
Type: [InvocationStepPayload](API_agent-runtime_InvocationStepPayload.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_agent-runtime_PutInvocationStep_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "invocationStepId": "string"
}
```

## Response Elements
<a name="API_agent-runtime_PutInvocationStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [invocationStepId](#API_agent-runtime_PutInvocationStep_ResponseSyntax) **   <a name="bedrock-agent-runtime_PutInvocationStep-response-invocationStepId"></a>
The unique identifier of the invocation step in UUID format.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

## Errors
<a name="API_agent-runtime_PutInvocationStep_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_PutInvocationStep_Examples"></a>

### Example request
<a name="API_agent-runtime_PutInvocationStep_Example_1"></a>

This example illustrates one usage of PutInvocationStep.

```
PUT bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/12345abc-1234-abcd-1234-abcdef123456/invocationSteps/ HTTP/1.1
Content-type: application/json

{
    "invocationIdentifier": "11111111-2222-3333-4444-555555555555",
    "invocationStepId": "abc-1234-abcd-1234-abcdef123456", 
    "invocationStepTime": "2023-08-08T12:00:00Z",
    "payload": {
        "contentBlocks": [
            {
                "text": "What's the weather in Seattle?"
            },
            {
                "image": {
                    "format": "png",
                    "source": {
                        "bytes": "base64_encoded_image_data"
                    }
                }
            }
        ]
    }
}
```

## See Also
<a name="API_agent-runtime_PutInvocationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/PutInvocationStep) 