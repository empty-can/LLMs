

# FlowNodeConfiguration
<a name="API_agent_FlowNodeConfiguration"></a>

Contains configurations for a node in your flow. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_FlowNodeConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agent **   <a name="bedrock-Type-agent_FlowNodeConfiguration-agent"></a>
Contains configurations for an agent node in your flow. Invokes an alias of an agent and returns the response.  
Type: [AgentFlowNodeConfiguration](API_agent_AgentFlowNodeConfiguration.md) object  
Required: No

 ** collector **   <a name="bedrock-Type-agent_FlowNodeConfiguration-collector"></a>
Contains configurations for a collector node in your flow. Collects an iteration of inputs and consolidates them into an array of outputs.  
Type: [CollectorFlowNodeConfiguration](API_agent_CollectorFlowNodeConfiguration.md) object  
Required: No

 ** condition **   <a name="bedrock-Type-agent_FlowNodeConfiguration-condition"></a>
Contains configurations for a condition node in your flow. Defines conditions that lead to different branches of the flow.  
Type: [ConditionFlowNodeConfiguration](API_agent_ConditionFlowNodeConfiguration.md) object  
Required: No

 ** inlineCode **   <a name="bedrock-Type-agent_FlowNodeConfiguration-inlineCode"></a>
Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.  
Type: [InlineCodeFlowNodeConfiguration](API_agent_InlineCodeFlowNodeConfiguration.md) object  
Required: No

 ** input **   <a name="bedrock-Type-agent_FlowNodeConfiguration-input"></a>
Contains configurations for an input flow node in your flow. The first node in the flow. `inputs` can't be specified for this node.  
Type: [InputFlowNodeConfiguration](API_agent_InputFlowNodeConfiguration.md) object  
Required: No

 ** iterator **   <a name="bedrock-Type-agent_FlowNodeConfiguration-iterator"></a>
Contains configurations for an iterator node in your flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.  
The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.  
Type: [IteratorFlowNodeConfiguration](API_agent_IteratorFlowNodeConfiguration.md) object  
Required: No

 ** knowledgeBase **   <a name="bedrock-Type-agent_FlowNodeConfiguration-knowledgeBase"></a>
Contains configurations for a knowledge base node in your flow. Queries a knowledge base and returns the retrieved results or generated response.  
Type: [KnowledgeBaseFlowNodeConfiguration](API_agent_KnowledgeBaseFlowNodeConfiguration.md) object  
Required: No

 ** lambdaFunction **   <a name="bedrock-Type-agent_FlowNodeConfiguration-lambdaFunction"></a>
Contains configurations for a Lambda function node in your flow. Invokes an AWS Lambda function.  
Type: [LambdaFunctionFlowNodeConfiguration](API_agent_LambdaFunctionFlowNodeConfiguration.md) object  
Required: No

 ** lex **   <a name="bedrock-Type-agent_FlowNodeConfiguration-lex"></a>
Contains configurations for a Lex node in your flow. Invokes an Amazon Lex bot to identify the intent of the input and return the intent as the output.  
Type: [LexFlowNodeConfiguration](API_agent_LexFlowNodeConfiguration.md) object  
Required: No

 ** loop **   <a name="bedrock-Type-agent_FlowNodeConfiguration-loop"></a>
Contains configurations for a DoWhile loop in your flow.  
Type: [LoopFlowNodeConfiguration](API_agent_LoopFlowNodeConfiguration.md) object  
Required: No

 ** loopController **   <a name="bedrock-Type-agent_FlowNodeConfiguration-loopController"></a>
Contains controller node configurations for a DoWhile loop in your flow.  
Type: [LoopControllerFlowNodeConfiguration](API_agent_LoopControllerFlowNodeConfiguration.md) object  
Required: No

 ** loopInput **   <a name="bedrock-Type-agent_FlowNodeConfiguration-loopInput"></a>
Contains input node configurations for a DoWhile loop in your flow.  
Type: [LoopInputFlowNodeConfiguration](API_agent_LoopInputFlowNodeConfiguration.md) object  
Required: No

 ** output **   <a name="bedrock-Type-agent_FlowNodeConfiguration-output"></a>
Contains configurations for an output flow node in your flow. The last node in the flow. `outputs` can't be specified for this node.  
Type: [OutputFlowNodeConfiguration](API_agent_OutputFlowNodeConfiguration.md) object  
Required: No

 ** prompt **   <a name="bedrock-Type-agent_FlowNodeConfiguration-prompt"></a>
Contains configurations for a prompt node in your flow. Runs a prompt and generates the model response as the output. You can use a prompt from Prompt management or you can configure one in this node.  
Type: [PromptFlowNodeConfiguration](API_agent_PromptFlowNodeConfiguration.md) object  
Required: No

 ** retrieval **   <a name="bedrock-Type-agent_FlowNodeConfiguration-retrieval"></a>
Contains configurations for a retrieval node in your flow. Retrieves data from an Amazon S3 location and returns it as the output.  
Type: [RetrievalFlowNodeConfiguration](API_agent_RetrievalFlowNodeConfiguration.md) object  
Required: No

 ** storage **   <a name="bedrock-Type-agent_FlowNodeConfiguration-storage"></a>
Contains configurations for a storage node in your flow. Stores an input in an Amazon S3 location.  
Type: [StorageFlowNodeConfiguration](API_agent_StorageFlowNodeConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_FlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowNodeConfiguration) 