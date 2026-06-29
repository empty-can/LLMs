

# NodeOutputEvent
<a name="API_agent-runtime_NodeOutputEvent"></a>

Contains information about the outputs produced by a specific node during a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_NodeOutputEvent_Contents"></a>

 ** fields **   <a name="bedrock-Type-agent-runtime_NodeOutputEvent-fields"></a>
A list of output fields produced by the node.  
Type: Array of [NodeOutputField](API_agent-runtime_NodeOutputField.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_NodeOutputEvent-nodeName"></a>
The name of the node that produced the outputs.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_NodeOutputEvent-timestamp"></a>
The timestamp when the outputs were produced by the node.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_NodeOutputEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/NodeOutputEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/NodeOutputEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/NodeOutputEvent) 