

# ListMemoryExtractionJobs
<a name="API_ListMemoryExtractionJobs"></a>

Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.

To use this operation, you must have the `bedrock-agentcore:ListMemoryExtractionJobs` permission.

## Request Syntax
<a name="API_ListMemoryExtractionJobs_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/extractionJobs HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "actorId": "{{string}}",
      "sessionId": "{{string}}",
      "status": "{{string}}",
      "strategyId": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMemoryExtractionJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-uri-memoryId"></a>
The unique identifier of the memory to list extraction jobs for.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_ListMemoryExtractionJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-filter"></a>
Filter criteria to apply when listing extraction jobs.  
Type: [ExtractionJobFilterInput](API_ExtractionJobFilterInput.md) object  
Required: No

 ** [maxResults](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [nextToken](#API_ListMemoryExtractionJobs_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListMemoryExtractionJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [ 
      { 
         "actorId": "string",
         "failureReason": "string",
         "jobID": "string",
         "messages": { ... },
         "sessionId": "string",
         "status": "string",
         "strategyId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemoryExtractionJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListMemoryExtractionJobs_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-response-jobs"></a>
List of extraction job metadata matching the specified criteria.  
Type: Array of [ExtractionJobMetadata](API_ExtractionJobMetadata.md) objects

 ** [nextToken](#API_ListMemoryExtractionJobs_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryExtractionJobs-response-nextToken"></a>
Token to retrieve the next page of results, if available.  
Type: String

## Errors
<a name="API_ListMemoryExtractionJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

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
<a name="API_ListMemoryExtractionJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListMemoryExtractionJobs) 