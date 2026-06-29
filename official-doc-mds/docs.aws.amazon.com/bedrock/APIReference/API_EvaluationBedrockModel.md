

# EvaluationBedrockModel
<a name="API_EvaluationBedrockModel"></a>

Contains the ARN of the Amazon Bedrock model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) specified in your evaluation job. Each Amazon Bedrock model supports different `inferenceParams`. To learn more about supported inference parameters for Amazon Bedrock models, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

The `inferenceParams` are specified using JSON. To successfully insert JSON as string make sure that all quotations are properly escaped. For example, `"temperature":"0.25"` key value pair would need to be formatted as `\"temperature\":\"0.25\"` to successfully accepted in the request.

## Contents
<a name="API_EvaluationBedrockModel_Contents"></a>

 ** modelIdentifier **   <a name="bedrock-Type-EvaluationBedrockModel-modelIdentifier"></a>
The ARN of the Amazon Bedrock model or inference profile specified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:provisioned-model/[a-z0-9]{12})|([0-9]{12}:imported-model/[a-z0-9]{12})|([0-9]{12}:application-inference-profile/[a-z0-9]{12})|([0-9]{12}:inference-profile/(([a-z-]{2,8}.)[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))|([0-9]{12}:(default-prompt-router|prompt-router)/[a-zA-Z0-9-:.]+)))|(([a-z]{2,4}[.]{1})([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|arn:aws(-[^:]+)?:sagemaker:[a-z0-9-]{1,20}:[0-9]{12}:endpoint/[a-z0-9-]{1,63}`   
Required: Yes

 ** inferenceParams **   <a name="bedrock-Type-EvaluationBedrockModel-inferenceParams"></a>
Each Amazon Bedrock support different inference parameters that change how the model behaves during inference.  
For code examples that demonstrate how to use the `inferenceParams` parameter, see [Create a model evaluation job in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create.html#model-evaluation-jobs-management-create-auto).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1023.  
Required: No

 ** performanceConfig **   <a name="bedrock-Type-EvaluationBedrockModel-performanceConfig"></a>
Specifies performance settings for the model or inference profile.  
Type: [PerformanceConfiguration](API_PerformanceConfiguration.md) object  
Required: No

## See Also
<a name="API_EvaluationBedrockModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationBedrockModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationBedrockModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationBedrockModel) 