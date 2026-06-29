

# AgenticRetrieveConfiguration
<a name="API_agent-runtime_AgenticRetrieveConfiguration"></a>

Configuration settings for the agentic retrieval operation.

## Contents
<a name="API_agent-runtime_AgenticRetrieveConfiguration_Contents"></a>

 ** foundationModelConfiguration **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveConfiguration-foundationModelConfiguration"></a>
The foundation model configuration. Required when foundationModelType is CUSTOM.  
Type: [FoundationModelConfiguration](API_agent-runtime_FoundationModelConfiguration.md) object  
Required: No

 ** foundationModelType **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveConfiguration-foundationModelType"></a>
The type of foundation model to use. CUSTOM uses a specified model, MANAGED uses the service default.  
Type: String  
Valid Values: `CUSTOM | MANAGED`   
Required: No

 ** maxAgentIteration **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveConfiguration-maxAgentIteration"></a>
The maximum number of agent iterations for retrieval.  
Type: Integer  
Valid Range: Minimum value of 2.  
Required: No

 ** rerankingConfiguration **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveConfiguration-rerankingConfiguration"></a>
The reranking model configuration. Required when rerankingModelType is CUSTOM.  
Type: [AgenticRetrieveRerankingConfiguration](API_agent-runtime_AgenticRetrieveRerankingConfiguration.md) object  
Required: No

 ** rerankingModelType **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveConfiguration-rerankingModelType"></a>
The type of reranking model to use. CUSTOM uses a specified model, MANAGED uses the service default. If not specified, defaults to MANAGED for managed embedding knowledge bases and NONE for custom embedding knowledge bases.  
Type: String  
Valid Values: `CUSTOM | MANAGED | NONE`   
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveConfiguration) 