

# HarnessContentBlock
<a name="API_HarnessContentBlock"></a>

A content block within a message.

## Contents
<a name="API_HarnessContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoningContent **   <a name="BedrockAgentCore-Type-HarnessContentBlock-reasoningContent"></a>
Model reasoning content.  
Type: [HarnessReasoningContentBlock](API_HarnessReasoningContentBlock.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessContentBlock-text"></a>
Text content.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** toolResult **   <a name="BedrockAgentCore-Type-HarnessContentBlock-toolResult"></a>
A tool execution result.  
Type: [HarnessToolResultBlock](API_HarnessToolResultBlock.md) object  
Required: No

 ** toolUse **   <a name="BedrockAgentCore-Type-HarnessContentBlock-toolUse"></a>
A tool use request from the model.  
Type: [HarnessToolUseBlock](API_HarnessToolUseBlock.md) object  
Required: No

## See Also
<a name="API_HarnessContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlock) 