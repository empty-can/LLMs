

# GetBatchEvaluation
<a name="API_GetBatchEvaluation"></a>

Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.

## Request Syntax
<a name="API_GetBatchEvaluation_RequestSyntax"></a>

```
GET /evaluations/batch-evaluate/{{batchEvaluationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBatchEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchEvaluationId](#API_GetBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-request-uri-batchEvaluationId"></a>
The unique identifier of the batch evaluation to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_GetBatchEvaluation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBatchEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchEvaluationArn": "string",
   "batchEvaluationId": "string",
   "batchEvaluationName": "string",
   "createdAt": "string",
   "dataSourceConfig": { ... },
   "description": "string",
   "errorDetails": [ "string" ],
   "evaluationResults": { 
      "evaluatorSummaries": [ 
         { 
            "evaluatorId": "string",
            "statistics": { 
               "averageScore": number
            },
            "totalEvaluated": number,
            "totalFailed": number
         }
      ],
      "numberOfSessionsCompleted": number,
      "numberOfSessionsFailed": number,
      "numberOfSessionsIgnored": number,
      "numberOfSessionsInProgress": number,
      "totalNumberOfSessions": number
   },
   "evaluators": [ 
      { 
         "evaluatorId": "string"
      }
   ],
   "executionSummaryResult": { 
      "executionSummaries": [ 
         { 
            "affectedSessionCount": number,
            "affectedSessions": [ 
               { 
                  "approachTaken": "string",
                  "finalOutcome": "string",
                  "sessionId": "string"
               }
            ],
            "clusterId": number,
            "description": "string",
            "name": "string"
         }
      ]
   },
   "failureAnalysisResult": { 
      "failures": [ 
         { 
            "affectedSessionCount": number,
            "clusterId": number,
            "description": "string",
            "name": "string",
            "subCategories": [ 
               { 
                  "affectedSessionCount": number,
                  "clusterId": number,
                  "description": "string",
                  "name": "string",
                  "rootCauses": [ 
                     { 
                        "affectedSessionCount": number,
                        "affectedSessions": [ 
                           { 
                              "explanation": "string",
                              "failureSpans": [ 
                                 { 
                                    "signals": [ 
                                       { 
                                          "category": "string",
                                          "confidence": number,
                                          "evidence": "string"
                                       }
                                    ],
                                    "spanId": "string",
                                    "traceId": "string"
                                 }
                              ],
                              "fixType": "string",
                              "recommendation": "string",
                              "sessionId": "string"
                           }
                        ],
                        "clusterId": number,
                        "name": "string",
                        "recommendation": "string",
                        "rootCause": "string"
                     }
                  ]
               }
            ]
         }
      ]
   },
   "insights": [ 
      { 
         "insightId": "string"
      }
   ],
   "kmsKeyArn": "string",
   "outputConfig": { ... },
   "status": "string",
   "updatedAt": "string",
   "userIntentResult": { 
      "userIntents": [ 
         { 
            "affectedSessionCount": number,
            "affectedSessions": [ 
               { 
                  "sessionId": "string",
                  "userMessages": [ "string" ]
               }
            ],
            "clusterId": number,
            "description": "string",
            "name": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetBatchEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluationArn](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the batch evaluation.  
Type: String

 ** [batchEvaluationId](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-batchEvaluationId"></a>
The unique identifier of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [batchEvaluationName](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-batchEvaluationName"></a>
The name of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [createdAt](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-createdAt"></a>
The timestamp when the batch evaluation was created.  
Type: Timestamp

 ** [dataSourceConfig](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-dataSourceConfig"></a>
The data source configuration specifying where agent traces are pulled from.  
Type: [DataSourceConfig](API_DataSourceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [description](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [errorDetails](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-errorDetails"></a>
The error details if the batch evaluation encountered failures.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [evaluationResults](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-evaluationResults"></a>
The aggregated evaluation results, including session completion counts and evaluator score summaries.  
Type: [EvaluationJobResults](API_EvaluationJobResults.md) object

 ** [evaluators](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-evaluators"></a>
The list of evaluators applied during the batch evaluation.  
Type: Array of [Evaluator](API_Evaluator.md) objects

 ** [executionSummaryResult](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-executionSummaryResult"></a>
The execution summary clustering results from insights, containing grouped execution patterns across evaluated sessions.  
Type: [ExecutionSummaryClusteringResultContent](API_ExecutionSummaryClusteringResultContent.md) object

 ** [failureAnalysisResult](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-failureAnalysisResult"></a>
The failure analysis results from insights, containing categorized failure clusters with root causes and recommendations.  
Type: [FailureAnalysisResultContent](API_FailureAnalysisResultContent.md) object

 ** [insights](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-insights"></a>
The list of insight analyses applied during the batch evaluation.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [kmsKeyArn](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [outputConfig](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-outputConfig"></a>
The output configuration specifying where evaluation results are written.  
Type: [OutputConfig](API_OutputConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-status"></a>
The current status of the batch evaluation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING` 

 ** [updatedAt](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-updatedAt"></a>
The timestamp when the batch evaluation was last updated.  
Type: Timestamp

 ** [userIntentResult](#API_GetBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-GetBatchEvaluation-response-userIntentResult"></a>
The user intent clustering results from insights, containing grouped user intents across evaluated sessions.  
Type: [UserIntentClusteringResultContent](API_UserIntentClusteringResultContent.md) object

## Errors
<a name="API_GetBatchEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_GetBatchEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetBatchEvaluation) 