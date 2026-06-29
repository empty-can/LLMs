

# KnowledgeBaseFlowNodeConfiguration
<a name="API_agent_KnowledgeBaseFlowNodeConfiguration"></a>

Contains configurations for a knowledge base node in a flow. This node takes a query as the input and returns, as the output, the retrieved responses directly (as an array) or a response generated based on the retrieved responses. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_KnowledgeBaseFlowNodeConfiguration_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-knowledgeBaseId"></a>
The unique identifier of the knowledge base to query.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `$|^[0-9a-zA-Z]+`   
Required: Yes

 ** guardrailConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-guardrailConfiguration"></a>
Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.  
Type: [GuardrailConfiguration](API_agent_GuardrailConfiguration.md) object  
Required: No

 ** inferenceConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-inferenceConfiguration"></a>
Contains inference configurations for the prompt.  
Type: [PromptInferenceConfiguration](API_agent_PromptInferenceConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** modelId **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-modelId"></a>
The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: No

 ** numberOfResults **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-numberOfResults"></a>
The number of results to retrieve from the knowledge base.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** orchestrationConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-orchestrationConfiguration"></a>
The configuration for orchestrating the retrieval and generation process in the knowledge base node.  
Type: [KnowledgeBaseOrchestrationConfiguration](API_agent_KnowledgeBaseOrchestrationConfiguration.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-promptTemplate"></a>
A custom prompt template to use with the knowledge base for generating responses.  
Type: [KnowledgeBasePromptTemplate](API_agent_KnowledgeBasePromptTemplate.md) object  
Required: No

 ** rerankingConfiguration **   <a name="bedrock-Type-agent_KnowledgeBaseFlowNodeConfiguration-rerankingConfiguration"></a>
The configuration for reranking the retrieved results from the knowledge base to improve relevance.  
Type: [VectorSearchRerankingConfiguration](API_agent_VectorSearchRerankingConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_KnowledgeBaseFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/KnowledgeBaseFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/KnowledgeBaseFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/KnowledgeBaseFlowNodeConfiguration) 