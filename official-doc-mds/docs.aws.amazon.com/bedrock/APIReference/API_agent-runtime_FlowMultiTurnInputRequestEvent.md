

# FlowMultiTurnInputRequestEvent
<a name="API_agent-runtime_FlowMultiTurnInputRequestEvent"></a>

Response object from the flow multi-turn node requesting additional information.

## Contents
<a name="API_agent-runtime_FlowMultiTurnInputRequestEvent_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowMultiTurnInputRequestEvent-content"></a>
The content payload containing the input request details for the multi-turn interaction.  
Type: [FlowMultiTurnInputContent](API_agent-runtime_FlowMultiTurnInputContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowMultiTurnInputRequestEvent-nodeName"></a>
The name of the node in the flow that is requesting the input.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** nodeType **   <a name="bedrock-Type-agent-runtime_FlowMultiTurnInputRequestEvent-nodeType"></a>
The type of the node in the flow that is requesting the input.  
Type: String  
Valid Values: `FlowInputNode | FlowOutputNode | LambdaFunctionNode | KnowledgeBaseNode | PromptNode | ConditionNode | LexNode`   
Required: Yes

## See Also
<a name="API_agent-runtime_FlowMultiTurnInputRequestEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowMultiTurnInputRequestEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowMultiTurnInputRequestEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowMultiTurnInputRequestEvent) 