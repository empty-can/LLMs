

# LlmAsAJudgeEvaluatorConfig
<a name="API_LlmAsAJudgeEvaluatorConfig"></a>

 The configuration for LLM-as-a-Judge evaluation that uses a language model to assess agent performance based on custom instructions and rating scales. 

## Contents
<a name="API_LlmAsAJudgeEvaluatorConfig_Contents"></a>

 ** instructions **   <a name="bedrockagentcorecontrol-Type-LlmAsAJudgeEvaluatorConfig-instructions"></a>
 The evaluation instructions that guide the language model in assessing agent performance, including criteria and evaluation guidelines.   
Type: String  
Required: Yes

 ** modelConfig **   <a name="bedrockagentcorecontrol-Type-LlmAsAJudgeEvaluatorConfig-modelConfig"></a>
 The model configuration that specifies which foundation model to use and how to configure it for evaluation.   
Type: [EvaluatorModelConfig](API_EvaluatorModelConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** ratingScale **   <a name="bedrockagentcorecontrol-Type-LlmAsAJudgeEvaluatorConfig-ratingScale"></a>
 The rating scale that defines how the evaluator should score agent performance, either numerical or categorical.   
Type: [RatingScale](API_RatingScale.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_LlmAsAJudgeEvaluatorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LlmAsAJudgeEvaluatorConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LlmAsAJudgeEvaluatorConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LlmAsAJudgeEvaluatorConfig) 