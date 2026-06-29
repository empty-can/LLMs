

# Tool
<a name="API_agent_Tool"></a>

Contains configurations for a tool that a model can use when generating a response. For more information, see [Use a tool to complete an Amazon Bedrock model response](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html).

## Contents
<a name="API_agent_Tool_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cachePoint **   <a name="bedrock-Type-agent_Tool-cachePoint"></a>
Creates a cache checkpoint within a tool designation  
Type: [CachePointBlock](API_agent_CachePointBlock.md) object  
Required: No

 ** toolSpec **   <a name="bedrock-Type-agent_Tool-toolSpec"></a>
The specification for the tool.  
Type: [ToolSpecification](API_agent_ToolSpecification.md) object  
Required: No

## See Also
<a name="API_agent_Tool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/Tool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/Tool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/Tool) 