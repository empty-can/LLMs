

# DataSourceSummary
<a name="API_agent_DataSourceSummary"></a>

Contains details about a data source.

## Contents
<a name="API_agent_DataSourceSummary_Contents"></a>

 ** dataSourceId **   <a name="bedrock-Type-agent_DataSourceSummary-dataSourceId"></a>
The unique identifier of the data source.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_DataSourceSummary-knowledgeBaseId"></a>
The unique identifier of the knowledge base to which the data source belongs.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_DataSourceSummary-name"></a>
The name of the data source.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_DataSourceSummary-status"></a>
The status of the data source.  
Type: String  
Valid Values: `AVAILABLE | DELETING | DELETE_UNSUCCESSFUL | CREATING | UPDATING | FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_DataSourceSummary-updatedAt"></a>
The time at which the data source was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_DataSourceSummary-description"></a>
The description of the data source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_DataSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DataSourceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DataSourceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DataSourceSummary) 