

# BedrockFoundationModelContextEnrichmentConfiguration
<a name="API_agent_BedrockFoundationModelContextEnrichmentConfiguration"></a>

Context enrichment configuration is used to provide additional context to the RAG application using Amazon Bedrock foundation models.

## Contents
<a name="API_agent_BedrockFoundationModelContextEnrichmentConfiguration_Contents"></a>

 ** enrichmentStrategyConfiguration **   <a name="bedrock-Type-agent_BedrockFoundationModelContextEnrichmentConfiguration-enrichmentStrategyConfiguration"></a>
The enrichment stategy used to provide additional context. For example, Neptune GraphRAG uses Amazon Bedrock foundation models to perform chunk entity extraction.  
Type: [EnrichmentStrategyConfiguration](API_agent_EnrichmentStrategyConfiguration.md) object  
Required: Yes

 ** modelArn **   <a name="bedrock-Type-agent_BedrockFoundationModelContextEnrichmentConfiguration-modelArn"></a>
The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

## See Also
<a name="API_agent_BedrockFoundationModelContextEnrichmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/BedrockFoundationModelContextEnrichmentConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/BedrockFoundationModelContextEnrichmentConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/BedrockFoundationModelContextEnrichmentConfiguration) 