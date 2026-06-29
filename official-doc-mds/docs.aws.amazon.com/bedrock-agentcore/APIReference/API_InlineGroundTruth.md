

# InlineGroundTruth
<a name="API_InlineGroundTruth"></a>

Inline ground truth data containing assertions, expected trajectories, and per-turn expected responses.

## Contents
<a name="API_InlineGroundTruth_Contents"></a>

 ** assertions **   <a name="BedrockAgentCore-Type-InlineGroundTruth-assertions"></a>
Assertions for evaluation, reuses common model EvaluationContentList.  
Type: Array of [EvaluationContent](API_EvaluationContent.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** expectedTrajectory **   <a name="BedrockAgentCore-Type-InlineGroundTruth-expectedTrajectory"></a>
The expected tool call sequence for trajectory evaluation.  
Type: [EvaluationExpectedTrajectory](API_EvaluationExpectedTrajectory.md) object  
Required: No

 ** turns **   <a name="BedrockAgentCore-Type-InlineGroundTruth-turns"></a>
A list of per-turn ground truth data, each containing an input prompt and expected response.  
Type: Array of [GroundTruthTurn](API_GroundTruthTurn.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## See Also
<a name="API_InlineGroundTruth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InlineGroundTruth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InlineGroundTruth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InlineGroundTruth) 