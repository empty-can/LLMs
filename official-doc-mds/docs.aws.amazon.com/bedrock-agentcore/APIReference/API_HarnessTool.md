

# HarnessTool
<a name="API_HarnessTool"></a>

A tool available to the agent loop.

## Contents
<a name="API_HarnessTool_Contents"></a>

 ** type **   <a name="BedrockAgentCore-Type-HarnessTool-type"></a>
The type of tool.  
Type: String  
Valid Values: `remote_mcp | agentcore_browser | agentcore_gateway | inline_function | agentcore_code_interpreter`   
Required: Yes

 ** config **   <a name="BedrockAgentCore-Type-HarnessTool-config"></a>
Tool-specific configuration.  
Type: [HarnessToolConfiguration](API_HarnessToolConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-HarnessTool-name"></a>
Unique name for the tool. If not provided, a name will be inferred or generated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## See Also
<a name="API_HarnessTool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessTool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessTool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessTool) 