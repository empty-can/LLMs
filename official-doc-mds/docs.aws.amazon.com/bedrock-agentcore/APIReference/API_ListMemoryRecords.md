

# ListMemoryRecords
<a name="API_ListMemoryRecords"></a>

Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:ListMemoryRecords` permission.

## Request Syntax
<a name="API_ListMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/memoryRecords HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "memoryStrategyId": "{{string}}",
   "metadataFilters": [ 
      { 
         "left": { ... },
         "operator": "{{string}}",
         "right": { ... }
      }
   ],
   "namespace": "{{string}}",
   "namespacePath": "{{string}}",
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource for which to list memory records.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_ListMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [memoryStrategyId](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-memoryStrategyId"></a>
The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** [metadataFilters](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-metadataFilters"></a>
A list of metadata filter expressions to scope the returned memory records.  
Type: Array of [MemoryMetadataFilterExpression](API_MemoryMetadataFilterExpression.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

 ** [namespace](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-namespace"></a>
The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either `namespace` or `namespacePath` is required.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** [namespacePath](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-namespacePath"></a>
Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either `namespace` or `namespacePath` is required.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

 ** [nextToken](#API_ListMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memoryRecordSummaries": [ 
      { 
         "content": { ... },
         "createdAt": number,
         "memoryRecordId": "string",
         "memoryStrategyId": "string",
         "metadata": { 
            "string" : { ... }
         },
         "namespaces": [ "string" ],
         "score": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memoryRecordSummaries](#API_ListMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-response-memoryRecordSummaries"></a>
The list of memory record summaries that match the specified criteria.  
Type: Array of [MemoryRecordSummary](API_MemoryRecordSummary.md) objects

 ** [nextToken](#API_ListMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-ListMemoryRecords-response-nextToken"></a>
The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.  
Type: String

## Errors
<a name="API_ListMemoryRecords_Errors"></a>

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
<a name="API_ListMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListMemoryRecords) 