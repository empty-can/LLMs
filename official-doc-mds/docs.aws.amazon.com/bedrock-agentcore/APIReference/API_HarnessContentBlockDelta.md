

# HarnessContentBlockDelta
<a name="API_HarnessContentBlockDelta"></a>

A delta update to a content block.

## Contents
<a name="API_HarnessContentBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoningContent **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-reasoningContent"></a>
A reasoning content delta.  
Type: [HarnessReasoningContentBlockDelta](API_HarnessReasoningContentBlockDelta.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-text"></a>
A text delta.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** toolResult **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-toolResult"></a>
A tool result delta.  
Type: Array of [HarnessToolResultBlockDelta](API_HarnessToolResultBlockDelta.md) objects  
Required: No

 ** toolUse **   <a name="BedrockAgentCore-Type-HarnessContentBlockDelta-toolUse"></a>
A tool use input delta.  
Type: [HarnessToolUseBlockDelta](API_HarnessToolUseBlockDelta.md) object  
Required: No

## See Also
<a name="API_HarnessContentBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockDelta) 