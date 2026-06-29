

# ListMemories
<a name="API_ListMemories"></a>

Lists the available Amazon Bedrock AgentCore Memory resources in the current AWS Region.

## Request Syntax
<a name="API_ListMemories_RequestSyntax"></a>

```
POST /memories/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMemories_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMemories_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListMemories_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListMemories-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListMemories_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListMemories-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListMemories_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memories": [ 
      { 
         "arn": "string",
         "createdAt": number,
         "id": "string",
         "managedByResourceArn": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memories](#API_ListMemories_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListMemories-response-memories"></a>
The list of AgentCore Memory resource summaries.  
Type: Array of [MemorySummary](API_MemorySummary.md) objects

 ** [nextToken](#API_ListMemories_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListMemories-response-nextToken"></a>
A token to retrieve the next page of results.  
Type: String

## Errors
<a name="API_ListMemories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ThrottledException **   
API rate limit has been exceeded.  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListMemories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListMemories) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListMemories) 