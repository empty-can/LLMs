

# QueryGenerationContext
<a name="API_agent_QueryGenerationContext"></a>

>Contains configurations for context to use during query generation.

## Contents
<a name="API_agent_QueryGenerationContext_Contents"></a>

 ** curatedQueries **   <a name="bedrock-Type-agent_QueryGenerationContext-curatedQueries"></a>
An array of objects, each of which defines information about example queries to help the query engine generate appropriate SQL queries.  
Type: Array of [CuratedQuery](API_agent_CuratedQuery.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** tables **   <a name="bedrock-Type-agent_QueryGenerationContext-tables"></a>
An array of objects, each of which defines information about a table in the database.  
Type: Array of [QueryGenerationTable](API_agent_QueryGenerationTable.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_agent_QueryGenerationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/QueryGenerationContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/QueryGenerationContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/QueryGenerationContext) 