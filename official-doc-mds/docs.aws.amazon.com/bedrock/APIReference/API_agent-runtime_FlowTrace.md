

# FlowTrace
<a name="API_agent-runtime_FlowTrace"></a>

Contains information about an input or output for a node in the flow. For more information, see [Track each step in your prompt flow by viewing its trace in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html).

## Contents
<a name="API_agent-runtime_FlowTrace_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conditionNodeResultTrace **   <a name="bedrock-Type-agent-runtime_FlowTrace-conditionNodeResultTrace"></a>
Contains information about an output from a condition node.  
Type: [FlowTraceConditionNodeResultEvent](API_agent-runtime_FlowTraceConditionNodeResultEvent.md) object  
Required: No

 ** nodeActionTrace **   <a name="bedrock-Type-agent-runtime_FlowTrace-nodeActionTrace"></a>
Contains information about an action (operation) called by a node.  
Type: [FlowTraceNodeActionEvent](API_agent-runtime_FlowTraceNodeActionEvent.md) object  
Required: No

 ** nodeDependencyTrace **   <a name="bedrock-Type-agent-runtime_FlowTrace-nodeDependencyTrace"></a>
Contains information about an internal trace of a node.  
Type: [FlowTraceDependencyEvent](API_agent-runtime_FlowTraceDependencyEvent.md) object  
Required: No

 ** nodeInputTrace **   <a name="bedrock-Type-agent-runtime_FlowTrace-nodeInputTrace"></a>
Contains information about the input into a node.  
Type: [FlowTraceNodeInputEvent](API_agent-runtime_FlowTraceNodeInputEvent.md) object  
Required: No

 ** nodeOutputTrace **   <a name="bedrock-Type-agent-runtime_FlowTrace-nodeOutputTrace"></a>
Contains information about the output from a node.  
Type: [FlowTraceNodeOutputEvent](API_agent-runtime_FlowTraceNodeOutputEvent.md) object  
Required: No

## See Also
<a name="API_agent-runtime_FlowTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTrace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTrace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTrace) 