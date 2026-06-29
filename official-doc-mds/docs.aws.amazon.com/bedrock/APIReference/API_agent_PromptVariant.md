

# PromptVariant
<a name="API_agent_PromptVariant"></a>

Contains details about a variant of the prompt.

## Contents
<a name="API_agent_PromptVariant_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_PromptVariant-name"></a>
The name of the prompt variant.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** templateConfiguration **   <a name="bedrock-Type-agent_PromptVariant-templateConfiguration"></a>
Contains configurations for the prompt template.  
Type: [PromptTemplateConfiguration](API_agent_PromptTemplateConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** templateType **   <a name="bedrock-Type-agent_PromptVariant-templateType"></a>
The type of prompt template to use.  
Type: String  
Valid Values: `TEXT | CHAT`   
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent_PromptVariant-additionalModelRequestFields"></a>
Contains model-specific inference configurations that aren't in the `inferenceConfiguration` field. To see model-specific inference parameters, see [Inference request parameters and response fields for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).  
Type: JSON value  
Required: No

 ** genAiResource **   <a name="bedrock-Type-agent_PromptVariant-genAiResource"></a>
Specifies a generative AI resource with which to use the prompt.  
Type: [PromptGenAiResource](API_agent_PromptGenAiResource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** inferenceConfiguration **   <a name="bedrock-Type-agent_PromptVariant-inferenceConfiguration"></a>
Contains inference configurations for the prompt variant.  
Type: [PromptInferenceConfiguration](API_agent_PromptInferenceConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** metadata **   <a name="bedrock-Type-agent_PromptVariant-metadata"></a>
An array of objects, each containing a key-value pair that defines a metadata tag and value to attach to a prompt variant.  
Type: Array of [PromptMetadataEntry](API_agent_PromptMetadataEntry.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** modelId **   <a name="bedrock-Type-agent_PromptVariant-modelId"></a>
The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) with which to run inference on the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: No

## See Also
<a name="API_agent_PromptVariant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptVariant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptVariant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptVariant) 