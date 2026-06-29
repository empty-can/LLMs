

# StatusDetails
<a name="API_StatusDetails"></a>

The status details for sub-tasks of a customization job. Possible statuses for each sub-task include the following:
+ NotStarted
+ InProgress
+ Completed
+ Stopping
+ Stopped
+ Failed

## Contents
<a name="API_StatusDetails_Contents"></a>

 ** dataProcessingDetails **   <a name="bedrock-Type-StatusDetails-dataProcessingDetails"></a>
For a Distillation job, the status details for the data processing sub-task of the customization job.  
Type: [DataProcessingDetails](API_DataProcessingDetails.md) object  
Required: No

 ** trainingDetails **   <a name="bedrock-Type-StatusDetails-trainingDetails"></a>
The status details for the training sub-task of the job.  
Type: [TrainingDetails](API_TrainingDetails.md) object  
Required: No

 ** validationDetails **   <a name="bedrock-Type-StatusDetails-validationDetails"></a>
The status details for the validation sub-task of the job.  
Type: [ValidationDetails](API_ValidationDetails.md) object  
Required: No

## See Also
<a name="API_StatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/StatusDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/StatusDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/StatusDetails) 