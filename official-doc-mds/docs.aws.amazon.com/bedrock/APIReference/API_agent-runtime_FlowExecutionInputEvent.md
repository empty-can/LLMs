

# FlowExecutionInputEvent
<a name="API_agent-runtime_FlowExecutionInputEvent"></a>

Contains information about the inputs provided to the flow at the start of a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowExecutionInputEvent_Contents"></a>

 ** fields **   <a name="bedrock-Type-agent-runtime_FlowExecutionInputEvent-fields"></a>
A list of input fields provided to the flow.  
Type: Array of [FlowInputField](API_agent-runtime_FlowInputField.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowExecutionInputEvent-nodeName"></a>
The name of the node that receives the inputs.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_FlowExecutionInputEvent-timestamp"></a>
The timestamp when the inputs are provided.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_FlowExecutionInputEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowExecutionInputEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowExecutionInputEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowExecutionInputEvent) 