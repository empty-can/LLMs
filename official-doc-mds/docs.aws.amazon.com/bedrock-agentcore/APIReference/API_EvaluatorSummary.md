

# EvaluatorSummary
<a name="API_EvaluatorSummary"></a>

Summary statistics for a single evaluator within a batch evaluation.

## Contents
<a name="API_EvaluatorSummary_Contents"></a>

 ** evaluatorId **   <a name="BedrockAgentCore-Type-EvaluatorSummary-evaluatorId"></a>
The unique identifier of the evaluator.  
Type: String  
Required: No

 ** statistics **   <a name="BedrockAgentCore-Type-EvaluatorSummary-statistics"></a>
The aggregated statistics for this evaluator.  
Type: [EvaluatorStatistics](API_EvaluatorStatistics.md) object  
Required: No

 ** totalEvaluated **   <a name="BedrockAgentCore-Type-EvaluatorSummary-totalEvaluated"></a>
The total number of sessions evaluated by this evaluator.  
Type: Integer  
Required: No

 ** totalFailed **   <a name="BedrockAgentCore-Type-EvaluatorSummary-totalFailed"></a>
The total number of sessions that failed evaluation by this evaluator.  
Type: Integer  
Required: No

## See Also
<a name="API_EvaluatorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluatorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluatorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluatorSummary) 