

# FlowTraceDependencyEvent
<a name="API_agent-runtime_FlowTraceDependencyEvent"></a>

Contains information about a dependency trace event in the flow.

## Contents
<a name="API_agent-runtime_FlowTraceDependencyEvent_Contents"></a>

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowTraceDependencyEvent-nodeName"></a>
The name of the node that generated the dependency trace.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_FlowTraceDependencyEvent-timestamp"></a>
The date and time that the dependency trace was generated.  
Type: Timestamp  
Required: Yes

 ** traceElements **   <a name="bedrock-Type-agent-runtime_FlowTraceDependencyEvent-traceElements"></a>
The trace elements containing detailed information about the dependency.  
Type: [TraceElements](API_agent-runtime_TraceElements.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_agent-runtime_FlowTraceDependencyEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceDependencyEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceDependencyEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceDependencyEvent) 