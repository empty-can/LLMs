

# EvaluationDatasetMetricConfig
<a name="API_EvaluationDatasetMetricConfig"></a>

Defines the prompt datasets, built-in metric names and custom metric names, and the task type.

## Contents
<a name="API_EvaluationDatasetMetricConfig_Contents"></a>

 ** dataset **   <a name="bedrock-Type-EvaluationDatasetMetricConfig-dataset"></a>
Specifies the prompt dataset.  
Type: [EvaluationDataset](API_EvaluationDataset.md) object  
Required: Yes

 ** metricNames **   <a name="bedrock-Type-EvaluationDatasetMetricConfig-metricNames"></a>
The names of the metrics you want to use for your evaluation job.  
For knowledge base evaluation jobs that evaluate retrieval only, valid values are "`Builtin.ContextRelevance`", "`Builtin.ContextCoverage`".  
For knowledge base evaluation jobs that evaluate retrieval with response generation, valid values are "`Builtin.Correctness`", "`Builtin.Completeness`", "`Builtin.Helpfulness`", "`Builtin.LogicalCoherence`", "`Builtin.Faithfulness`", "`Builtin.Harmfulness`", "`Builtin.Stereotyping`", "`Builtin.Refusal`".  
For automated model evaluation jobs, valid values are "`Builtin.Accuracy`", "`Builtin.Robustness`", and "`Builtin.Toxicity`". In model evaluation jobs that use a LLM as judge you can specify "`Builtin.Correctness`", "`Builtin.Completeness"`, "`Builtin.Faithfulness"`, "`Builtin.Helpfulness`", "`Builtin.Coherence`", "`Builtin.Relevance`", "`Builtin.FollowingInstructions`", "`Builtin.ProfessionalStyleAndTone`", You can also specify the following responsible AI related metrics only for model evaluation job that use a LLM as judge "`Builtin.Harmfulness`", "`Builtin.Stereotyping`", and "`Builtin.Refusal`".  
For human-based model evaluation jobs, the list of strings must match the `name` parameter specified in `HumanEvaluationCustomMetric`.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[0-9a-zA-Z-_.]+`   
Required: Yes

 ** taskType **   <a name="bedrock-Type-EvaluationDatasetMetricConfig-taskType"></a>
The the type of task you want to evaluate for your evaluation job. This applies only to model evaluation jobs and is ignored for knowledge base evaluation jobs.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-Za-z0-9]+`   
Valid Values: `Summarization | Classification | QuestionAndAnswer | Generation | Custom`   
Required: Yes

## See Also
<a name="API_EvaluationDatasetMetricConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationDatasetMetricConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationDatasetMetricConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationDatasetMetricConfig) 