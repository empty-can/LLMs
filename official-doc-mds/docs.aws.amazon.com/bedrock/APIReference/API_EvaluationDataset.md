

# EvaluationDataset
<a name="API_EvaluationDataset"></a>

Used to specify the name of a built-in prompt dataset and optionally, the Amazon S3 bucket where a custom prompt dataset is saved.

## Contents
<a name="API_EvaluationDataset_Contents"></a>

 ** name **   <a name="bedrock-Type-EvaluationDataset-name"></a>
Used to specify supported built-in prompt datasets. Valid values are `Builtin.Bold`, `Builtin.BoolQ`, `Builtin.NaturalQuestions`, `Builtin.Gigaword`, `Builtin.RealToxicityPrompts`, `Builtin.TriviaQA`, `Builtin.T-Rex`, `Builtin.WomensEcommerceClothingReviews` and `Builtin.Wikitext2`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[0-9a-zA-Z-_.]+`   
Required: Yes

 ** datasetLocation **   <a name="bedrock-Type-EvaluationDataset-datasetLocation"></a>
For custom prompt datasets, you must specify the location in Amazon S3 where the prompt dataset is saved.  
Type: [EvaluationDatasetLocation](API_EvaluationDatasetLocation.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_EvaluationDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationDataset) 