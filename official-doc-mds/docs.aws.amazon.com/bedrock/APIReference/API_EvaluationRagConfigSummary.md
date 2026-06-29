

# EvaluationRagConfigSummary
<a name="API_EvaluationRagConfigSummary"></a>

A summary of the RAG resources used in an Amazon Bedrock Knowledge Base evaluation job. These resources can be Knowledge Bases in Amazon Bedrock or RAG sources outside of Amazon Bedrock that you use to generate your own inference response data.

## Contents
<a name="API_EvaluationRagConfigSummary_Contents"></a>

 ** bedrockKnowledgeBaseIdentifiers **   <a name="bedrock-Type-EvaluationRagConfigSummary-bedrockKnowledgeBaseIdentifiers"></a>
The Amazon Resource Names (ARNs) of the Knowledge Base resources used for a Knowledge Base evaluation job where Amazon Bedrock invokes the Knowledge Base for you.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: No

 ** precomputedRagSourceIdentifiers **   <a name="bedrock-Type-EvaluationRagConfigSummary-precomputedRagSourceIdentifiers"></a>
A label that identifies the RAG sources used for a Knowledge Base evaluation job where you provide your own inference response data.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9._-]){0,255}`   
Required: No

## See Also
<a name="API_EvaluationRagConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationRagConfigSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationRagConfigSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationRagConfigSummary) 