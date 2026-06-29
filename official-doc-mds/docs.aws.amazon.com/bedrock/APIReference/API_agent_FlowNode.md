

# FlowNode
<a name="API_agent_FlowNode"></a>

Contains configurations about a node in the flow.

## Contents
<a name="API_agent_FlowNode_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_FlowNode-name"></a>
A name for the node.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent_FlowNode-type"></a>
The type of node. This value must match the name of the key that you provide in the configuration you provide in the `FlowNodeConfiguration` field.  
Type: String  
Valid Values: `Input | Output | KnowledgeBase | Condition | Lex | Prompt | LambdaFunction | Storage | Agent | Retrieval | Iterator | Collector | InlineCode | Loop | LoopInput | LoopController`   
Required: Yes

 ** configuration **   <a name="bedrock-Type-agent_FlowNode-configuration"></a>
Contains configurations for the node.  
Type: [FlowNodeConfiguration](API_agent_FlowNodeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** inputs **   <a name="bedrock-Type-agent_FlowNode-inputs"></a>
An array of objects, each of which contains information about an input into the node.  
Type: Array of [FlowNodeInput](API_agent_FlowNodeInput.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 20 items.  
Required: No

 ** outputs **   <a name="bedrock-Type-agent_FlowNode-outputs"></a>
A list of objects, each of which contains information about an output from the node.  
Type: Array of [FlowNodeOutput](API_agent_FlowNodeOutput.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_agent_FlowNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowNode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowNode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowNode) 