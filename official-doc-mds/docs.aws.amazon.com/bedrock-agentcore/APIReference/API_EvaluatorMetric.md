

# EvaluatorMetric
<a name="API_EvaluatorMetric"></a>

Statistical metrics for a single evaluator comparing control and treatment variants.

## Contents
<a name="API_EvaluatorMetric_Contents"></a>

 ** controlStats **   <a name="BedrockAgentCore-Type-EvaluatorMetric-controlStats"></a>
The statistics for the control variant.  
Type: [ControlStats](API_ControlStats.md) object  
Required: Yes

 ** evaluatorArn **   <a name="BedrockAgentCore-Type-EvaluatorMetric-evaluatorArn"></a>
The Amazon Resource Name (ARN) of the evaluator.  
Type: String  
Required: Yes

 ** variantResults **   <a name="BedrockAgentCore-Type-EvaluatorMetric-variantResults"></a>
The results for each treatment variant compared against the control.  
Type: Array of [VariantResult](API_VariantResult.md) objects  
Required: Yes

## See Also
<a name="API_EvaluatorMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluatorMetric) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluatorMetric) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluatorMetric) 