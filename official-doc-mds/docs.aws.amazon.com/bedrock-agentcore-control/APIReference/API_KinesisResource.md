

# KinesisResource
<a name="API_KinesisResource"></a>

Configuration for Kinesis Data Stream delivery.

## Contents
<a name="API_KinesisResource_Contents"></a>

 ** contentConfigurations **   <a name="bedrockagentcorecontrol-Type-KinesisResource-contentConfigurations"></a>
Content configurations for stream delivery.  
Type: Array of [ContentConfiguration](API_ContentConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** dataStreamArn **   <a name="bedrockagentcorecontrol-Type-KinesisResource-dataStreamArn"></a>
ARN of the Kinesis Data Stream.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: Yes

## See Also
<a name="API_KinesisResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/KinesisResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/KinesisResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/KinesisResource) 