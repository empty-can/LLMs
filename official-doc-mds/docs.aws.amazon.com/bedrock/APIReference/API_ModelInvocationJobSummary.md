

# ModelInvocationJobSummary
<a name="API_ModelInvocationJobSummary"></a>

A summary of a batch inference job.

## Contents
<a name="API_ModelInvocationJobSummary_Contents"></a>

 ** inputDataConfig **   <a name="bedrock-Type-ModelInvocationJobSummary-inputDataConfig"></a>
Details about the location of the input to the batch inference job.  
Type: [ModelInvocationJobInputDataConfig](API_ModelInvocationJobInputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** jobArn **   <a name="bedrock-Type-ModelInvocationJobSummary-jobArn"></a>
The Amazon Resource Name (ARN) of the batch inference job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-invocation-job/[a-z0-9]{12})`   
Required: Yes

 ** jobName **   <a name="bedrock-Type-ModelInvocationJobSummary-jobName"></a>
The name of the batch inference job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9]{1,63}(-*[a-zA-Z0-9\+\-\.]){0,63}`   
Required: Yes

 ** modelId **   <a name="bedrock-Type-ModelInvocationJobSummary-modelId"></a>
The unique identifier of the foundation model used for model inference.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-:]{1,63}/[a-z0-9]{12}$)|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)$)|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+$)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

 ** outputDataConfig **   <a name="bedrock-Type-ModelInvocationJobSummary-outputDataConfig"></a>
Details about the location of the output of the batch inference job.  
Type: [ModelInvocationJobOutputDataConfig](API_ModelInvocationJobOutputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** roleArn **   <a name="bedrock-Type-ModelInvocationJobSummary-roleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at [Create a service role for batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** submitTime **   <a name="bedrock-Type-ModelInvocationJobSummary-submitTime"></a>
The time at which the batch inference job was submitted.  
Type: Timestamp  
Required: Yes

 ** clientRequestToken **   <a name="bedrock-Type-ModelInvocationJobSummary-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]{1,256}(-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** endTime **   <a name="bedrock-Type-ModelInvocationJobSummary-endTime"></a>
The time at which the batch inference job ended.  
Type: Timestamp  
Required: No

 ** errorRecordCount **   <a name="bedrock-Type-ModelInvocationJobSummary-errorRecordCount"></a>
The number of records that failed to process in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** jobExpirationTime **   <a name="bedrock-Type-ModelInvocationJobSummary-jobExpirationTime"></a>
The time at which the batch inference job times or timed out.  
Type: Timestamp  
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-ModelInvocationJobSummary-lastModifiedTime"></a>
The time at which the batch inference job was last modified.  
Type: Timestamp  
Required: No

 ** message **   <a name="bedrock-Type-ModelInvocationJobSummary-message"></a>
If the batch inference job failed, this field contains a message describing why the job failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** modelInvocationType **   <a name="bedrock-Type-ModelInvocationJobSummary-modelInvocationType"></a>
The invocation endpoint for ModelInvocationJob  
Type: String  
Valid Values: `InvokeModel | Converse`   
Required: No

 ** processedRecordCount **   <a name="bedrock-Type-ModelInvocationJobSummary-processedRecordCount"></a>
The number of records that have been processed in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** status **   <a name="bedrock-Type-ModelInvocationJobSummary-status"></a>
The status of the batch inference job.  
The following statuses are possible:  
+ Submitted – This job has been submitted to a queue for validation.
+ Validating – This job is being validated for the requirements described in [Format and upload your batch inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html). The criteria include the following:
  + Your IAM service role has access to the Amazon S3 buckets containing your files.
  + Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the `modelInput` value matches the request body for the model.
  + Your files fulfill the requirements for file size and number of records. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html).
+ Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.
+ Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.
+ InProgress – This job has begun. You can start viewing the results in the output S3 location.
+ Completed – This job has successfully completed. View the output files in the output S3 location.
+ PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.
+ Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the [Support Center](https://console.aws.amazon.com/support/home/).
+ Stopped – This job was stopped by a user.
+ Stopping – This job is being stopped by a user.
Type: String  
Valid Values: `Submitted | InProgress | Completed | Failed | Stopping | Stopped | PartiallyCompleted | Expired | Validating | Scheduled`   
Required: No

 ** successRecordCount **   <a name="bedrock-Type-ModelInvocationJobSummary-successRecordCount"></a>
The number of records that were successfully processed in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** timeoutDurationInHours **   <a name="bedrock-Type-ModelInvocationJobSummary-timeoutDurationInHours"></a>
The number of hours after which the batch inference job was set to time out.  
Type: Integer  
Valid Range: Minimum value of 24. Maximum value of 168.  
Required: No

 ** totalRecordCount **   <a name="bedrock-Type-ModelInvocationJobSummary-totalRecordCount"></a>
The total number of records in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** vpcConfig **   <a name="bedrock-Type-ModelInvocationJobSummary-vpcConfig"></a>
The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see [Protect batch inference jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc).  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## See Also
<a name="API_ModelInvocationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelInvocationJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelInvocationJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelInvocationJobSummary) 