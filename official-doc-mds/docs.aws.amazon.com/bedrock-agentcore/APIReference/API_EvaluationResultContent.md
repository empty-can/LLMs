

# EvaluationResultContent
<a name="API_EvaluationResultContent"></a>

 The comprehensive result of an evaluation containing the score, explanation, evaluator metadata, and execution details. Provides both quantitative ratings and qualitative insights about agent performance. 

## Contents
<a name="API_EvaluationResultContent_Contents"></a>

 ** context **   <a name="BedrockAgentCore-Type-EvaluationResultContent-context"></a>
 The contextual information associated with this evaluation result, including span context details that identify the specific traces and sessions that were evaluated.   
Type: [Context](API_Context.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** evaluatorArn **   <a name="BedrockAgentCore-Type-EvaluationResultContent-evaluatorArn"></a>
 The Amazon Resource Name (ARN) of the evaluator used to generate this result. For custom evaluators, this is the full ARN; for built-in evaluators, this follows the pattern `Builtin.{EvaluatorName}`.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/Builtin.[a-zA-Z0-9_-]+`   
Required: Yes

 ** evaluatorId **   <a name="BedrockAgentCore-Type-EvaluationResultContent-evaluatorId"></a>
 The unique identifier of the evaluator that produced this result. This matches the `evaluatorId` provided in the evaluation request and can be used to identify which evaluator generated specific results.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** evaluatorName **   <a name="BedrockAgentCore-Type-EvaluationResultContent-evaluatorName"></a>
 The human-readable name of the evaluator used for this evaluation. For built-in evaluators, this is the descriptive name (e.g., "Helpfulness", "Correctness"); for custom evaluators, this is the user-defined name.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9_]{0,47})`   
Required: Yes

 ** errorCode **   <a name="BedrockAgentCore-Type-EvaluationResultContent-errorCode"></a>
 The error code indicating the type of failure that occurred during evaluation. Used to programmatically identify and handle different categories of evaluation errors.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-EvaluationResultContent-errorMessage"></a>
 The error message describing what went wrong if the evaluation failed. Provides detailed information about evaluation failures to help diagnose and resolve issues with evaluator configuration or input data.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** explanation **   <a name="BedrockAgentCore-Type-EvaluationResultContent-explanation"></a>
 The detailed explanation provided by the evaluator describing the reasoning behind the assigned score. This qualitative feedback helps understand why specific ratings were given and provides actionable insights for improvement.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** ignoredReferenceInputFields **   <a name="BedrockAgentCore-Type-EvaluationResultContent-ignoredReferenceInputFields"></a>
 The list of reference input field names that were provided but not used by the evaluator. Helps identify which ground truth data was not consumed during evaluation.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** label **   <a name="BedrockAgentCore-Type-EvaluationResultContent-label"></a>
 The categorical label assigned by the evaluator when using a categorical rating scale. This provides a human-readable description of the evaluation result (e.g., "Excellent", "Good", "Poor") corresponding to the numerical value. For numerical scales, this field is optional and provides a natural language explanation of what the value means (e.g., value 0.5 = "Somewhat Helpful").   
Type: String  
Required: No

 ** tokenUsage **   <a name="BedrockAgentCore-Type-EvaluationResultContent-tokenUsage"></a>
 The token consumption statistics for this evaluation, including input tokens, output tokens, and total tokens used by the underlying language model during the evaluation process.   
Type: [TokenUsage](API_TokenUsage.md) object  
Required: No

 ** value **   <a name="BedrockAgentCore-Type-EvaluationResultContent-value"></a>
 The numerical score assigned by the evaluator according to its configured rating scale. For numerical scales, this is a decimal value within the defined range. This field is not allowed for categorical scales.   
Type: Double  
Required: No

## See Also
<a name="API_EvaluationResultContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationResultContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationResultContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationResultContent) 