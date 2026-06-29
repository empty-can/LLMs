

# FlowTraceNodeOutputEvent
<a name="API_agent-runtime_FlowTraceNodeOutputEvent"></a>

Contains information about the output from a node. For more information, see [Track each step in your prompt flow by viewing its trace in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html).

## Contents
<a name="API_agent-runtime_FlowTraceNodeOutputEvent_Contents"></a>

 ** fields **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputEvent-fields"></a>
An array of objects containing information about each field in the output.  
Type: Array of [FlowTraceNodeOutputField](API_agent-runtime_FlowTraceNodeOutputField.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputEvent-nodeName"></a>
The name of the node that yielded the output.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputEvent-timestamp"></a>
The date and time that the trace was returned.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_FlowTraceNodeOutputEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceNodeOutputEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceNodeOutputEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceNodeOutputEvent) 