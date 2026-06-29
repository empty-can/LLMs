

# ManagedSearchBedrockRerankingConfiguration
<a name="API_agent-runtime_ManagedSearchBedrockRerankingConfiguration"></a>

Configuration for a Bedrock reranking model used in managed search.

## Contents
<a name="API_agent-runtime_ManagedSearchBedrockRerankingConfiguration_Contents"></a>

 ** modelConfiguration **   <a name="bedrock-Type-agent-runtime_ManagedSearchBedrockRerankingConfiguration-modelConfiguration"></a>
The model configuration containing the model ARN for reranking.  
Type: [ManagedSearchBedrockRerankingModelConfiguration](API_agent-runtime_ManagedSearchBedrockRerankingModelConfiguration.md) object  
Required: Yes

 ** metadataConfiguration **   <a name="bedrock-Type-agent-runtime_ManagedSearchBedrockRerankingConfiguration-metadataConfiguration"></a>
The metadata configuration for reranking.  
Type: [MetadataConfigurationForReranking](API_agent-runtime_MetadataConfigurationForReranking.md) object  
Required: No

 ** numberOfRerankedResults **   <a name="bedrock-Type-agent-runtime_ManagedSearchBedrockRerankingConfiguration-numberOfRerankedResults"></a>
The number of results to return after reranking.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_agent-runtime_ManagedSearchBedrockRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ManagedSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ManagedSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ManagedSearchBedrockRerankingConfiguration) 