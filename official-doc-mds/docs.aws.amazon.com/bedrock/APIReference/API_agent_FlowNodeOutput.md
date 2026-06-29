

# FlowNodeOutput
<a name="API_agent_FlowNodeOutput"></a>

Contains configurations for an output from a node.

## Contents
<a name="API_agent_FlowNodeOutput_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_FlowNodeOutput-name"></a>
A name for the output that you can reference.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent_FlowNodeOutput-type"></a>
The data type of the output. If the output doesn't match this type at runtime, a validation error will be thrown.  
Type: String  
Valid Values: `String | Number | Boolean | Object | Array`   
Required: Yes

## See Also
<a name="API_agent_FlowNodeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowNodeOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowNodeOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowNodeOutput) 