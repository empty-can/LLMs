

# BrowserAction
<a name="API_BrowserAction"></a>

The browser action to perform. Exactly one member must be set per request.

## Contents
<a name="API_BrowserAction_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** keyPress **   <a name="BedrockAgentCore-Type-BrowserAction-keyPress"></a>
Press a key one or more times.  
Type: [KeyPressArguments](API_KeyPressArguments.md) object  
Required: No

 ** keyShortcut **   <a name="BedrockAgentCore-Type-BrowserAction-keyShortcut"></a>
Press a key combination.  
Type: [KeyShortcutArguments](API_KeyShortcutArguments.md) object  
Required: No

 ** keyType **   <a name="BedrockAgentCore-Type-BrowserAction-keyType"></a>
Type a string of text.  
Type: [KeyTypeArguments](API_KeyTypeArguments.md) object  
Required: No

 ** mouseClick **   <a name="BedrockAgentCore-Type-BrowserAction-mouseClick"></a>
Click at the specified coordinates.  
Type: [MouseClickArguments](API_MouseClickArguments.md) object  
Required: No

 ** mouseDrag **   <a name="BedrockAgentCore-Type-BrowserAction-mouseDrag"></a>
Drag from a start position to an end position.  
Type: [MouseDragArguments](API_MouseDragArguments.md) object  
Required: No

 ** mouseMove **   <a name="BedrockAgentCore-Type-BrowserAction-mouseMove"></a>
Move the cursor to the specified coordinates.  
Type: [MouseMoveArguments](API_MouseMoveArguments.md) object  
Required: No

 ** mouseScroll **   <a name="BedrockAgentCore-Type-BrowserAction-mouseScroll"></a>
Scroll at the specified position.  
Type: [MouseScrollArguments](API_MouseScrollArguments.md) object  
Required: No

 ** screenshot **   <a name="BedrockAgentCore-Type-BrowserAction-screenshot"></a>
Capture a full-screen screenshot.  
Type: [ScreenshotArguments](API_ScreenshotArguments.md) object  
Required: No

## See Also
<a name="API_BrowserAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserAction) 