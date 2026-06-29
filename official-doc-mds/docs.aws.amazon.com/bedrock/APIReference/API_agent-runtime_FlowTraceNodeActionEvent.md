

# FlowTraceNodeActionEvent
<a name="API_agent-runtime_FlowTraceNodeActionEvent"></a>

Contains information about an action (operation) called by a node in an Amazon Bedrock flow. The service generates action events for calls made by prompt nodes, agent nodes, and AWS Lambda nodes. 

## Contents
<a name="API_agent-runtime_FlowTraceNodeActionEvent_Contents"></a>

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-nodeName"></a>
The name of the node that called the operation.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** operationName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-operationName"></a>
The name of the operation that the node called.  
Type: String  
Required: Yes

 ** requestId **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-requestId"></a>
The ID of the request that the node made to the operation.  
Type: String  
Required: Yes

 ** serviceName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-serviceName"></a>
The name of the service that the node called.  
Type: String  
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-timestamp"></a>
The date and time that the operation was called.  
Type: Timestamp  
Required: Yes

 ** operationRequest **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-operationRequest"></a>
The request payload sent to the downstream service.  
Type: JSON value  
Required: No

 ** operationResponse **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeActionEvent-operationResponse"></a>
The response payload received from the downstream service.  
Type: JSON value  
Required: No

## See Also
<a name="API_agent-runtime_FlowTraceNodeActionEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceNodeActionEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceNodeActionEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceNodeActionEvent) 