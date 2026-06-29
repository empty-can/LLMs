

# RecordingConfig
<a name="API_RecordingConfig"></a>

The recording configuration for a browser. This structure defines how browser sessions are recorded.

## Contents
<a name="API_RecordingConfig_Contents"></a>

 ** enabled **   <a name="bedrockagentcorecontrol-Type-RecordingConfig-enabled"></a>
Indicates whether recording is enabled for the browser. When set to true, browser sessions are recorded.  
Type: Boolean  
Required: No

 ** s3Location **   <a name="bedrockagentcorecontrol-Type-RecordingConfig-s3Location"></a>
The Amazon S3 location where browser recordings are stored. This location contains the recorded browser sessions.  
Type: [S3Location](API_S3Location.md) object  
Required: No

## See Also
<a name="API_RecordingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RecordingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RecordingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RecordingConfig) 