

# FlowTraceNodeInputExecutionChainItem
<a name="API_agent-runtime_FlowTraceNodeInputExecutionChainItem"></a>

Represents an item in the execution chain for flow trace node input tracking.

## Contents
<a name="API_agent-runtime_FlowTraceNodeInputExecutionChainItem_Contents"></a>

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputExecutionChainItem-nodeName"></a>
The name of the node in the execution chain.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputExecutionChainItem-type"></a>
The type of execution chain item. Supported values are Iterator and Loop.  
Type: String  
Valid Values: `Iterator | Loop`   
Required: Yes

 ** index **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputExecutionChainItem-index"></a>
The index position of this item in the execution chain.  
Type: Integer  
Required: No

## See Also
<a name="API_agent-runtime_FlowTraceNodeInputExecutionChainItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceNodeInputExecutionChainItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceNodeInputExecutionChainItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceNodeInputExecutionChainItem) 