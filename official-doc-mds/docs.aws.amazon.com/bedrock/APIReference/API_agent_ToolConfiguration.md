

# ToolConfiguration
<a name="API_agent_ToolConfiguration"></a>

Configuration information for the tools that the model can use when generating a response. For more information, see [Use a tool to complete an Amazon Bedrock model response](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html).

## Contents
<a name="API_agent_ToolConfiguration_Contents"></a>

 ** tools **   <a name="bedrock-Type-agent_ToolConfiguration-tools"></a>
An array of tools to pass to a model.  
Type: Array of [Tool](API_agent_Tool.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

 ** toolChoice **   <a name="bedrock-Type-agent_ToolConfiguration-toolChoice"></a>
Defines which tools the model should request when invoked.  
Type: [ToolChoice](API_agent_ToolChoice.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_agent_ToolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ToolConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ToolConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ToolConfiguration) 