

# FlowInput
<a name="API_agent-runtime_FlowInput"></a>

Contains information about an input into the prompt flow and where to send it.

## Contents
<a name="API_agent-runtime_FlowInput_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowInput-content"></a>
Contains information about an input into the prompt flow.  
Type: [FlowInputContent](API_agent-runtime_FlowInputContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowInput-nodeName"></a>
The name of the flow input node that begins the prompt flow.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** nodeInputName **   <a name="bedrock-Type-agent-runtime_FlowInput-nodeInputName"></a>
The name of the input from the flow input node.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: No

 ** nodeOutputName **   <a name="bedrock-Type-agent-runtime_FlowInput-nodeOutputName"></a>
The name of the output from the flow input node that begins the prompt flow.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: No

## See Also
<a name="API_agent-runtime_FlowInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowInput) 