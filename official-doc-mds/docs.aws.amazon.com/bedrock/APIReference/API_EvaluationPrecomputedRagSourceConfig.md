

# EvaluationPrecomputedRagSourceConfig
<a name="API_EvaluationPrecomputedRagSourceConfig"></a>

A summary of a RAG source used for a Knowledge Base evaluation job where you provide your own inference response data.

## Contents
<a name="API_EvaluationPrecomputedRagSourceConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** retrieveAndGenerateSourceConfig **   <a name="bedrock-Type-EvaluationPrecomputedRagSourceConfig-retrieveAndGenerateSourceConfig"></a>
A summary of a RAG source used for a retrieve-and-generate Knowledge Base evaluation job where you provide your own inference response data.  
Type: [EvaluationPrecomputedRetrieveAndGenerateSourceConfig](API_EvaluationPrecomputedRetrieveAndGenerateSourceConfig.md) object  
Required: No

 ** retrieveSourceConfig **   <a name="bedrock-Type-EvaluationPrecomputedRagSourceConfig-retrieveSourceConfig"></a>
A summary of a RAG source used for a retrieve-only Knowledge Base evaluation job where you provide your own inference response data.  
Type: [EvaluationPrecomputedRetrieveSourceConfig](API_EvaluationPrecomputedRetrieveSourceConfig.md) object  
Required: No

## See Also
<a name="API_EvaluationPrecomputedRagSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationPrecomputedRagSourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationPrecomputedRagSourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationPrecomputedRagSourceConfig) 