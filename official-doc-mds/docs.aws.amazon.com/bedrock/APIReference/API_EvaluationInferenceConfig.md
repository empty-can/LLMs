

# EvaluationInferenceConfig
<a name="API_EvaluationInferenceConfig"></a>

The configuration details of the inference model for an evaluation job.

For automated model evaluation jobs, only a single model is supported.

For human-based model evaluation jobs, your annotator can compare the responses for up to two different models.

## Contents
<a name="API_EvaluationInferenceConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** models **   <a name="bedrock-Type-EvaluationInferenceConfig-models"></a>
Specifies the inference models.  
Type: Array of [EvaluationModelConfig](API_EvaluationModelConfig.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: No

 ** ragConfigs **   <a name="bedrock-Type-EvaluationInferenceConfig-ragConfigs"></a>
Contains the configuration details of the inference for a knowledge base evaluation job, including either the retrieval only configuration or the retrieval with response generation configuration.  
Type: Array of [RAGConfig](API_RAGConfig.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

## See Also
<a name="API_EvaluationInferenceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationInferenceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationInferenceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationInferenceConfig) 