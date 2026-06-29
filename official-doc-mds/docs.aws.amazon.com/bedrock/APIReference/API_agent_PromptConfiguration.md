

# PromptConfiguration
<a name="API_agent_PromptConfiguration"></a>

Contains configurations to override a prompt template in one part of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).

## Contents
<a name="API_agent_PromptConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent_PromptConfiguration-additionalModelRequestFields"></a>
If the Converse or ConverseStream operations support the model, `additionalModelRequestFields` contains additional inference parameters, beyond the base set of inference parameters in the `inferenceConfiguration` field.   
For more information, see [Inference request parameters and response fields for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).  
Type: JSON value  
Required: No

 ** basePromptTemplate **   <a name="bedrock-Type-agent_PromptConfiguration-basePromptTemplate"></a>
Defines the prompt template with which to replace the default prompt template. You can use placeholder variables in the base prompt template to customize the prompt. For more information, see [Prompt template placeholder variables](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html). For more information, see [Configure the prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-configure.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: No

 ** foundationModel **   <a name="bedrock-Type-agent_PromptConfiguration-foundationModel"></a>
The agent's foundation model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: No

 ** inferenceConfiguration **   <a name="bedrock-Type-agent_PromptConfiguration-inferenceConfiguration"></a>
Contains inference parameters to use when the agent invokes a foundation model in the part of the agent sequence defined by the `promptType`. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).  
Type: [InferenceConfiguration](API_agent_InferenceConfiguration.md) object  
Required: No

 ** parserMode **   <a name="bedrock-Type-agent_PromptConfiguration-parserMode"></a>
Specifies whether to override the default parser Lambda function when parsing the raw foundation model output in the part of the agent sequence defined by the `promptType`. If you set the field as `OVERRIDDEN`, the `overrideLambda` field in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) must be specified with the ARN of a Lambda function.  
Type: String  
Valid Values: `DEFAULT | OVERRIDDEN`   
Required: No

 ** promptCreationMode **   <a name="bedrock-Type-agent_PromptConfiguration-promptCreationMode"></a>
Specifies whether to override the default prompt template for this `promptType`. Set this value to `OVERRIDDEN` to use the prompt that you provide in the `basePromptTemplate`. If you leave it as `DEFAULT`, the agent uses a default prompt template.  
Type: String  
Valid Values: `DEFAULT | OVERRIDDEN`   
Required: No

 ** promptState **   <a name="bedrock-Type-agent_PromptConfiguration-promptState"></a>
Specifies whether to allow the agent to carry out the step specified in the `promptType`. If you set this value to `DISABLED`, the agent skips that step. The default state for each `promptType` is as follows.  
+  `PRE_PROCESSING` – `DISABLED` 
+  `ORCHESTRATION` – `ENABLED` 
+  `KNOWLEDGE_BASE_RESPONSE_GENERATION` – `ENABLED` 
+  `POST_PROCESSING` – `DISABLED` 
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** promptType **   <a name="bedrock-Type-agent_PromptConfiguration-promptType"></a>
The step in the agent sequence that this prompt configuration applies to.  
Type: String  
Valid Values: `PRE_PROCESSING | ORCHESTRATION | POST_PROCESSING | KNOWLEDGE_BASE_RESPONSE_GENERATION | MEMORY_SUMMARIZATION`   
Required: No

## See Also
<a name="API_agent_PromptConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptConfiguration) 