

# ListOnlineEvaluationConfigs
<a name="API_ListOnlineEvaluationConfigs"></a>

 Lists all online evaluation configurations in the account, providing summary information about each configuration's status and settings. 

## Request Syntax
<a name="API_ListOnlineEvaluationConfigs_RequestSyntax"></a>

```
POST /online-evaluation-configs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOnlineEvaluationConfigs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListOnlineEvaluationConfigs_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListOnlineEvaluationConfigs-request-uri-maxResults"></a>
 The maximum number of online evaluation configurations to return in a single response.   
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListOnlineEvaluationConfigs_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListOnlineEvaluationConfigs-request-uri-nextToken"></a>
 The pagination token from a previous request to retrieve the next page of results. 

## Request Body
<a name="API_ListOnlineEvaluationConfigs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOnlineEvaluationConfigs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "onlineEvaluationConfigs": [ 
      { 
         "clusteringConfig": { 
            "frequencies": [ "string" ]
         },
         "createdAt": number,
         "description": "string",
         "executionStatus": "string",
         "failureReason": "string",
         "insights": [ 
            { 
               "insightId": "string"
            }
         ],
         "onlineEvaluationConfigArn": "string",
         "onlineEvaluationConfigId": "string",
         "onlineEvaluationConfigName": "string",
         "status": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListOnlineEvaluationConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOnlineEvaluationConfigs_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListOnlineEvaluationConfigs-response-nextToken"></a>
 The pagination token to use in a subsequent request to retrieve the next page of results.   
Type: String

 ** [onlineEvaluationConfigs](#API_ListOnlineEvaluationConfigs_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListOnlineEvaluationConfigs-response-onlineEvaluationConfigs"></a>
 The list of online evaluation configuration summaries containing basic information about each configuration.   
Type: Array of [OnlineEvaluationConfigSummary](API_OnlineEvaluationConfigSummary.md) objects

## Errors
<a name="API_ListOnlineEvaluationConfigs_Errors"></a>

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
<a name="API_ListOnlineEvaluationConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListOnlineEvaluationConfigs) 