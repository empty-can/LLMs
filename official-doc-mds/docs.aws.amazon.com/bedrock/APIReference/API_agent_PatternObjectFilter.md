

# PatternObjectFilter
<a name="API_agent_PatternObjectFilter"></a>

The specific filters applied to your data source content. You can filter out or include certain content.

## Contents
<a name="API_agent_PatternObjectFilter_Contents"></a>

 ** objectType **   <a name="bedrock-Type-agent_PatternObjectFilter-objectType"></a>
The supported object type or content type of the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** exclusionFilters **   <a name="bedrock-Type-agent_PatternObjectFilter-exclusionFilters"></a>
A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** inclusionFilters **   <a name="bedrock-Type-agent_PatternObjectFilter-inclusionFilters"></a>
A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

## See Also
<a name="API_agent_PatternObjectFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PatternObjectFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PatternObjectFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PatternObjectFilter) 