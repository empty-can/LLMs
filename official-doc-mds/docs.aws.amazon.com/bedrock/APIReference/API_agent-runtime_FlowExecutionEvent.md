

# FlowExecutionEvent
<a name="API_agent-runtime_FlowExecutionEvent"></a>

Represents an event that occurred during an flow execution. This is a union type that can contain one of several event types, such as node input and output events; flow input and output events; condition node result events, or failure events.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowExecutionEvent_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conditionResultEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-conditionResultEvent"></a>
Contains information about a condition evaluation result during the flow execution. This event is generated when a condition node in the flow evaluates its conditions.  
Type: [ConditionResultEvent](API_agent-runtime_ConditionResultEvent.md) object  
Required: No

 ** flowFailureEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-flowFailureEvent"></a>
Contains information about a failure that occurred at the flow level during execution.  
Type: [FlowFailureEvent](API_agent-runtime_FlowFailureEvent.md) object  
Required: No

 ** flowInputEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-flowInputEvent"></a>
Contains information about the inputs provided to the flow at the start of execution.  
Type: [FlowExecutionInputEvent](API_agent-runtime_FlowExecutionInputEvent.md) object  
Required: No

 ** flowOutputEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-flowOutputEvent"></a>
Contains information about the outputs produced by the flow at the end of execution.  
Type: [FlowExecutionOutputEvent](API_agent-runtime_FlowExecutionOutputEvent.md) object  
Required: No

 ** nodeActionEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-nodeActionEvent"></a>
Contains information about an action (operation) called by a node during execution.  
Type: [NodeActionEvent](API_agent-runtime_NodeActionEvent.md) object  
Required: No

 ** nodeDependencyEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-nodeDependencyEvent"></a>
Contains information about an internal trace of a specific node during execution.  
Type: [NodeDependencyEvent](API_agent-runtime_NodeDependencyEvent.md) object  
Required: No

 ** nodeFailureEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-nodeFailureEvent"></a>
Contains information about a failure that occurred at a specific node during execution.  
Type: [NodeFailureEvent](API_agent-runtime_NodeFailureEvent.md) object  
Required: No

 ** nodeInputEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-nodeInputEvent"></a>
Contains information about the inputs provided to a specific node during execution.  
Type: [NodeInputEvent](API_agent-runtime_NodeInputEvent.md) object  
Required: No

 ** nodeOutputEvent **   <a name="bedrock-Type-agent-runtime_FlowExecutionEvent-nodeOutputEvent"></a>
Contains information about the outputs produced by a specific node during execution.  
Type: [NodeOutputEvent](API_agent-runtime_NodeOutputEvent.md) object  
Required: No

## See Also
<a name="API_agent-runtime_FlowExecutionEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowExecutionEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowExecutionEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowExecutionEvent) 