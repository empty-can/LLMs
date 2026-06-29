

# ToolDescriptionInput
<a name="API_ToolDescriptionInput"></a>

A tool description input containing the tool name and its current description.

## Contents
<a name="API_ToolDescriptionInput_Contents"></a>

 ** toolDescription **   <a name="BedrockAgentCore-Type-ToolDescriptionInput-toolDescription"></a>
The current description of the tool to optimize.  
Type: [ToolDescriptionConfig](API_ToolDescriptionConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** toolName **   <a name="BedrockAgentCore-Type-ToolDescriptionInput-toolName"></a>
The name of the tool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_\-\.]+`   
Required: Yes

## See Also
<a name="API_ToolDescriptionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionInput) 