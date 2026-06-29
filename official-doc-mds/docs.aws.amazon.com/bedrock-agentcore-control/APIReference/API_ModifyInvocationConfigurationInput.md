

# ModifyInvocationConfigurationInput
<a name="API_ModifyInvocationConfigurationInput"></a>

The configuration for updating invocation settings.

## Contents
<a name="API_ModifyInvocationConfigurationInput_Contents"></a>

 ** payloadDeliveryBucketName **   <a name="bedrockagentcorecontrol-Type-ModifyInvocationConfigurationInput-payloadDeliveryBucketName"></a>
The updated S3 bucket name for event payload delivery.  
Type: String  
Pattern: `[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`   
Required: No

 ** topicArn **   <a name="bedrockagentcorecontrol-Type-ModifyInvocationConfigurationInput-topicArn"></a>
The updated ARN of the SNS topic for job notifications.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

## See Also
<a name="API_ModifyInvocationConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ModifyInvocationConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ModifyInvocationConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ModifyInvocationConfigurationInput) 