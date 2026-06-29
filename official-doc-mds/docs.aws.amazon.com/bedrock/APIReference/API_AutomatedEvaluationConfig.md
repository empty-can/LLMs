

# AutomatedEvaluationConfig
<a name="API_AutomatedEvaluationConfig"></a>

The configuration details of an automated evaluation job. The `EvaluationDatasetMetricConfig` object is used to specify the prompt datasets, task type, and metric names.

## Contents
<a name="API_AutomatedEvaluationConfig_Contents"></a>

 ** datasetMetricConfigs **   <a name="bedrock-Type-AutomatedEvaluationConfig-datasetMetricConfigs"></a>
Configuration details of the prompt datasets and metrics you want to use for your evaluation job.  
Type: Array of [EvaluationDatasetMetricConfig](API_EvaluationDatasetMetricConfig.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** customMetricConfig **   <a name="bedrock-Type-AutomatedEvaluationConfig-customMetricConfig"></a>
Defines the configuration of custom metrics to be used in an evaluation job.  
Type: [AutomatedEvaluationCustomMetricConfig](API_AutomatedEvaluationCustomMetricConfig.md) object  
Required: No

 ** evaluatorModelConfig **   <a name="bedrock-Type-AutomatedEvaluationConfig-evaluatorModelConfig"></a>
Contains the evaluator model configuration details. `EvaluatorModelConfig` is required for evaluation jobs that use a knowledge base or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.  
Type: [EvaluatorModelConfig](API_EvaluatorModelConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_AutomatedEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedEvaluationConfig) 