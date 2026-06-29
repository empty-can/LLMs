

# CustomModelSummary
<a name="API_CustomModelSummary"></a>

Summary information for a custom model.

## Contents
<a name="API_CustomModelSummary_Contents"></a>

 ** baseModelArn **   <a name="bedrock-Type-CustomModelSummary-baseModelArn"></a>
The base model Amazon Resource Name (ARN).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** baseModelName **   <a name="bedrock-Type-CustomModelSummary-baseModelName"></a>
The base model name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63})`   
Required: Yes

 ** creationTime **   <a name="bedrock-Type-CustomModelSummary-creationTime"></a>
Creation time of the model.  
Type: Timestamp  
Required: Yes

 ** modelArn **   <a name="bedrock-Type-CustomModelSummary-modelArn"></a>
The Amazon Resource Name (ARN) of the custom model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}`   
Required: Yes

 ** modelName **   <a name="bedrock-Type-CustomModelSummary-modelName"></a>
The name of the custom model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

 ** customizationType **   <a name="bedrock-Type-CustomModelSummary-customizationType"></a>
Specifies whether to carry out continued pre-training of a model or whether to fine-tune it. For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html).  
Type: String  
Valid Values: `FINE_TUNING | CONTINUED_PRE_TRAINING | DISTILLATION | REINFORCEMENT_FINE_TUNING | IMPORTED`   
Required: No

 ** modelStatus **   <a name="bedrock-Type-CustomModelSummary-modelStatus"></a>
The current status of the custom model. Possible values include:  
+  `Creating` - The model is being created and validated.
+  `Active` - The model has been successfully created and is ready for use.
+  `Failed` - The model creation process failed.
Type: String  
Valid Values: `Active | Creating | Failed`   
Required: No

 ** ownerAccountId **   <a name="bedrock-Type-CustomModelSummary-ownerAccountId"></a>
The unique identifier of the account that owns the model.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

## See Also
<a name="API_CustomModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomModelSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomModelSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomModelSummary) 