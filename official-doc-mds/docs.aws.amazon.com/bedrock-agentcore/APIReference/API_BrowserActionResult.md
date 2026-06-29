

# BrowserActionResult
<a name="API_BrowserActionResult"></a>

The result of a browser action execution. Exactly one member is set, matching the action that was performed.

## Contents
<a name="API_BrowserActionResult_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** keyPress **   <a name="BedrockAgentCore-Type-BrowserActionResult-keyPress"></a>
The result of a key press action.  
Type: [KeyPressResult](API_KeyPressResult.md) object  
Required: No

 ** keyShortcut **   <a name="BedrockAgentCore-Type-BrowserActionResult-keyShortcut"></a>
The result of a key shortcut action.  
Type: [KeyShortcutResult](API_KeyShortcutResult.md) object  
Required: No

 ** keyType **   <a name="BedrockAgentCore-Type-BrowserActionResult-keyType"></a>
The result of a key type action.  
Type: [KeyTypeResult](API_KeyTypeResult.md) object  
Required: No

 ** mouseClick **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseClick"></a>
The result of a mouse click action.  
Type: [MouseClickResult](API_MouseClickResult.md) object  
Required: No

 ** mouseDrag **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseDrag"></a>
The result of a mouse drag action.  
Type: [MouseDragResult](API_MouseDragResult.md) object  
Required: No

 ** mouseMove **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseMove"></a>
The result of a mouse move action.  
Type: [MouseMoveResult](API_MouseMoveResult.md) object  
Required: No

 ** mouseScroll **   <a name="BedrockAgentCore-Type-BrowserActionResult-mouseScroll"></a>
The result of a mouse scroll action.  
Type: [MouseScrollResult](API_MouseScrollResult.md) object  
Required: No

 ** screenshot **   <a name="BedrockAgentCore-Type-BrowserActionResult-screenshot"></a>
The result of a screenshot action.  
Type: [ScreenshotResult](API_ScreenshotResult.md) object  
Required: No

## See Also
<a name="API_BrowserActionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserActionResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserActionResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserActionResult) 