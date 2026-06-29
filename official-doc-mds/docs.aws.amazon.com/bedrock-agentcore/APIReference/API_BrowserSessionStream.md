

# BrowserSessionStream
<a name="API_BrowserSessionStream"></a>

The collection of streams associated with a browser session in Amazon Bedrock AgentCore. These streams provide different ways to interact with and observe the browser session, including programmatic control and visual representation of the browser content.

## Contents
<a name="API_BrowserSessionStream_Contents"></a>

 ** automationStream **   <a name="BedrockAgentCore-Type-BrowserSessionStream-automationStream"></a>
The stream that enables programmatic control of the browser. This stream allows agents to perform actions such as navigating to URLs, clicking elements, and filling forms.  
Type: [AutomationStream](API_AutomationStream.md) object  
Required: Yes

 ** liveViewStream **   <a name="BedrockAgentCore-Type-BrowserSessionStream-liveViewStream"></a>
The stream that provides a visual representation of the browser content. This stream allows agents to observe the current state of the browser, including rendered web pages and visual elements.  
Type: [LiveViewStream](API_LiveViewStream.md) object  
Required: No

## See Also
<a name="API_BrowserSessionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserSessionStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserSessionStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserSessionStream) 