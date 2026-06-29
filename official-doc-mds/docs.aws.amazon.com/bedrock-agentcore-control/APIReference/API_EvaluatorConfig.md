

# EvaluatorConfig
<a name="API_EvaluatorConfig"></a>

 The configuration that defines how an evaluator assesses agent performance, including the evaluation method and parameters. 

## Contents
<a name="API_EvaluatorConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** codeBased **   <a name="bedrockagentcorecontrol-Type-EvaluatorConfig-codeBased"></a>
 Configuration for a code-based evaluator that uses a customer-managed Lambda function to programmatically assess agent performance.   
Type: [CodeBasedEvaluatorConfig](API_CodeBasedEvaluatorConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** llmAsAJudge **   <a name="bedrockagentcorecontrol-Type-EvaluatorConfig-llmAsAJudge"></a>
 The LLM-as-a-Judge configuration that uses a language model to evaluate agent performance based on custom instructions and rating scales.   
Type: [LlmAsAJudgeEvaluatorConfig](API_LlmAsAJudgeEvaluatorConfig.md) object  
Required: No

## See Also
<a name="API_EvaluatorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EvaluatorConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EvaluatorConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EvaluatorConfig) 