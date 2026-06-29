

# ToolDescriptionSource
<a name="API_ToolDescriptionSource"></a>

The source of tool descriptions, either inline text or from a configuration bundle.

## Contents
<a name="API_ToolDescriptionSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBundle **   <a name="BedrockAgentCore-Type-ToolDescriptionSource-configurationBundle"></a>
Tool descriptions sourced from a configuration bundle version.  
Type: [ToolDescriptionConfigurationBundle](API_ToolDescriptionConfigurationBundle.md) object  
Required: No

 ** toolDescriptionText **   <a name="BedrockAgentCore-Type-ToolDescriptionSource-toolDescriptionText"></a>
Tool descriptions provided as inline text.  
Type: [ToolDescriptionTextInput](API_ToolDescriptionTextInput.md) object  
Required: No

## See Also
<a name="API_ToolDescriptionSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionSource) 