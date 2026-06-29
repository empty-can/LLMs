

# CreateOnlineEvaluationConfig
<a name="API_CreateOnlineEvaluationConfig"></a>

 Creates an online evaluation configuration for continuous monitoring of agent performance. Online evaluation automatically samples live traffic from CloudWatch logs at specified rates and applies evaluators to assess agent quality in production. 

## Request Syntax
<a name="API_CreateOnlineEvaluationConfig_RequestSyntax"></a>

```
POST /online-evaluation-configs/create HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "clusteringConfig": { 
      "frequencies": [ "{{string}}" ]
   },
   "dataSourceConfig": { ... },
   "description": "{{string}}",
   "enableOnCreate": {{boolean}},
   "evaluationExecutionRoleArn": "{{string}}",
   "evaluators": [ 
      { ... }
   ],
   "insights": [ 
      { 
         "insightId": "{{string}}"
      }
   ],
   "onlineEvaluationConfigName": "{{string}}",
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
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateOnlineEvaluationConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOnlineEvaluationConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [clusteringConfig](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-clusteringConfig"></a>
Configuration for periodic batch evaluation clustering of insight results.  
Type: [ClusteringConfig](API_ClusteringConfig.md) object  
Required: No

 ** [dataSourceConfig](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-dataSourceConfig"></a>
 The data source configuration that specifies CloudWatch log groups and service names to monitor for agent traces.   
Type: [DataSourceConfig](API_DataSourceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [description](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-description"></a>
 The description of the online evaluation configuration that explains its monitoring purpose and scope.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `.+`   
Required: No

 ** [enableOnCreate](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-enableOnCreate"></a>
 Whether to enable the online evaluation configuration immediately upon creation. If true, evaluation begins automatically.   
Type: Boolean  
Required: Yes

 ** [evaluationExecutionRoleArn](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-evaluationExecutionRoleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role that grants permissions to read from CloudWatch logs, write evaluation results, and invoke Amazon Bedrock models for evaluation. If the configuration references evaluators encrypted with a customer managed AWS KMS key, this role must also have `kms:Decrypt` permission on the KMS key. The service validates this permission at configuration creation time. For more information, see [Encryption at rest for AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [evaluators](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-evaluators"></a>
 The list of evaluators to apply during online evaluation. Can include both built-in evaluators and custom evaluators created with `CreateEvaluator`.   
Type: Array of [EvaluatorReference](API_EvaluatorReference.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [insights](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-insights"></a>
The list of insight types to run against agent sessions.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [onlineEvaluationConfigName](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-onlineEvaluationConfigName"></a>
 The name of the online evaluation configuration. Must be unique within your account.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [rule](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-rule"></a>
 The evaluation rule that defines sampling configuration, filters, and session detection settings for the online evaluation.   
Type: [Rule](API_Rule.md) object  
Required: Yes

 ** [tags](#API_CreateOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-request-tags"></a>
A map of tag keys and values to assign to an AgentCore Online Evaluation Config. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateOnlineEvaluationConfig_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": number,
   "executionStatus": "string",
   "failureReason": "string",
   "onlineEvaluationConfigArn": "string",
   "onlineEvaluationConfigId": "string",
   "outputConfig": { 
      "cloudWatchConfig": { 
         "logGroupName": "string"
      }
   },
   "status": "string"
}
```

## Response Elements
<a name="API_CreateOnlineEvaluationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-createdAt"></a>
 The timestamp when the online evaluation configuration was created.   
Type: Timestamp

 ** [executionStatus](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-executionStatus"></a>
 The execution status indicating whether the online evaluation is currently running.   
Type: String  
Valid Values: `ENABLED | DISABLED` 

 ** [failureReason](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-failureReason"></a>
 The reason for failure if the online evaluation configuration creation or execution failed.   
Type: String

 ** [onlineEvaluationConfigArn](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-onlineEvaluationConfigArn"></a>
 The Amazon Resource Name (ARN) of the created online evaluation configuration.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [onlineEvaluationConfigId](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-onlineEvaluationConfigId"></a>
 The unique identifier of the created online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [outputConfig](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-outputConfig"></a>
 The configuration that specifies where evaluation results should be written for monitoring and analysis.   
Type: [OutputConfig](API_OutputConfig.md) object

 ** [status](#API_CreateOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateOnlineEvaluationConfig-response-status"></a>
 The status of the online evaluation configuration.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ERROR` 

## Errors
<a name="API_CreateOnlineEvaluationConfig_Errors"></a>

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
<a name="API_CreateOnlineEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig) 