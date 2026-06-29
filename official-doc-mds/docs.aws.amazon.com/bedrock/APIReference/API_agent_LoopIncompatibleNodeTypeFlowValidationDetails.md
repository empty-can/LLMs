

# LoopIncompatibleNodeTypeFlowValidationDetails
<a name="API_agent_LoopIncompatibleNodeTypeFlowValidationDetails"></a>

Details about a flow that contains an incompatible node in a DoWhile loop.

## Contents
<a name="API_agent_LoopIncompatibleNodeTypeFlowValidationDetails_Contents"></a>

 ** incompatibleNodeName **   <a name="bedrock-Type-agent_LoopIncompatibleNodeTypeFlowValidationDetails-incompatibleNodeName"></a>
The node that's incompatible in the DoWhile loop.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** incompatibleNodeType **   <a name="bedrock-Type-agent_LoopIncompatibleNodeTypeFlowValidationDetails-incompatibleNodeType"></a>
The node type of the incompatible node in the DoWhile loop. Some node types, like a condition node, aren't allowed in a DoWhile loop.  
Type: String  
Valid Values: `Input | Condition | Iterator | Collector`   
Required: Yes

 ** node **   <a name="bedrock-Type-agent_LoopIncompatibleNodeTypeFlowValidationDetails-node"></a>
The `Loop` container node that contains an incompatible node.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

## See Also
<a name="API_agent_LoopIncompatibleNodeTypeFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/LoopIncompatibleNodeTypeFlowValidationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/LoopIncompatibleNodeTypeFlowValidationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/LoopIncompatibleNodeTypeFlowValidationDetails) 