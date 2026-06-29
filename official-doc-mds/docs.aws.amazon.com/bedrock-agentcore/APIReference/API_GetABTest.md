

# GetABTest
<a name="API_GetABTest"></a>

Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.

## Request Syntax
<a name="API_GetABTest_RequestSyntax"></a>

```
GET /ab-tests/{{abTestId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetABTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [abTestId](#API_GetABTest_RequestSyntax) **   <a name="BedrockAgentCore-GetABTest-request-uri-abTestId"></a>
The unique identifier of the A/B test to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_GetABTest_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetABTest_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "createdAt": number,
   "currentRunId": "string",
   "description": "string",
   "errorDetails": [ "string" ],
   "evaluationConfig": { ... },
   "executionStatus": "string",
   "gatewayArn": "string",
   "gatewayFilter": { 
      "targetPaths": [ "string" ]
   },
   "maxDurationExpiresAt": number,
   "name": "string",
   "results": { 
      "analysisTimestamp": number,
      "evaluatorMetrics": [ 
         { 
            "controlStats": { 
               "mean": number,
               "sampleSize": number,
               "variantName": "string"
            },
            "evaluatorArn": "string",
            "variantResults": [ 
               { 
                  "absoluteChange": number,
                  "confidenceInterval": { 
                     "lower": number,
                     "upper": number
                  },
                  "isSignificant": boolean,
                  "mean": number,
                  "percentChange": number,
                  "pValue": number,
                  "sampleSize": number,
                  "variantName": "string"
               }
            ]
         }
      ]
   },
   "roleArn": "string",
   "startedAt": number,
   "status": "string",
   "stoppedAt": number,
   "updatedAt": number,
   "variants": [ 
      { 
         "name": "string",
         "variantConfiguration": { 
            "configurationBundle": { 
               "bundleArn": "string",
               "bundleVersion": "string"
            },
            "target": { 
               "name": "string"
            }
         },
         "weight": number
      }
   ]
}
```

## Response Elements
<a name="API_GetABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-abTestId"></a>
The unique identifier of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-createdAt"></a>
The timestamp when the A/B test was created.  
Type: Timestamp

 ** [currentRunId](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-currentRunId"></a>
The identifier of the current run of the A/B test.  
Type: String

 ** [description](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-description"></a>
The description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [errorDetails](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-errorDetails"></a>
The error details if the A/B test encountered failures.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [evaluationConfig](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-evaluationConfig"></a>
The evaluation configuration for measuring variant performance.  
Type: [ABTestEvaluationConfig](API_ABTestEvaluationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [executionStatus](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-executionStatus"></a>
The execution status indicating whether the A/B test is currently running.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED` 

 ** [gatewayArn](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway used for traffic splitting.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [gatewayFilter](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-gatewayFilter"></a>
The gateway filter restricting which target paths are included.  
Type: [GatewayFilter](API_GatewayFilter.md) object

 ** [maxDurationExpiresAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-maxDurationExpiresAt"></a>
The timestamp when the A/B test will automatically expire.  
Type: Timestamp

 ** [name](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-name"></a>
The name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [results](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-results"></a>
The statistical results of the A/B test, including per-evaluator metrics and significance analysis.  
Type: [ABTestResults](API_ABTestResults.md) object

 ** [roleArn](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-roleArn"></a>
The IAM role ARN used by the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [startedAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-startedAt"></a>
The timestamp when the A/B test was started.  
Type: Timestamp

 ** [status](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-status"></a>
The current status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

 ** [stoppedAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-stoppedAt"></a>
The timestamp when the A/B test was stopped.  
Type: Timestamp

 ** [updatedAt](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-updatedAt"></a>
The timestamp when the A/B test was last updated.  
Type: Timestamp

 ** [variants](#API_GetABTest_ResponseSyntax) **   <a name="BedrockAgentCore-GetABTest-response-variants"></a>
The list of variants in the A/B test.  
Type: Array of [Variant](API_Variant.md) objects  
Array Members: Fixed number of 2 items.

## Errors
<a name="API_GetABTest_Errors"></a>

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
<a name="API_GetABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetABTest) 