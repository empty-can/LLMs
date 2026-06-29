

# EvaluationInferenceConfigSummary
<a name="API_EvaluationInferenceConfigSummary"></a>

Identifies the models, Knowledge Bases, or other RAG sources evaluated in a model or Knowledge Base evaluation job.

## Contents
<a name="API_EvaluationInferenceConfigSummary_Contents"></a>

 ** modelConfigSummary **   <a name="bedrock-Type-EvaluationInferenceConfigSummary-modelConfigSummary"></a>
A summary of the models used in an Amazon Bedrock model evaluation job. These resources can be models in Amazon Bedrock or models outside of Amazon Bedrock that you use to generate your own inference response data.  
Type: [EvaluationModelConfigSummary](API_EvaluationModelConfigSummary.md) object  
Required: No

 ** ragConfigSummary **   <a name="bedrock-Type-EvaluationInferenceConfigSummary-ragConfigSummary"></a>
A summary of the RAG resources used in an Amazon Bedrock Knowledge Base evaluation job. These resources can be Knowledge Bases in Amazon Bedrock or RAG sources outside of Amazon Bedrock that you use to generate your own inference response data.  
Type: [EvaluationRagConfigSummary](API_EvaluationRagConfigSummary.md) object  
Required: No

## See Also
<a name="API_EvaluationInferenceConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationInferenceConfigSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationInferenceConfigSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationInferenceConfigSummary) 