

# IngestionJobStatistics
<a name="API_agent_IngestionJobStatistics"></a>

Contains the statistics for the data ingestion job.

## Contents
<a name="API_agent_IngestionJobStatistics_Contents"></a>

 ** numberOfDocumentsDeleted **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfDocumentsDeleted"></a>
The number of source documents that were deleted.  
Type: Long  
Required: No

 ** numberOfDocumentsFailed **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfDocumentsFailed"></a>
The number of source documents that failed to be ingested.  
Type: Long  
Required: No

 ** numberOfDocumentsScanned **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfDocumentsScanned"></a>
The total number of source documents that were scanned. Includes new, updated, and unchanged documents.  
Type: Long  
Required: No

 ** numberOfDocumentsSkipped **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfDocumentsSkipped"></a>
The number of source documents that were skipped during ingestion.  
Type: Long  
Required: No

 ** numberOfMetadataDocumentsModified **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfMetadataDocumentsModified"></a>
The number of metadata files that were updated or deleted.  
Type: Long  
Required: No

 ** numberOfMetadataDocumentsScanned **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfMetadataDocumentsScanned"></a>
The total number of metadata files that were scanned. Includes new, updated, and unchanged files.  
Type: Long  
Required: No

 ** numberOfModifiedDocumentsIndexed **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfModifiedDocumentsIndexed"></a>
The number of modified source documents in the data source that were successfully indexed.  
Type: Long  
Required: No

 ** numberOfNewDocumentsIndexed **   <a name="bedrock-Type-agent_IngestionJobStatistics-numberOfNewDocumentsIndexed"></a>
The number of new source documents in the data source that were successfully indexed.  
Type: Long  
Required: No

## See Also
<a name="API_agent_IngestionJobStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/IngestionJobStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/IngestionJobStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/IngestionJobStatistics) 