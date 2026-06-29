

# BatchEvaluationSummary
<a name="API_BatchEvaluationSummary"></a>

Summary representation for list responses.

## Contents
<a name="API_BatchEvaluationSummary_Contents"></a>

 ** batchEvaluationArn **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the batch evaluation.  
Type: String  
Required: Yes

 ** batchEvaluationId **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-batchEvaluationId"></a>
The unique identifier of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** batchEvaluationName **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-batchEvaluationName"></a>
The name of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-createdAt"></a>
The timestamp when the batch evaluation was created.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-status"></a>
The current status of the batch evaluation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING`   
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Required: No

 ** errorDetails **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-errorDetails"></a>
The error details if the batch evaluation encountered failures.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Required: No

 ** evaluationResults **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-evaluationResults"></a>
The aggregated evaluation results.  
Type: [EvaluationJobResults](API_EvaluationJobResults.md) object  
Required: No

 ** evaluators **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-evaluators"></a>
The list of evaluators applied during the batch evaluation.  
Type: Array of [Evaluator](API_Evaluator.md) objects  
Required: No

 ** insights **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-insights"></a>
The list of insight analyses applied during the batch evaluation.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** kmsKeyArn **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** updatedAt **   <a name="BedrockAgentCore-Type-BatchEvaluationSummary-updatedAt"></a>
The timestamp when the batch evaluation was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_BatchEvaluationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchEvaluationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchEvaluationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchEvaluationSummary) 