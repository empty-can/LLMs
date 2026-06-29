

# ContextEnrichmentConfiguration
<a name="API_agent_ContextEnrichmentConfiguration"></a>

Context enrichment configuration is used to provide additional context to the RAG application.

## Contents
<a name="API_agent_ContextEnrichmentConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_ContextEnrichmentConfiguration-type"></a>
The method used for context enrichment. It must be Amazon Bedrock foundation models.  
Type: String  
Valid Values: `BEDROCK_FOUNDATION_MODEL`   
Required: Yes

 ** bedrockFoundationModelConfiguration **   <a name="bedrock-Type-agent_ContextEnrichmentConfiguration-bedrockFoundationModelConfiguration"></a>
The configuration of the Amazon Bedrock foundation model used for context enrichment.  
Type: [BedrockFoundationModelContextEnrichmentConfiguration](API_agent_BedrockFoundationModelContextEnrichmentConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_ContextEnrichmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ContextEnrichmentConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ContextEnrichmentConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ContextEnrichmentConfiguration) 