

# NodeInputField
<a name="API_agent-runtime_NodeInputField"></a>

Represents an input field provided to a node during a flow execution.

## Contents
<a name="API_agent-runtime_NodeInputField_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_NodeInputField-content"></a>
The content of the input field, which can contain text or structured data.  
Type: [NodeExecutionContent](API_agent-runtime_NodeExecutionContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrock-Type-agent-runtime_NodeInputField-name"></a>
The name of the input field as defined in the node's input schema.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** category **   <a name="bedrock-Type-agent-runtime_NodeInputField-category"></a>
The category of the input field.  
Type: String  
Valid Values: `LoopCondition | ReturnValueToLoopStart | ExitLoop`   
Required: No

 ** executionChain **   <a name="bedrock-Type-agent-runtime_NodeInputField-executionChain"></a>
The execution path through nested nodes like iterators and loops.  
Type: Array of [NodeInputExecutionChainItem](API_agent-runtime_NodeInputExecutionChainItem.md) objects  
Required: No

 ** source **   <a name="bedrock-Type-agent-runtime_NodeInputField-source"></a>
The source node that provides input data to this field.  
Type: [NodeInputSource](API_agent-runtime_NodeInputSource.md) object  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_NodeInputField-type"></a>
The data type of the input field for compatibility validation.  
Type: String  
Valid Values: `String | Number | Boolean | Object | Array`   
Required: No

## See Also
<a name="API_agent-runtime_NodeInputField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/NodeInputField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/NodeInputField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/NodeInputField) 