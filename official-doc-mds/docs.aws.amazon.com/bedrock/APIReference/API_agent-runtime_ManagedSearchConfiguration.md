

# ManagedSearchConfiguration
<a name="API_agent-runtime_ManagedSearchConfiguration"></a>

Configuration for managed search in a knowledge base. Managed search automatically determines the best search strategy based on your data store configuration.

## Contents
<a name="API_agent-runtime_ManagedSearchConfiguration_Contents"></a>

 ** filter **   <a name="bedrock-Type-agent-runtime_ManagedSearchConfiguration-filter"></a>
Filters the metadata of the retrieved results so that Amazon Bedrock returns only results that match the filter.  
Type: [RetrievalFilter](API_agent-runtime_RetrievalFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** numberOfResults **   <a name="bedrock-Type-agent-runtime_ManagedSearchConfiguration-numberOfResults"></a>
The number of results to retrieve.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** rerankingConfiguration **   <a name="bedrock-Type-agent-runtime_ManagedSearchConfiguration-rerankingConfiguration"></a>
Contains configurations for reranking the results retrieved from the managed search.  
Type: [ManagedSearchRerankingConfiguration](API_agent-runtime_ManagedSearchRerankingConfiguration.md) object  
Required: No

 ** rerankingModelType **   <a name="bedrock-Type-agent-runtime_ManagedSearchConfiguration-rerankingModelType"></a>
The type of reranking model to use when reranking results retrieved from the managed search. Use `CUSTOM` to specify a model, `MANAGED` to use the service default, or `NONE` to disable reranking.  
Type: String  
Valid Values: `CUSTOM | MANAGED | NONE`   
Required: No

## See Also
<a name="API_agent-runtime_ManagedSearchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ManagedSearchConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ManagedSearchConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ManagedSearchConfiguration) 