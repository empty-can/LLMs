

# UpdateOnlineEvaluationConfig
<a name="API_UpdateOnlineEvaluationConfig"></a>

 Updates an online evaluation configuration's settings, including rules, data sources, evaluators, and execution status. Changes take effect immediately for ongoing evaluations. 

## Request Syntax
<a name="API_UpdateOnlineEvaluationConfig_RequestSyntax"></a>

```
PUT /online-evaluation-configs/{{onlineEvaluationConfigId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "clusteringConfig": { 
      "frequencies": [ "{{string}}" ]
   },
   "dataSourceConfig": { ... },
   "description": "{{string}}",
   "evaluationExecutionRoleArn": "{{string}}",
   "evaluators": [ 
      { ... }
   ],
   "executionStatus": "{{string}}",
   "insights": [ 
      { 
         "insightId": "{{string}}"
      }
   ],
   "rule": { 
      "filters": [ 
         { 
            "key": "{{string}}",
            "operator": "{{string}}",
            "value": { ... }
         }
      ],
      "samplingConfig": { 
         "samplingPercentage": {{number}}
      },
      "sessionConfig": { 
         "sessionTimeoutMinutes": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateOnlineEvaluationConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [onlineEvaluationConfigId](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-uri-onlineEvaluationConfigId"></a>
 The unique identifier of the online evaluation configuration to update.   
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateOnlineEvaluationConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [clusteringConfig](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-clusteringConfig"></a>
The updated clustering configuration for periodic batch evaluation.  
Type: [ClusteringConfig](API_ClusteringConfig.md) object  
Required: No

 ** [dataSourceConfig](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-dataSourceConfig"></a>
 The updated data source configuration specifying CloudWatch log groups and service names to monitor.   
Type: [DataSourceConfig](API_DataSourceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [description](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-description"></a>
 The updated description of the online evaluation configuration.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `.+`   
Required: No

 ** [evaluationExecutionRoleArn](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-evaluationExecutionRoleArn"></a>
 The updated Amazon Resource Name (ARN) of the IAM role used for evaluation execution.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

 ** [evaluators](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-evaluators"></a>
 The updated list of evaluators to apply during online evaluation.   
Type: Array of [EvaluatorReference](API_EvaluatorReference.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [executionStatus](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-executionStatus"></a>
 The updated execution status to enable or disable the online evaluation.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [insights](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-insights"></a>
The updated list of insight types to run against agent sessions.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [rule](#API_UpdateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-request-rule"></a>
 The updated evaluation rule containing sampling configuration, filters, and session settings.   
Type: [Rule](API_Rule.md) object  
Required: No

## Response Syntax
<a name="API_UpdateOnlineEvaluationConfig_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "executionStatus": "string",
   "failureReason": "string",
   "onlineEvaluationConfigArn": "string",
   "onlineEvaluationConfigId": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateOnlineEvaluationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [executionStatus](#API_UpdateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-response-executionStatus"></a>
 The execution status indicating whether the online evaluation is currently running.   
Type: String  
Valid Values: `ENABLED | DISABLED` 

 ** [failureReason](#API_UpdateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-response-failureReason"></a>
 The reason for failure if the online evaluation configuration update or execution failed.   
Type: String

 ** [onlineEvaluationConfigArn](#API_UpdateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-response-onlineEvaluationConfigArn"></a>
 The Amazon Resource Name (ARN) of the updated online evaluation configuration.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [onlineEvaluationConfigId](#API_UpdateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-response-onlineEvaluationConfigId"></a>
 The unique identifier of the updated online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [status](#API_UpdateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-response-status"></a>
 The status of the online evaluation configuration.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ERROR` 

 ** [updatedAt](#API_UpdateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateOnlineEvaluationConfig-response-updatedAt"></a>
 The timestamp when the online evaluation configuration was last updated.   
Type: Timestamp

## Errors
<a name="API_UpdateOnlineEvaluationConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateOnlineEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateOnlineEvaluationConfig) 