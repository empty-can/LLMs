

# HumanEvaluationCustomMetric
<a name="API_HumanEvaluationCustomMetric"></a>

In a model evaluation job that uses human workers you must define the name of the metric, and how you want that metric rated `ratingMethod`, and an optional description of the metric.

## Contents
<a name="API_HumanEvaluationCustomMetric_Contents"></a>

 ** name **   <a name="bedrock-Type-HumanEvaluationCustomMetric-name"></a>
The name of the metric. Your human evaluators will see this name in the evaluation UI.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[0-9a-zA-Z-_.]+`   
Required: Yes

 ** ratingMethod **   <a name="bedrock-Type-HumanEvaluationCustomMetric-ratingMethod"></a>
Choose how you want your human workers to evaluation your model. Valid values for rating methods are `ThumbsUpDown`, `IndividualLikertScale`,`ComparisonLikertScale`, `ComparisonChoice`, and `ComparisonRank`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9a-zA-Z-_]+`   
Required: Yes

 ** description **   <a name="bedrock-Type-HumanEvaluationCustomMetric-description"></a>
An optional description of the metric. Use this parameter to provide more details about the metric.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `.+`   
Required: No

## See Also
<a name="API_HumanEvaluationCustomMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/HumanEvaluationCustomMetric) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/HumanEvaluationCustomMetric) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/HumanEvaluationCustomMetric) 