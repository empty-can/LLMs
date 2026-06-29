

# IngestionJobFilter
<a name="API_agent_IngestionJobFilter"></a>

The definition of a filter to filter the data.

## Contents
<a name="API_agent_IngestionJobFilter_Contents"></a>

 ** attribute **   <a name="bedrock-Type-agent_IngestionJobFilter-attribute"></a>
The name of field or attribute to apply the filter.  
Type: String  
Valid Values: `STATUS`   
Required: Yes

 ** operator **   <a name="bedrock-Type-agent_IngestionJobFilter-operator"></a>
The operation to apply to the field or attribute.  
Type: String  
Valid Values: `EQ`   
Required: Yes

 ** values **   <a name="bedrock-Type-agent_IngestionJobFilter-values"></a>
A list of values that belong to the field or attribute.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `.*`   
Required: Yes

## See Also
<a name="API_agent_IngestionJobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/IngestionJobFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/IngestionJobFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/IngestionJobFilter) 