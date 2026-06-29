

# EvaluationJobResults
<a name="API_EvaluationJobResults"></a>

Aggregated results from a batch evaluation, including session completion counts and evaluator score summaries.

## Contents
<a name="API_EvaluationJobResults_Contents"></a>

 ** evaluatorSummaries **   <a name="BedrockAgentCore-Type-EvaluationJobResults-evaluatorSummaries"></a>
A list of per-evaluator summary statistics.  
Type: Array of [EvaluatorSummary](API_EvaluatorSummary.md) objects  
Required: No

 ** numberOfSessionsCompleted **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsCompleted"></a>
The number of sessions that have been successfully evaluated.  
Type: Integer  
Required: No

 ** numberOfSessionsFailed **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsFailed"></a>
The number of sessions that failed evaluation.  
Type: Integer  
Required: No

 ** numberOfSessionsIgnored **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsIgnored"></a>
The number of sessions that were ignored during evaluation.  
Type: Integer  
Required: No

 ** numberOfSessionsInProgress **   <a name="BedrockAgentCore-Type-EvaluationJobResults-numberOfSessionsInProgress"></a>
The number of sessions currently being evaluated.  
Type: Integer  
Required: No

 ** totalNumberOfSessions **   <a name="BedrockAgentCore-Type-EvaluationJobResults-totalNumberOfSessions"></a>
The total number of sessions included in the batch evaluation.  
Type: Integer  
Required: No

## See Also
<a name="API_EvaluationJobResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationJobResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationJobResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationJobResults) 