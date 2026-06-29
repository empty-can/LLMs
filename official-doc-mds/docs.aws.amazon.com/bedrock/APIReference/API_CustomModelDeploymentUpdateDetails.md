

# CustomModelDeploymentUpdateDetails
<a name="API_CustomModelDeploymentUpdateDetails"></a>

 Details about an update to a custom model deployment, including the new custom model resource ARN and current update status. 

## Contents
<a name="API_CustomModelDeploymentUpdateDetails_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-CustomModelDeploymentUpdateDetails-modelArn"></a>
 ARN of the new custom model being deployed as part of the update.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** updateStatus **   <a name="bedrock-Type-CustomModelDeploymentUpdateDetails-updateStatus"></a>
 Current status of the deployment update.   
Type: String  
Valid Values: `Updating | UpdateCompleted | UpdateFailed`   
Required: Yes

## See Also
<a name="API_CustomModelDeploymentUpdateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomModelDeploymentUpdateDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomModelDeploymentUpdateDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomModelDeploymentUpdateDetails) 