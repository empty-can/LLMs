

# BedrockEvaluatorModelConfig
<a name="API_BedrockEvaluatorModelConfig"></a>

 The configuration for using Amazon Bedrock models in evaluator assessments, including model selection and inference parameters. 

## Contents
<a name="API_BedrockEvaluatorModelConfig_Contents"></a>

 ** modelId **   <a name="bedrockagentcorecontrol-Type-BedrockEvaluatorModelConfig-modelId"></a>
 The identifier of the Amazon Bedrock model to use for evaluation. Must be a supported foundation model available in your region.   
Type: String  
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrockagentcorecontrol-Type-BedrockEvaluatorModelConfig-additionalModelRequestFields"></a>
 Additional model-specific request fields to customize model behavior beyond the standard inference configuration.   
Type: JSON value  
Required: No

 ** inferenceConfig **   <a name="bedrockagentcorecontrol-Type-BedrockEvaluatorModelConfig-inferenceConfig"></a>
 The inference configuration parameters that control model behavior during evaluation, including temperature, token limits, and sampling settings.   
Type: [InferenceConfiguration](API_InferenceConfiguration.md) object  
Required: No

## See Also
<a name="API_BedrockEvaluatorModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BedrockEvaluatorModelConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BedrockEvaluatorModelConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BedrockEvaluatorModelConfig) 