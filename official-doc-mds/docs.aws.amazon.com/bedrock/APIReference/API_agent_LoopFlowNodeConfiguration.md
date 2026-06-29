

# LoopFlowNodeConfiguration
<a name="API_agent_LoopFlowNodeConfiguration"></a>

Contains configurations for the nodes of a DoWhile loop in your flow.

A DoWhile loop is made up of the following nodes:
+  `Loop` - The container node that holds the loop's flow definition. This node encompasses the entire loop structure.
+  `LoopInput` - The entry point node for the loop. This node receives inputs from nodes outside the loop and from previous loop iterations.
+ Body nodes - The processing nodes that execute within each loop iteration. These can be nodes for handling data in your flow, such as a prompt or Lambda function nodes. Some node types aren't supported inside a DoWhile loop body. For more information, see [LoopIncompatibleNodeTypeFlowValidationDetails](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_LoopIncompatibleNodeTypeFlowValidationDetails.html).
+  `LoopController` - The node that evaluates whether the loop should continue or exit based on a condition.

These nodes work together to create a loop that runs at least once and continues until a specified condition is met or a maximum number of iterations is reached.

## Contents
<a name="API_agent_LoopFlowNodeConfiguration_Contents"></a>

 ** definition **   <a name="bedrock-Type-agent_LoopFlowNodeConfiguration-definition"></a>
The definition of the DoWhile loop nodes and connections between nodes in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object  
Required: Yes

## See Also
<a name="API_agent_LoopFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/LoopFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/LoopFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/LoopFlowNodeConfiguration) 