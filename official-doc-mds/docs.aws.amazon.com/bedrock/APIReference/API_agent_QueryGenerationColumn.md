

# QueryGenerationColumn
<a name="API_agent_QueryGenerationColumn"></a>

Contains information about a column in the current table for the query engine to consider.

## Contents
<a name="API_agent_QueryGenerationColumn_Contents"></a>

 ** description **   <a name="bedrock-Type-agent_QueryGenerationColumn-description"></a>
A description of the column that helps the query engine understand the contents of the column.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** inclusion **   <a name="bedrock-Type-agent_QueryGenerationColumn-inclusion"></a>
Specifies whether to include or exclude the column during query generation. If you specify `EXCLUDE`, the column will be ignored. If you specify `INCLUDE`, all other columns in the table will be ignored.  
Type: String  
Valid Values: `INCLUDE | EXCLUDE`   
Required: No

 ** name **   <a name="bedrock-Type-agent_QueryGenerationColumn-name"></a>
The name of the column for which the other fields in this object apply.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.  
Required: No

## See Also
<a name="API_agent_QueryGenerationColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/QueryGenerationColumn) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/QueryGenerationColumn) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/QueryGenerationColumn) 