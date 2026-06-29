

# DataAutomationLibraryIngestionJob
<a name="API_data-automation_DataAutomationLibraryIngestionJob"></a>

A data automation library ingestion job.

## Contents
<a name="API_data-automation_DataAutomationLibraryIngestionJob_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-creationTime"></a>
When the job was created.  
Type: Timestamp  
Required: Yes

 ** entityType **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-entityType"></a>
The entity type.  
Type: String  
Valid Values: `VOCABULARY`   
Required: Yes

 ** jobArn **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-jobArn"></a>
The job's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library-ingestion-job/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** jobStatus **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-jobStatus"></a>
The job's status.  
Type: String  
Valid Values: `IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`   
Required: Yes

 ** operationType **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-operationType"></a>
The operation type.  
Type: String  
Valid Values: `UPSERT | DELETE`   
Required: Yes

 ** outputConfiguration **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-outputConfiguration"></a>
Output configuration for the job.  
Type: [OutputConfiguration](API_data-automation_OutputConfiguration.md) object  
Required: Yes

 ** completionTime **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-completionTime"></a>
When the job completed.  
Type: Timestamp  
Required: No

 ** errorMessage **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-errorMessage"></a>
The error message if the job failed.  
Type: String  
Required: No

 ** errorType **   <a name="bedrock-Type-data-automation_DataAutomationLibraryIngestionJob-errorType"></a>
The error type if the job failed.  
Type: String  
Required: No

## See Also
<a name="API_data-automation_DataAutomationLibraryIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DataAutomationLibraryIngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DataAutomationLibraryIngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DataAutomationLibraryIngestionJob) 