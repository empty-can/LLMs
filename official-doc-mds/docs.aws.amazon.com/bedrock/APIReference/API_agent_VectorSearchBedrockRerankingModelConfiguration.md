

# VectorSearchBedrockRerankingModelConfiguration
<a name="API_agent_VectorSearchBedrockRerankingModelConfiguration"></a>

Configures the Amazon Bedrock model used for reranking retrieved results.

## Contents
<a name="API_agent_VectorSearchBedrockRerankingModelConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-agent_VectorSearchBedrockRerankingModelConfiguration-modelArn"></a>
The Amazon Resource Name (ARN) of the Amazon Bedrock reranker model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/(.*))?`   
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent_VectorSearchBedrockRerankingModelConfiguration-additionalModelRequestFields"></a>
Specifies additional model-specific request parameters as key-value pairs that are included in the request to the Amazon Bedrock reranker model.  
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_agent_VectorSearchBedrockRerankingModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/VectorSearchBedrockRerankingModelConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/VectorSearchBedrockRerankingModelConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/VectorSearchBedrockRerankingModelConfiguration) 