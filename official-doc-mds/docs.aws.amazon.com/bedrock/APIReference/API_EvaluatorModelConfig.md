

# EvaluatorModelConfig
<a name="API_EvaluatorModelConfig"></a>

Specifies the model configuration for the evaluator model. `EvaluatorModelConfig` is required for evaluation jobs that use a knowledge base or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.

## Contents
<a name="API_EvaluatorModelConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bedrockEvaluatorModels **   <a name="bedrock-Type-EvaluatorModelConfig-bedrockEvaluatorModels"></a>
The evaluator model used in knowledge base evaluation job or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.  
Type: Array of [BedrockEvaluatorModel](API_BedrockEvaluatorModel.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

## See Also
<a name="API_EvaluatorModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluatorModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluatorModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluatorModelConfig) 