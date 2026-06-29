

# ToolDescriptionConfigurationBundle
<a name="API_ToolDescriptionConfigurationBundle"></a>

Tool descriptions sourced from a configuration bundle version.

## Contents
<a name="API_ToolDescriptionConfigurationBundle_Contents"></a>

 ** bundleArn **   <a name="BedrockAgentCore-Type-ToolDescriptionConfigurationBundle-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** tools **   <a name="BedrockAgentCore-Type-ToolDescriptionConfigurationBundle-tools"></a>
The list of tool entries mapping tool names to their JSON paths within the bundle.  
Type: Array of [ConfigurationBundleToolEntry](API_ConfigurationBundleToolEntry.md) objects  
Required: Yes

 ** versionId **   <a name="BedrockAgentCore-Type-ToolDescriptionConfigurationBundle-versionId"></a>
The version identifier of the configuration bundle.  
Type: String  
Required: Yes

## See Also
<a name="API_ToolDescriptionConfigurationBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionConfigurationBundle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionConfigurationBundle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionConfigurationBundle) 