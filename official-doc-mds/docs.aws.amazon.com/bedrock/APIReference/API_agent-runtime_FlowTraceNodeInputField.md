

# FlowTraceNodeInputField
<a name="API_agent-runtime_FlowTraceNodeInputField"></a>

Contains information about a field in the input into a node. For more information, see [Track each step in your prompt flow by viewing its trace in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html).

## Contents
<a name="API_agent-runtime_FlowTraceNodeInputField_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputField-content"></a>
The content of the node input.  
Type: [FlowTraceNodeInputContent](API_agent-runtime_FlowTraceNodeInputContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** nodeInputName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputField-nodeInputName"></a>
The name of the node input.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** category **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputField-category"></a>
The category of the input field.  
Type: String  
Valid Values: `LoopCondition | ReturnValueToLoopStart | ExitLoop`   
Required: No

 ** executionChain **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputField-executionChain"></a>
The execution path through nested nodes like iterators and loops.  
Type: Array of [FlowTraceNodeInputExecutionChainItem](API_agent-runtime_FlowTraceNodeInputExecutionChainItem.md) objects  
Required: No

 ** source **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputField-source"></a>
The source node that provides input data to this field.  
Type: [FlowTraceNodeInputSource](API_agent-runtime_FlowTraceNodeInputSource.md) object  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeInputField-type"></a>
The data type of the input field for compatibility validation.  
Type: String  
Valid Values: `String | Number | Boolean | Object | Array`   
Required: No

## See Also
<a name="API_agent-runtime_FlowTraceNodeInputField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceNodeInputField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceNodeInputField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceNodeInputField) 