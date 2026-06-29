

# FlowValidation
<a name="API_agent_FlowValidation"></a>

Contains information about validation of the flow.

This data type is used in the following API operations:
+  [GetFlow response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html#API_agent_GetFlow_ResponseSyntax) 
+  [GetFlowVersion response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlowVersion.html#API_agent_GetFlowVersion_ResponseSyntax) 

## Contents
<a name="API_agent_FlowValidation_Contents"></a>

 ** message **   <a name="bedrock-Type-agent_FlowValidation-message"></a>
A message describing the validation error.  
Type: String  
Pattern: `[\s\S]+`   
Required: Yes

 ** severity **   <a name="bedrock-Type-agent_FlowValidation-severity"></a>
The severity of the issue described in the message.  
Type: String  
Valid Values: `Warning | Error`   
Required: Yes

 ** details **   <a name="bedrock-Type-agent_FlowValidation-details"></a>
Specific details about the validation issue encountered in the flow.  
Type: [FlowValidationDetails](API_agent_FlowValidationDetails.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** type **   <a name="bedrock-Type-agent_FlowValidation-type"></a>
The type of validation issue encountered in the flow.  
Type: String  
Valid Values: `CyclicConnection | DuplicateConnections | DuplicateConditionExpression | UnreachableNode | UnknownConnectionSource | UnknownConnectionSourceOutput | UnknownConnectionTarget | UnknownConnectionTargetInput | UnknownConnectionCondition | MalformedConditionExpression | MalformedNodeInputExpression | MismatchedNodeInputType | MismatchedNodeOutputType | IncompatibleConnectionDataType | MissingConnectionConfiguration | MissingDefaultCondition | MissingEndingNodes | MissingNodeConfiguration | MissingNodeInput | MissingNodeOutput | MissingStartingNodes | MultipleNodeInputConnections | UnfulfilledNodeInput | UnsatisfiedConnectionConditions | Unspecified | UnknownNodeInput | UnknownNodeOutput | MissingLoopInputNode | MissingLoopControllerNode | MultipleLoopInputNodes | MultipleLoopControllerNodes | LoopIncompatibleNodeType | InvalidLoopBoundary`   
Required: No

## See Also
<a name="API_agent_FlowValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowValidation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowValidation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowValidation) 