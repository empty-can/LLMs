

# ScreenshotResult
<a name="API_ScreenshotResult"></a>

The result of a screenshot action.

## Contents
<a name="API_ScreenshotResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-ScreenshotResult-status"></a>
The status of the action execution.  
Type: String  
Valid Values: `SUCCESS | FAILED`   
Required: Yes

 ** data **   <a name="BedrockAgentCore-Type-ScreenshotResult-data"></a>
The base64-encoded image data. Present only when the action succeeded.  
Type: Base64-encoded binary data object  
Required: No

 ** error **   <a name="BedrockAgentCore-Type-ScreenshotResult-error"></a>
The error message. Present only when the action failed.  
Type: String  
Required: No

## See Also
<a name="API_ScreenshotResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ScreenshotResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ScreenshotResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ScreenshotResult) 