

# SearchCriteria
<a name="API_SearchCriteria"></a>

Contains search criteria for retrieving memory records.

## Contents
<a name="API_SearchCriteria_Contents"></a>

 ** searchQuery **   <a name="BedrockAgentCore-Type-SearchCriteria-searchQuery"></a>
The search query to use for finding relevant memory records.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10000.  
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-SearchCriteria-memoryStrategyId"></a>
The memory strategy identifier to filter memory records by.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** metadataFilters **   <a name="BedrockAgentCore-Type-SearchCriteria-metadataFilters"></a>
Filters to apply to metadata associated with a memory.  
Type: Array of [MemoryMetadataFilterExpression](API_MemoryMetadataFilterExpression.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

 ** topK **   <a name="BedrockAgentCore-Type-SearchCriteria-topK"></a>
The maximum number of top-scoring memory records to return. This value is used for semantic search ranking.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_SearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SearchCriteria) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SearchCriteria) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SearchCriteria) 