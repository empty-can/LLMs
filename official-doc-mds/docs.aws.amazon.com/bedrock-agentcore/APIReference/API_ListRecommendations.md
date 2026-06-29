

# ListRecommendations
<a name="API_ListRecommendations"></a>

Lists all recommendations in the account, with optional filtering by status.

## Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
GET /recommendations?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{statusFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRecommendations_RequestSyntax) **   <a name="BedrockAgentCore-ListRecommendations-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListRecommendations_RequestSyntax) **   <a name="BedrockAgentCore-ListRecommendations-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [statusFilter](#API_ListRecommendations_RequestSyntax) **   <a name="BedrockAgentCore-ListRecommendations-request-uri-statusFilter"></a>
Optional filter to return only recommendations with the specified status.  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

## Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendationSummaries": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "name": "string",
         "recommendationArn": "string",
         "recommendationId": "string",
         "status": "string",
         "type": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="BedrockAgentCore-ListRecommendations-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [recommendationSummaries](#API_ListRecommendations_ResponseSyntax) **   <a name="BedrockAgentCore-ListRecommendations-response-recommendationSummaries"></a>
The list of recommendation summaries.  
Type: Array of [RecommendationSummary](API_RecommendationSummary.md) objects

## Errors
<a name="API_ListRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListRecommendations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListRecommendations) 