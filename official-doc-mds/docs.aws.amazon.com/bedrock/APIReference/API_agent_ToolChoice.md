

# ToolChoice
<a name="API_agent_ToolChoice"></a>

Defines which tools the model should request when invoked. For more information, see [Use a tool to complete an Amazon Bedrock model response](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html).

## Contents
<a name="API_agent_ToolChoice_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** any **   <a name="bedrock-Type-agent_ToolChoice-any"></a>
Defines tools, at least one of which must be requested by the model. No text is generated but the results of tool use are sent back to the model to help generate a response.  
Type: [AnyToolChoice](API_agent_AnyToolChoice.md) object  
Required: No

 ** auto **   <a name="bedrock-Type-agent_ToolChoice-auto"></a>
Defines tools. The model automatically decides whether to call a tool or to generate text instead.  
Type: [AutoToolChoice](API_agent_AutoToolChoice.md) object  
Required: No

 ** tool **   <a name="bedrock-Type-agent_ToolChoice-tool"></a>
Defines a specific tool that the model must request. No text is generated but the results of tool use are sent back to the model to help generate a response.  
Type: [SpecificToolChoice](API_agent_SpecificToolChoice.md) object  
Required: No

## See Also
<a name="API_agent_ToolChoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ToolChoice) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ToolChoice) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ToolChoice) 