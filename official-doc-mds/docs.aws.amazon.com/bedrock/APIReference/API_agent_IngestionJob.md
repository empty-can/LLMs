

# IngestionJob
<a name="API_agent_IngestionJob"></a>

Contains details about a data ingestion job. Data sources are ingested into a knowledge base so that Large Language Models (LLMs) can use your data.

This data type is used in the following API operations:
+  [StartIngestionJob response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_StartIngestionJob.html#API_agent_StartIngestionJob_ResponseSyntax) 
+  [GetIngestionJob response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetIngestionJob.html#API_agent_GetIngestionJob_ResponseSyntax) 
+  [ListIngestionJob response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListIngestionJobs.html#API_agent_ListIngestionJobs_ResponseSyntax) 

## Contents
<a name="API_agent_IngestionJob_Contents"></a>

 ** dataSourceId **   <a name="bedrock-Type-agent_IngestionJob-dataSourceId"></a>
The unique identifier of the data source for the data ingestion job.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** ingestionJobId **   <a name="bedrock-Type-agent_IngestionJob-ingestionJobId"></a>
The unique identifier of the data ingestion job.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_IngestionJob-knowledgeBaseId"></a>
The unique identifier of the knowledge for the data ingestion job.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** startedAt **   <a name="bedrock-Type-agent_IngestionJob-startedAt"></a>
The time the data ingestion job started.  
If you stop a data ingestion job, the `startedAt` time is the time the job was started before the job was stopped.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="bedrock-Type-agent_IngestionJob-status"></a>
The status of the data ingestion job.  
Type: String  
Valid Values: `STARTING | IN_PROGRESS | COMPLETE | FAILED | STOPPING | STOPPED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_IngestionJob-updatedAt"></a>
The time the data ingestion job was last updated.  
If you stop a data ingestion job, the `updatedAt` time is the time the job was stopped.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_IngestionJob-description"></a>
The description of the data ingestion job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** failureReasons **   <a name="bedrock-Type-agent_IngestionJob-failureReasons"></a>
A list of reasons that the data ingestion job failed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** statistics **   <a name="bedrock-Type-agent_IngestionJob-statistics"></a>
Contains statistics about the data ingestion job.  
Type: [IngestionJobStatistics](API_agent_IngestionJobStatistics.md) object  
Required: No

## See Also
<a name="API_agent_IngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/IngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/IngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/IngestionJob) 