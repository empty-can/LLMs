

# ModelCustomizationJobSummary
<a name="API_ModelCustomizationJobSummary"></a>

Information about one customization job

## Contents
<a name="API_ModelCustomizationJobSummary_Contents"></a>

 ** baseModelArn **   <a name="bedrock-Type-ModelCustomizationJobSummary-baseModelArn"></a>
Amazon Resource Name (ARN) of the base model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** creationTime **   <a name="bedrock-Type-ModelCustomizationJobSummary-creationTime"></a>
Creation time of the custom model.   
Type: Timestamp  
Required: Yes

 ** jobArn **   <a name="bedrock-Type-ModelCustomizationJobSummary-jobArn"></a>
Amazon Resource Name (ARN) of the customization job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12}`   
Required: Yes

 ** jobName **   <a name="bedrock-Type-ModelCustomizationJobSummary-jobName"></a>
Name of the customization job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*`   
Required: Yes

 ** status **   <a name="bedrock-Type-ModelCustomizationJobSummary-status"></a>
Status of the customization job.   
Type: String  
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`   
Required: Yes

 ** customizationType **   <a name="bedrock-Type-ModelCustomizationJobSummary-customizationType"></a>
Specifies whether to carry out continued pre-training of a model or whether to fine-tune it. For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html).  
Type: String  
Valid Values: `FINE_TUNING | CONTINUED_PRE_TRAINING | DISTILLATION | REINFORCEMENT_FINE_TUNING | IMPORTED`   
Required: No

 ** customModelArn **   <a name="bedrock-Type-ModelCustomizationJobSummary-customModelArn"></a>
Amazon Resource Name (ARN) of the custom model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}`   
Required: No

 ** customModelName **   <a name="bedrock-Type-ModelCustomizationJobSummary-customModelName"></a>
Name of the custom model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: No

 ** endTime **   <a name="bedrock-Type-ModelCustomizationJobSummary-endTime"></a>
Time that the customization job ended.  
Type: Timestamp  
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-ModelCustomizationJobSummary-lastModifiedTime"></a>
Time that the customization job was last modified.  
Type: Timestamp  
Required: No

 ** statusDetails **   <a name="bedrock-Type-ModelCustomizationJobSummary-statusDetails"></a>
Details about the status of the data processing sub-task of the job.  
Type: [StatusDetails](API_StatusDetails.md) object  
Required: No

## See Also
<a name="API_ModelCustomizationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelCustomizationJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelCustomizationJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelCustomizationJobSummary) 