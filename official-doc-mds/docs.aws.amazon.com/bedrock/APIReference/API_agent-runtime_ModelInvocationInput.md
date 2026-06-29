

# ModelInvocationInput
<a name="API_agent-runtime_ModelInvocationInput"></a>

The input for the pre-processing step.
+ The `type` matches the agent step.
+ The `text` contains the prompt.
+ The `inferenceConfiguration`, `parserMode`, and `overrideLambda` values are set in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) object that was set when the agent was created or updated.

## Contents
<a name="API_agent-runtime_ModelInvocationInput_Contents"></a>

 ** foundationModel **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-foundationModel"></a>
The identifier of a foundation model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+))$|(^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{1,20}):(|[0-9]{12}):inference-profile/[a-zA-Z0-9-:.]+)`   
Required: No

 ** inferenceConfiguration **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-inferenceConfiguration"></a>
Specifications about the inference parameters that were provided alongside the prompt. These are specified in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) object that was set when the agent was created or updated. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).  
Type: [InferenceConfiguration](API_agent-runtime_InferenceConfiguration.md) object  
Required: No

 ** overrideLambda **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-overrideLambda"></a>
The ARN of the Lambda function to use when parsing the raw foundation model output in parts of the agent sequence.  
Type: String  
Required: No

 ** parserMode **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-parserMode"></a>
Specifies whether to override the default parser Lambda function when parsing the raw foundation model output in the part of the agent sequence defined by the `promptType`.  
Type: String  
Valid Values: `DEFAULT | OVERRIDDEN`   
Required: No

 ** promptCreationMode **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-promptCreationMode"></a>
Specifies whether the default prompt template was `OVERRIDDEN`. If it was, the `basePromptTemplate` that was set in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) object when the agent was created or updated is used instead.  
Type: String  
Valid Values: `DEFAULT | OVERRIDDEN`   
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-text"></a>
The text that prompted the agent at this step.  
Type: String  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-traceId"></a>
The unique identifier of the trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_ModelInvocationInput-type"></a>
The step in the agent sequence.  
Type: String  
Valid Values: `PRE_PROCESSING | ORCHESTRATION | KNOWLEDGE_BASE_RESPONSE_GENERATION | POST_PROCESSING | ROUTING_CLASSIFIER`   
Required: No

## See Also
<a name="API_agent-runtime_ModelInvocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ModelInvocationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ModelInvocationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ModelInvocationInput) 