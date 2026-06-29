

# AutomationStream
<a name="API_AutomationStream"></a>

The configuration for a stream that enables programmatic control of a browser session in Amazon Bedrock AgentCore. This stream provides a bidirectional communication channel for sending commands to the browser and receiving responses, allowing agents to automate web interactions such as navigation, form filling, and element clicking.

## Contents
<a name="API_AutomationStream_Contents"></a>

 ** streamEndpoint **   <a name="BedrockAgentCore-Type-AutomationStream-streamEndpoint"></a>
The endpoint URL for the automation stream. This URL is used to establish a WebSocket connection to the stream for sending commands and receiving responses.  
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 512.  
Required: Yes

 ** streamStatus **   <a name="BedrockAgentCore-Type-AutomationStream-streamStatus"></a>
The current status of the automation stream. This indicates whether the stream is available for use. Possible values include ACTIVE, CONNECTING, and DISCONNECTED.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

## See Also
<a name="API_AutomationStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AutomationStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AutomationStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AutomationStream) 