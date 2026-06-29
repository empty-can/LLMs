

# IngestionJobSummary
<a name="API_agent_IngestionJobSummary"></a>

Contains details about a data ingestion job.

## Contents
<a name="API_agent_IngestionJobSummary_Contents"></a>

 ** dataSourceId **   <a name="bedrock-Type-agent_IngestionJobSummary-dataSourceId"></a>
The unique identifier of the data source for the data ingestion job.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** ingestionJobId **   <a name="bedrock-Type-agent_IngestionJobSummary-ingestionJobId"></a>
The unique identifier of the data ingestion job.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_IngestionJobSummary-knowledgeBaseId"></a>
The unique identifier of the knowledge base for the data ingestion job.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** startedAt **   <a name="bedrock-Type-agent_IngestionJobSummary-startedAt"></a>
The time the data ingestion job started.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="bedrock-Type-agent_IngestionJobSummary-status"></a>
The status of the data ingestion job.  
Type: String  
Valid Values: `STARTING | IN_PROGRESS | COMPLETE | FAILED | STOPPING | STOPPED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_IngestionJobSummary-updatedAt"></a>
The time the data ingestion job was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_IngestionJobSummary-description"></a>
The description of the data ingestion job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** statistics **   <a name="bedrock-Type-agent_IngestionJobSummary-statistics"></a>
Contains statistics for the data ingestion job.  
Type: [IngestionJobStatistics](API_agent_IngestionJobStatistics.md) object  
Required: No

## See Also
<a name="API_agent_IngestionJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/IngestionJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/IngestionJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/IngestionJobSummary) 