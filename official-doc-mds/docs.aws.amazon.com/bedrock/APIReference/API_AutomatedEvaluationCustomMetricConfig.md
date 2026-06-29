

# AutomatedEvaluationCustomMetricConfig
<a name="API_AutomatedEvaluationCustomMetricConfig"></a>

Defines the configuration of custom metrics to be used in an evaluation job. To learn more about using custom metrics in Amazon Bedrock evaluation jobs, see [Create a prompt for a custom metrics (LLM-as-a-judge model evaluations)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html) and [Create a prompt for a custom metrics (RAG evaluations)](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-evaluation-custom-metrics-prompt-formats.html).

## Contents
<a name="API_AutomatedEvaluationCustomMetricConfig_Contents"></a>

 ** customMetrics **   <a name="bedrock-Type-AutomatedEvaluationCustomMetricConfig-customMetrics"></a>
Defines a list of custom metrics to be used in an Amazon Bedrock evaluation job.  
Type: Array of [AutomatedEvaluationCustomMetricSource](API_AutomatedEvaluationCustomMetricSource.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

 ** evaluatorModelConfig **   <a name="bedrock-Type-AutomatedEvaluationCustomMetricConfig-evaluatorModelConfig"></a>
Configuration of the evaluator model you want to use to evaluate custom metrics in an Amazon Bedrock evaluation job.  
Type: [CustomMetricEvaluatorModelConfig](API_CustomMetricEvaluatorModelConfig.md) object  
Required: Yes

## See Also
<a name="API_AutomatedEvaluationCustomMetricConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedEvaluationCustomMetricConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedEvaluationCustomMetricConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedEvaluationCustomMetricConfig) 