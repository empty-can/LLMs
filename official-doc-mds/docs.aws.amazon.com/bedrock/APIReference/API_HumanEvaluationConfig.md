

# HumanEvaluationConfig
<a name="API_HumanEvaluationConfig"></a>

Specifies the custom metrics, how tasks will be rated, the flow definition ARN, and your custom prompt datasets. Model evaluation jobs use human workers *only* support the use of custom prompt datasets. To learn more about custom prompt datasets and the required format, see [Custom prompt datasets](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets-custom.html).

When you create custom metrics in `HumanEvaluationCustomMetric` you must specify the metric's `name`. The list of `names` specified in the `HumanEvaluationCustomMetric` array, must match the `metricNames` array of strings specified in `EvaluationDatasetMetricConfig`. For example, if in the `HumanEvaluationCustomMetric` array your specified the names `"accuracy", "toxicity", "readability"` as custom metrics *then* the `metricNames` array would need to look like the following `["accuracy", "toxicity", "readability"]` in `EvaluationDatasetMetricConfig`.

## Contents
<a name="API_HumanEvaluationConfig_Contents"></a>

 ** datasetMetricConfigs **   <a name="bedrock-Type-HumanEvaluationConfig-datasetMetricConfigs"></a>
Use to specify the metrics, task, and prompt dataset to be used in your model evaluation job.  
Type: Array of [EvaluationDatasetMetricConfig](API_EvaluationDatasetMetricConfig.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** customMetrics **   <a name="bedrock-Type-HumanEvaluationConfig-customMetrics"></a>
A `HumanEvaluationCustomMetric` object. It contains the names the metrics, how the metrics are to be evaluated, an optional description.  
Type: Array of [HumanEvaluationCustomMetric](API_HumanEvaluationCustomMetric.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** humanWorkflowConfig **   <a name="bedrock-Type-HumanEvaluationConfig-humanWorkflowConfig"></a>
The parameters of the human workflow.  
Type: [HumanWorkflowConfig](API_HumanWorkflowConfig.md) object  
Required: No

## See Also
<a name="API_HumanEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/HumanEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/HumanEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/HumanEvaluationConfig) 