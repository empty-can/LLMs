

# FlowOutputEvent
<a name="API_agent-runtime_FlowOutputEvent"></a>

Contains information about an output from prompt flow invoction.

## Contents
<a name="API_agent-runtime_FlowOutputEvent_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowOutputEvent-content"></a>
The content in the output.  
Type: [FlowOutputContent](API_agent-runtime_FlowOutputContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowOutputEvent-nodeName"></a>
The name of the flow output node that the output is from.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** nodeType **   <a name="bedrock-Type-agent-runtime_FlowOutputEvent-nodeType"></a>
The type of the node that the output is from.  
Type: String  
Valid Values: `FlowInputNode | FlowOutputNode | LambdaFunctionNode | KnowledgeBaseNode | PromptNode | ConditionNode | LexNode`   
Required: Yes

## See Also
<a name="API_agent-runtime_FlowOutputEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowOutputEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowOutputEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowOutputEvent) 