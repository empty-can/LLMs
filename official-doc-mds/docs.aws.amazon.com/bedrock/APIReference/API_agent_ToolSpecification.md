

# ToolSpecification
<a name="API_agent_ToolSpecification"></a>

Contains a specification for a tool. For more information, see [Use a tool to complete an Amazon Bedrock model response](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html).

## Contents
<a name="API_agent_ToolSpecification_Contents"></a>

 ** inputSchema **   <a name="bedrock-Type-agent_ToolSpecification-inputSchema"></a>
The input schema for the tool.  
Type: [ToolInputSchema](API_agent_ToolInputSchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrock-Type-agent_ToolSpecification-name"></a>
The name of the tool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]*`   
Required: Yes

 ** description **   <a name="bedrock-Type-agent_ToolSpecification-description"></a>
The description of the tool.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** strict **   <a name="bedrock-Type-agent_ToolSpecification-strict"></a>
Whether the tool schema is strictly enforced.  
Type: Boolean  
Required: No

## See Also
<a name="API_agent_ToolSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ToolSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ToolSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ToolSpecification) 