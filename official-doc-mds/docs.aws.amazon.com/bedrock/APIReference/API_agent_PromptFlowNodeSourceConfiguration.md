

# PromptFlowNodeSourceConfiguration
<a name="API_agent_PromptFlowNodeSourceConfiguration"></a>

Contains configurations for a prompt and whether it is from Prompt management or defined inline.

## Contents
<a name="API_agent_PromptFlowNodeSourceConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inline **   <a name="bedrock-Type-agent_PromptFlowNodeSourceConfiguration-inline"></a>
Contains configurations for a prompt that is defined inline  
Type: [PromptFlowNodeInlineConfiguration](API_agent_PromptFlowNodeInlineConfiguration.md) object  
Required: No

 ** resource **   <a name="bedrock-Type-agent_PromptFlowNodeSourceConfiguration-resource"></a>
Contains configurations for a prompt from Prompt management.  
Type: [PromptFlowNodeResourceConfiguration](API_agent_PromptFlowNodeResourceConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_PromptFlowNodeSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptFlowNodeSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptFlowNodeSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptFlowNodeSourceConfiguration) 