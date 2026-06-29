

# DataAutomationLibraryIngestionJobSummary
<a name="API_data-automation_DataAutomationLibraryIngestionJobSummary"></a>

A summary of a data automation library ingestion job.

## Contents
<a name="API_data-automation_DataAutomationLibraryIngestionJobSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJobSummary-creationTime"></a>
When the job was created.  
Type: Timestamp  
Required: Yes

 ** entityType **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJobSummary-entityType"></a>
The entity type.  
Type: String  
Valid Values: `VOCABULARY`   
Required: Yes

 ** jobArn **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJobSummary-jobArn"></a>
The job's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library-ingestion-job/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** jobStatus **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJobSummary-jobStatus"></a>
The job's status.  
Type: String  
Valid Values: `IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`   
Required: Yes

 ** operationType **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJobSummary-operationType"></a>
The operation type.  
Type: String  
Valid Values: `UPSERT | DELETE`   
Required: Yes

 ** completionTime **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJobSummary-completionTime"></a>
When the job completed.  
Type: Timestamp  
Required: No

## See Also
<a name="API_data-automation_DataAutomationLibraryIngestionJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DataAutomationLibraryIngestionJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DataAutomationLibraryIngestionJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DataAutomationLibraryIngestionJobSummary) 