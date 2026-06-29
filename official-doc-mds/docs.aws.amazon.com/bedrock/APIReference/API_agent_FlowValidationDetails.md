

# FlowValidationDetails
<a name="API_agent_FlowValidationDetails"></a>

A union type containing various possible validation issues in the flow.

## Contents
<a name="API_agent_FlowValidationDetails_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cyclicConnection **   <a name="bedrock-Type-agent_FlowValidationDetails-cyclicConnection"></a>
Details about a cyclic connection in the flow.  
Type: [CyclicConnectionFlowValidationDetails](API_agent_CyclicConnectionFlowValidationDetails.md) object  
Required: No

 ** duplicateConditionExpression **   <a name="bedrock-Type-agent_FlowValidationDetails-duplicateConditionExpression"></a>
Details about duplicate condition expressions in a node.  
Type: [DuplicateConditionExpressionFlowValidationDetails](API_agent_DuplicateConditionExpressionFlowValidationDetails.md) object  
Required: No

 ** duplicateConnections **   <a name="bedrock-Type-agent_FlowValidationDetails-duplicateConnections"></a>
Details about duplicate connections between nodes.  
Type: [DuplicateConnectionsFlowValidationDetails](API_agent_DuplicateConnectionsFlowValidationDetails.md) object  
Required: No

 ** incompatibleConnectionDataType **   <a name="bedrock-Type-agent_FlowValidationDetails-incompatibleConnectionDataType"></a>
Details about incompatible data types in a connection.  
Type: [IncompatibleConnectionDataTypeFlowValidationDetails](API_agent_IncompatibleConnectionDataTypeFlowValidationDetails.md) object  
Required: No

 ** invalidLoopBoundary **   <a name="bedrock-Type-agent_FlowValidationDetails-invalidLoopBoundary"></a>
Details about a flow that includes connections that violate loop boundary rules.  
Type: [InvalidLoopBoundaryFlowValidationDetails](API_agent_InvalidLoopBoundaryFlowValidationDetails.md) object  
Required: No

 ** loopIncompatibleNodeType **   <a name="bedrock-Type-agent_FlowValidationDetails-loopIncompatibleNodeType"></a>
Details about a flow that includes incompatible node types in a DoWhile loop.  
Type: [LoopIncompatibleNodeTypeFlowValidationDetails](API_agent_LoopIncompatibleNodeTypeFlowValidationDetails.md) object  
Required: No

 ** malformedConditionExpression **   <a name="bedrock-Type-agent_FlowValidationDetails-malformedConditionExpression"></a>
Details about a malformed condition expression in a node.  
Type: [MalformedConditionExpressionFlowValidationDetails](API_agent_MalformedConditionExpressionFlowValidationDetails.md) object  
Required: No

 ** malformedNodeInputExpression **   <a name="bedrock-Type-agent_FlowValidationDetails-malformedNodeInputExpression"></a>
Details about a malformed input expression in a node.  
Type: [MalformedNodeInputExpressionFlowValidationDetails](API_agent_MalformedNodeInputExpressionFlowValidationDetails.md) object  
Required: No

 ** mismatchedNodeInputType **   <a name="bedrock-Type-agent_FlowValidationDetails-mismatchedNodeInputType"></a>
Details about mismatched input data types in a node.  
Type: [MismatchedNodeInputTypeFlowValidationDetails](API_agent_MismatchedNodeInputTypeFlowValidationDetails.md) object  
Required: No

 ** mismatchedNodeOutputType **   <a name="bedrock-Type-agent_FlowValidationDetails-mismatchedNodeOutputType"></a>
Details about mismatched output data types in a node.  
Type: [MismatchedNodeOutputTypeFlowValidationDetails](API_agent_MismatchedNodeOutputTypeFlowValidationDetails.md) object  
Required: No

 ** missingConnectionConfiguration **   <a name="bedrock-Type-agent_FlowValidationDetails-missingConnectionConfiguration"></a>
Details about missing configuration for a connection.  
Type: [MissingConnectionConfigurationFlowValidationDetails](API_agent_MissingConnectionConfigurationFlowValidationDetails.md) object  
Required: No

 ** missingDefaultCondition **   <a name="bedrock-Type-agent_FlowValidationDetails-missingDefaultCondition"></a>
Details about a missing default condition in a conditional node.  
Type: [MissingDefaultConditionFlowValidationDetails](API_agent_MissingDefaultConditionFlowValidationDetails.md) object  
Required: No

 ** missingEndingNodes **   <a name="bedrock-Type-agent_FlowValidationDetails-missingEndingNodes"></a>
Details about missing ending nodes in the flow.  
Type: [MissingEndingNodesFlowValidationDetails](API_agent_MissingEndingNodesFlowValidationDetails.md) object  
Required: No

 ** missingLoopControllerNode **   <a name="bedrock-Type-agent_FlowValidationDetails-missingLoopControllerNode"></a>
Details about a flow that's missing a required `LoopController` node in a DoWhile loop.  
Type: [MissingLoopControllerNodeFlowValidationDetails](API_agent_MissingLoopControllerNodeFlowValidationDetails.md) object  
Required: No

 ** missingLoopInputNode **   <a name="bedrock-Type-agent_FlowValidationDetails-missingLoopInputNode"></a>
Details about a flow that's missing a required `LoopInput` node in a DoWhile loop.  
Type: [MissingLoopInputNodeFlowValidationDetails](API_agent_MissingLoopInputNodeFlowValidationDetails.md) object  
Required: No

 ** missingNodeConfiguration **   <a name="bedrock-Type-agent_FlowValidationDetails-missingNodeConfiguration"></a>
