

# ModelCopyJobSummary
<a name="API_ModelCopyJobSummary"></a>

Contains details about each model copy job.

This data type is used in the following API operations:
+  [ListModelCopyJobs response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelCopyJobs.html#API_ListModelCopyJobs_ResponseSyntax) 

## Contents
<a name="API_ModelCopyJobSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-ModelCopyJobSummary-creationTime"></a>
The time that the model copy job was created.  
Type: Timestamp  
Required: Yes

 ** jobArn **   <a name="bedrock-Type-ModelCopyJobSummary-jobArn"></a>
The Amazon Resoource Name (ARN) of the model copy job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-copy-job/[a-z0-9]{12}`   
Required: Yes

 ** sourceAccountId **   <a name="bedrock-Type-ModelCopyJobSummary-sourceAccountId"></a>
The unique identifier of the account that the model being copied originated from.  
Type: String  
Pattern: `[0-9]{12}`   
Required: Yes

 ** sourceModelArn **   <a name="bedrock-Type-ModelCopyJobSummary-sourceModelArn"></a>
The Amazon Resource Name (ARN) of the original model being copied.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** status **   <a name="bedrock-Type-ModelCopyJobSummary-status"></a>
The status of the model copy job.  
Type: String  
Valid Values: `InProgress | Completed | Failed`   
Required: Yes

 ** targetModelArn **   <a name="bedrock-Type-ModelCopyJobSummary-targetModelArn"></a>
The Amazon Resource Name (ARN) of the copied model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}`   
Required: Yes

 ** failureMessage **   <a name="bedrock-Type-ModelCopyJobSummary-failureMessage"></a>
If a model fails to be copied, a message describing why the job failed is included here.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** sourceModelName **   <a name="bedrock-Type-ModelCopyJobSummary-sourceModelName"></a>
The name of the original model being copied.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: No

 ** targetModelKmsKeyArn **   <a name="bedrock-Type-ModelCopyJobSummary-targetModelKmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the copied model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** targetModelName **   <a name="bedrock-Type-ModelCopyJobSummary-targetModelName"></a>
The name of the copied model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: No

 ** targetModelTags **   <a name="bedrock-Type-ModelCopyJobSummary-targetModelTags"></a>
Tags associated with the copied model.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## See Also
<a name="API_ModelCopyJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelCopyJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelCopyJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelCopyJobSummary) 