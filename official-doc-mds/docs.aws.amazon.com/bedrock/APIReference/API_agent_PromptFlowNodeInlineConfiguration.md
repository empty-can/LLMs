

# PromptFlowNodeInlineConfiguration
<a name="API_agent_PromptFlowNodeInlineConfiguration"></a>

Contains configurations for a prompt defined inline in the node.

## Contents
<a name="API_agent_PromptFlowNodeInlineConfiguration_Contents"></a>

 ** modelId **   <a name="bedrock-Type-agent_PromptFlowNodeInlineConfiguration-modelId"></a>
The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to run inference with.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `$|^(arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** templateConfiguration **   <a name="bedrock-Type-agent_PromptFlowNodeInlineConfiguration-templateConfiguration"></a>
Contains a prompt and variables in the prompt that can be replaced with values at runtime.  
Type: [PromptTemplateConfiguration](API_agent_PromptTemplateConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** templateType **   <a name="bedrock-Type-agent_PromptFlowNodeInlineConfiguration-templateType"></a>
The type of prompt template.  
Type: String  
Valid Values: `TEXT | CHAT`   
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent_PromptFlowNodeInlineConfiguration-additionalModelRequestFields"></a>
Additional fields to be included in the model request for the Prompt node.  
Type: JSON value  
Required: No

 ** inferenceConfiguration **   <a name="bedrock-Type-agent_PromptFlowNodeInlineConfiguration-inferenceConfiguration"></a>
Contains inference configurations for the prompt.  
Type: [PromptInferenceConfiguration](API_agent_PromptInferenceConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_agent_PromptFlowNodeInlineConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptFlowNodeInlineConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptFlowNodeInlineConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptFlowNodeInlineConfiguration) 