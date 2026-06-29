

# GetOnlineEvaluationConfig
<a name="API_GetOnlineEvaluationConfig"></a>

 Retrieves detailed information about an online evaluation configuration, including its rules, data sources, evaluators, and execution status. 

## Request Syntax
<a name="API_GetOnlineEvaluationConfig_RequestSyntax"></a>

```
GET /online-evaluation-configs/{{onlineEvaluationConfigId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOnlineEvaluationConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [onlineEvaluationConfigId](#API_GetOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-request-uri-onlineEvaluationConfigId"></a>
 The unique identifier of the online evaluation configuration to retrieve.   
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_GetOnlineEvaluationConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOnlineEvaluationConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clusteringConfig": { 
      "frequencies": [ "string" ]
   },
   "createdAt": number,
   "dataSourceConfig": { ... },
   "description": "string",
   "evaluationExecutionRoleArn": "string",
   "evaluators": [ 
      { ... }
   ],
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
   "outputConfig": { 
      "cloudWatchConfig": { 
         "logGroupName": "string"
      }
   },
   "rule": { 
      "filters": [ 
         { 
            "key": "string",
            "operator": "string",
            "value": { ... }
         }
      ],
      "samplingConfig": { 
         "samplingPercentage": number
      },
      "sessionConfig": { 
         "sessionTimeoutMinutes": number
      }
   },
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetOnlineEvaluationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusteringConfig](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-clusteringConfig"></a>
The clustering configuration for periodic batch evaluation.  
Type: [ClusteringConfig](API_ClusteringConfig.md) object

 ** [createdAt](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-createdAt"></a>
 The timestamp when the online evaluation configuration was created.   
Type: Timestamp

 ** [dataSourceConfig](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-dataSourceConfig"></a>
 The data source configuration specifying CloudWatch log groups and service names to monitor.   
Type: [DataSourceConfig](API_DataSourceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [description](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-description"></a>
 The description of the online evaluation configuration.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `.+` 

 ** [evaluationExecutionRoleArn](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-evaluationExecutionRoleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role used for evaluation execution.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [evaluators](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-evaluators"></a>
 The list of evaluators applied during online evaluation.   
Type: Array of [EvaluatorReference](API_EvaluatorReference.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [executionStatus](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-executionStatus"></a>
 The execution status indicating whether the online evaluation is currently running.   
Type: String  
Valid Values: `ENABLED | DISABLED` 

 ** [failureReason](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-failureReason"></a>
 The reason for failure if the online evaluation configuration execution failed.   
Type: String

 ** [insights](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-insights"></a>
The list of insight types configured for this evaluation.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [onlineEvaluationConfigArn](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-onlineEvaluationConfigArn"></a>
 The Amazon Resource Name (ARN) of the online evaluation configuration.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [onlineEvaluationConfigId](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-onlineEvaluationConfigId"></a>
 The unique identifier of the online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [onlineEvaluationConfigName](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-onlineEvaluationConfigName"></a>
 The name of the online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [outputConfig](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-outputConfig"></a>
 The output configuration specifying where evaluation results are written.   
Type: [OutputConfig](API_OutputConfig.md) object

 ** [rule](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-rule"></a>
 The evaluation rule containing sampling configuration, filters, and session settings.   
Type: [Rule](API_Rule.md) object

 ** [status](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-status"></a>
 The status of the online evaluation configuration.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ERROR` 

 ** [updatedAt](#API_GetOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetOnlineEvaluationConfig-response-updatedAt"></a>
 The timestamp when the online evaluation configuration was last updated.   
Type: Timestamp

## Errors
<a name="API_GetOnlineEvaluationConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetOnlineEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig) 