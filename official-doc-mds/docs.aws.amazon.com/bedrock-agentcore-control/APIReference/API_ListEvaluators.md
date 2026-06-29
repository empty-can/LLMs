

# ListEvaluators
<a name="API_ListEvaluators"></a>

 Lists all available evaluators, including both builtin evaluators provided by the service and custom evaluators created by the user. 

## Request Syntax
<a name="API_ListEvaluators_RequestSyntax"></a>

```
POST /evaluators?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEvaluators_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListEvaluators_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListEvaluators-request-uri-maxResults"></a>
 The maximum number of evaluators to return in a single response.   
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListEvaluators_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListEvaluators-request-uri-nextToken"></a>
 The pagination token from a previous request to retrieve the next page of results. 

## Request Body
<a name="API_ListEvaluators_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEvaluators_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "evaluators": [ 
      { 
         "createdAt": number,
         "description": "string",
         "evaluatorArn": "string",
         "evaluatorId": "string",
         "evaluatorName": "string",
         "evaluatorType": "string",
         "kmsKeyArn": "string",
         "level": "string",
         "lockedForModification": boolean,
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEvaluators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evaluators](#API_ListEvaluators_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListEvaluators-response-evaluators"></a>
 The list of evaluator summaries containing basic information about each evaluator.   
Type: Array of [EvaluatorSummary](API_EvaluatorSummary.md) objects

 ** [nextToken](#API_ListEvaluators_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListEvaluators-response-nextToken"></a>
 The pagination token to use in a subsequent request to retrieve the next page of results.   
Type: String

## Errors
<a name="API_ListEvaluators_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListEvaluators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListEvaluators) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListEvaluators) 