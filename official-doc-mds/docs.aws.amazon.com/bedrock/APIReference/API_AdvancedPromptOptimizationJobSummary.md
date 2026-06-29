

# AdvancedPromptOptimizationJobSummary
<a name="API_AdvancedPromptOptimizationJobSummary"></a>

A summary of an advanced prompt optimization job.

## Contents
<a name="API_AdvancedPromptOptimizationJobSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-AdvancedPromptOptimizationJobSummary-creationTime"></a>
The time at which the job was created.  
Type: Timestamp  
Required: Yes

 ** jobArn **   <a name="bedrock-Type-AdvancedPromptOptimizationJobSummary-jobArn"></a>
The ARN of the job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/[a-z0-9]{12}`   
Required: Yes

 ** jobName **   <a name="bedrock-Type-AdvancedPromptOptimizationJobSummary-jobName"></a>
The name of the job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9.+-]*`   
Required: Yes

 ** jobStatus **   <a name="bedrock-Type-AdvancedPromptOptimizationJobSummary-jobStatus"></a>
The status of the job.  
Type: String  
Valid Values: `InProgress | Completed | Failed | PartiallyCompleted | Stopping | Stopped | Deleting`   
Required: Yes

 ** lastModifiedTime **   <a name="bedrock-Type-AdvancedPromptOptimizationJobSummary-lastModifiedTime"></a>
The time at which the job was last modified.  
Type: Timestamp  
Required: No

## See Also
<a name="API_AdvancedPromptOptimizationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AdvancedPromptOptimizationJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AdvancedPromptOptimizationJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AdvancedPromptOptimizationJobSummary) 