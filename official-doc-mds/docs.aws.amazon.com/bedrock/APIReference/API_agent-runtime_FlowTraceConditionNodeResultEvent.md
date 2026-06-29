

# FlowTraceConditionNodeResultEvent
<a name="API_agent-runtime_FlowTraceConditionNodeResultEvent"></a>

Contains information about an output from a condition node. For more information, see [Track each step in your prompt flow by viewing its trace in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html).

## Contents
<a name="API_agent-runtime_FlowTraceConditionNodeResultEvent_Contents"></a>

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowTraceConditionNodeResultEvent-nodeName"></a>
The name of the condition node.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** satisfiedConditions **   <a name="bedrock-Type-agent-runtime_FlowTraceConditionNodeResultEvent-satisfiedConditions"></a>
An array of objects containing information about the conditions that were satisfied.  
Type: Array of [FlowTraceCondition](API_agent-runtime_FlowTraceCondition.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_FlowTraceConditionNodeResultEvent-timestamp"></a>
The date and time that the trace was returned.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_FlowTraceConditionNodeResultEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceConditionNodeResultEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceConditionNodeResultEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceConditionNodeResultEvent) 