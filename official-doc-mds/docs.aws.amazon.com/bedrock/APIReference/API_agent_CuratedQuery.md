

# CuratedQuery
<a name="API_agent_CuratedQuery"></a>

Contains configurations for a query, each of which defines information about example queries to help the query engine generate appropriate SQL queries.

## Contents
<a name="API_agent_CuratedQuery_Contents"></a>

 ** naturalLanguage **   <a name="bedrock-Type-agent_CuratedQuery-naturalLanguage"></a>
An example natural language query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

 ** sql **   <a name="bedrock-Type-agent_CuratedQuery-sql"></a>
The SQL equivalent of the natural language query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

## See Also
<a name="API_agent_CuratedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CuratedQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CuratedQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CuratedQuery) 