

# CustomModelDeploymentSummary
<a name="API_CustomModelDeploymentSummary"></a>

Contains summary information about a custom model deployment, including its ARN, name, status, and associated custom model.

## Contents
<a name="API_CustomModelDeploymentSummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-CustomModelDeploymentSummary-createdAt"></a>
The date and time when the custom model deployment was created.  
Type: Timestamp  
Required: Yes

 ** customModelDeploymentArn **   <a name="bedrock-Type-CustomModelDeploymentSummary-customModelDeploymentArn"></a>
The Amazon Resource Name (ARN) of the custom model deployment.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model-deployment/[a-z0-9]{12}`   
Required: Yes

 ** customModelDeploymentName **   <a name="bedrock-Type-CustomModelDeploymentSummary-customModelDeploymentName"></a>
The name of the custom model deployment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

 ** modelArn **   <a name="bedrock-Type-CustomModelDeploymentSummary-modelArn"></a>
The Amazon Resource Name (ARN) of the custom model associated with this deployment.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** status **   <a name="bedrock-Type-CustomModelDeploymentSummary-status"></a>
The status of the custom model deployment. Possible values are `CREATING`, `ACTIVE`, and `FAILED`.  
Type: String  
Valid Values: `Creating | Active | Failed`   
Required: Yes

 ** failureMessage **   <a name="bedrock-Type-CustomModelDeploymentSummary-failureMessage"></a>
If the deployment status is `FAILED`, this field contains a message describing the failure reason.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** lastUpdatedAt **   <a name="bedrock-Type-CustomModelDeploymentSummary-lastUpdatedAt"></a>
The date and time when the custom model deployment was last modified.  
Type: Timestamp  
Required: No

## See Also
<a name="API_CustomModelDeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomModelDeploymentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomModelDeploymentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomModelDeploymentSummary) 