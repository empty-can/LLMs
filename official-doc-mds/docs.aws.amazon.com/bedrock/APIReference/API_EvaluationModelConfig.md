

# EvaluationModelConfig
<a name="API_EvaluationModelConfig"></a>

Defines the models used in the model evaluation job.

## Contents
<a name="API_EvaluationModelConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bedrockModel **   <a name="bedrock-Type-EvaluationModelConfig-bedrockModel"></a>
Defines the Amazon Bedrock model or inference profile and inference parameters you want used.  
Type: [EvaluationBedrockModel](API_EvaluationBedrockModel.md) object  
Required: No

 ** precomputedInferenceSource **   <a name="bedrock-Type-EvaluationModelConfig-precomputedInferenceSource"></a>
Defines the model used to generate inference response data for a model evaluation job where you provide your own inference response data.  
Type: [EvaluationPrecomputedInferenceSource](API_EvaluationPrecomputedInferenceSource.md) object  
Required: No

## See Also
<a name="API_EvaluationModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationModelConfig) 