Details about missing configuration for a node.  
Type: [MissingNodeConfigurationFlowValidationDetails](API_agent_MissingNodeConfigurationFlowValidationDetails.md) object  
Required: No

 ** missingNodeInput **   <a name="bedrock-Type-agent_FlowValidationDetails-missingNodeInput"></a>
Details about a missing required input in a node.  
Type: [MissingNodeInputFlowValidationDetails](API_agent_MissingNodeInputFlowValidationDetails.md) object  
Required: No

 ** missingNodeOutput **   <a name="bedrock-Type-agent_FlowValidationDetails-missingNodeOutput"></a>
Details about a missing required output in a node.  
Type: [MissingNodeOutputFlowValidationDetails](API_agent_MissingNodeOutputFlowValidationDetails.md) object  
Required: No

 ** missingStartingNodes **   <a name="bedrock-Type-agent_FlowValidationDetails-missingStartingNodes"></a>
Details about missing starting nodes in the flow.  
Type: [MissingStartingNodesFlowValidationDetails](API_agent_MissingStartingNodesFlowValidationDetails.md) object  
Required: No

 ** multipleLoopControllerNodes **   <a name="bedrock-Type-agent_FlowValidationDetails-multipleLoopControllerNodes"></a>
Details about a flow that contains multiple `LoopController` nodes in a DoWhile loop.  
Type: [MultipleLoopControllerNodesFlowValidationDetails](API_agent_MultipleLoopControllerNodesFlowValidationDetails.md) object  
Required: No

 ** multipleLoopInputNodes **   <a name="bedrock-Type-agent_FlowValidationDetails-multipleLoopInputNodes"></a>
Details about a flow that contains multiple `LoopInput` nodes in a DoWhile loop.  
Type: [MultipleLoopInputNodesFlowValidationDetails](API_agent_MultipleLoopInputNodesFlowValidationDetails.md) object  
Required: No

 ** multipleNodeInputConnections **   <a name="bedrock-Type-agent_FlowValidationDetails-multipleNodeInputConnections"></a>
Details about multiple connections to a single node input.  
Type: [MultipleNodeInputConnectionsFlowValidationDetails](API_agent_MultipleNodeInputConnectionsFlowValidationDetails.md) object  
Required: No

 ** unfulfilledNodeInput **   <a name="bedrock-Type-agent_FlowValidationDetails-unfulfilledNodeInput"></a>
Details about an unfulfilled node input with no valid connections.  
Type: [UnfulfilledNodeInputFlowValidationDetails](API_agent_UnfulfilledNodeInputFlowValidationDetails.md) object  
Required: No

 ** unknownConnectionCondition **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownConnectionCondition"></a>
Details about an unknown condition for a connection.  
Type: [UnknownConnectionConditionFlowValidationDetails](API_agent_UnknownConnectionConditionFlowValidationDetails.md) object  
Required: No

 ** unknownConnectionSource **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownConnectionSource"></a>
Details about an unknown source node for a connection.  
Type: [UnknownConnectionSourceFlowValidationDetails](API_agent_UnknownConnectionSourceFlowValidationDetails.md) object  
Required: No

 ** unknownConnectionSourceOutput **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownConnectionSourceOutput"></a>
Details about an unknown source output for a connection.  
Type: [UnknownConnectionSourceOutputFlowValidationDetails](API_agent_UnknownConnectionSourceOutputFlowValidationDetails.md) object  
Required: No

 ** unknownConnectionTarget **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownConnectionTarget"></a>
Details about an unknown target node for a connection.  
Type: [UnknownConnectionTargetFlowValidationDetails](API_agent_UnknownConnectionTargetFlowValidationDetails.md) object  
Required: No

 ** unknownConnectionTargetInput **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownConnectionTargetInput"></a>
Details about an unknown target input for a connection.  
Type: [UnknownConnectionTargetInputFlowValidationDetails](API_agent_UnknownConnectionTargetInputFlowValidationDetails.md) object  
Required: No

 ** unknownNodeInput **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownNodeInput"></a>
Details about an unknown input for a node.  
Type: [UnknownNodeInputFlowValidationDetails](API_agent_UnknownNodeInputFlowValidationDetails.md) object  
Required: No

 ** unknownNodeOutput **   <a name="bedrock-Type-agent_FlowValidationDetails-unknownNodeOutput"></a>
Details about an unknown output for a node.  
Type: [UnknownNodeOutputFlowValidationDetails](API_agent_UnknownNodeOutputFlowValidationDetails.md) object  
Required: No

 ** unreachableNode **   <a name="bedrock-Type-agent_FlowValidationDetails-unreachableNode"></a>
Details about an unreachable node in the flow.  
Type: [UnreachableNodeFlowValidationDetails](API_agent_UnreachableNodeFlowValidationDetails.md) object  
Required: No

 ** unsatisfiedConnectionConditions **   <a name="bedrock-Type-agent_FlowValidationDetails-unsatisfiedConnectionConditions"></a>
Details about unsatisfied conditions for a connection.  
Type: [UnsatisfiedConnectionConditionsFlowValidationDetails](API_agent_UnsatisfiedConnectionConditionsFlowValidationDetails.md) object  
Required: No

 ** unspecified **   <a name="bedrock-Type-agent_FlowValidationDetails-unspecified"></a>
Details about an unspecified validation.  
Type: [UnspecifiedFlowValidationDetails](API_agent_UnspecifiedFlowValidationDetails.md) object  
Required: No

## See Also
<a name="API_agent_FlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowValidationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowValidationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowValidationDetails) 