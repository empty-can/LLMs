

# KnowledgeBaseOrchestrationConfiguration
<a name="API_agent_KnowledgeBaseOrchestrationConfiguration"></a>

Configures how the knowledge base orchestrates the retrieval and generation process, allowing for customization of prompts, inference parameters, and performance settings.

## Contents
<a name="API_agent_KnowledgeBaseOrchestrationConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent_KnowledgeBaseOrchestrationConfiguration-additionalModelRequestFields"></a>
The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.  
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** inferenceConfig **   <a name="bedrock-Type-agent_KnowledgeBaseOrchestrationConfiguration-inferenceConfig"></a>
Contains inference configurations for the prompt.  
Type: [PromptInferenceConfiguration](API_agent_PromptInferenceConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** performanceConfig **   <a name="bedrock-Type-agent_KnowledgeBaseOrchestrationConfiguration-performanceConfig"></a>
The performance configuration options for the knowledge base retrieval and generation process.  
Type: [PerformanceConfiguration](API_agent_PerformanceConfiguration.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-agent_KnowledgeBaseOrchestrationConfiguration-promptTemplate"></a>
A custom prompt template for orchestrating the retrieval and generation process.  
Type: [KnowledgeBasePromptTemplate](API_agent_KnowledgeBasePromptTemplate.md) object  
Required: No

## See Also
<a name="API_agent_KnowledgeBaseOrchestrationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/KnowledgeBaseOrchestrationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/KnowledgeBaseOrchestrationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/KnowledgeBaseOrchestrationConfiguration) 