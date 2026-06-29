

# CustomMetricDefinition
<a name="API_CustomMetricDefinition"></a>

The definition of a custom metric for use in an Amazon Bedrock evaluation job. A custom metric definition includes a metric name, prompt (instructions) and optionally, a rating scale. Your prompt must include a task description and input variables. The required input variables are different for model-as-a-judge and RAG evaluations.

For more information about how to define a custom metric in Amazon Bedrock, see [Create a prompt for a custom metrics (LLM-as-a-judge model evaluations)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html) and [Create a prompt for a custom metrics (RAG evaluations)](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-evaluation-custom-metrics-prompt-formats.html).

## Contents
<a name="API_CustomMetricDefinition_Contents"></a>

 ** instructions **   <a name="bedrock-Type-CustomMetricDefinition-instructions"></a>
The prompt for a custom metric that instructs the evaluator model how to rate the model or RAG source under evaluation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5000.  
Required: Yes

 ** name **   <a name="bedrock-Type-CustomMetricDefinition-name"></a>
The name for a custom metric. Names must be unique in your AWS region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[0-9a-zA-Z-_.]+`   
Required: Yes

 ** ratingScale **   <a name="bedrock-Type-CustomMetricDefinition-ratingScale"></a>
Defines the rating scale to be used for a custom metric. We recommend that you always define a ratings scale when creating a custom metric. If you don't define a scale, Amazon Bedrock won't be able to visually display the results of the evaluation in the console or calculate average values of numerical scores. For more information on specifying a rating scale, see [Specifying an output schema (rating scale)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html#model-evaluation-custom-metrics-prompt-formats-schema).  
Type: Array of [RatingScaleItem](API_RatingScaleItem.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

## See Also
<a name="API_CustomMetricDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomMetricDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomMetricDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomMetricDefinition) 