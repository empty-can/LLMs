

# OrchestrationTrace
<a name="API_agent-runtime_OrchestrationTrace"></a>

Details about the orchestration step, in which the agent determines the order in which actions are executed and which knowledge bases are retrieved.

## Contents
<a name="API_agent-runtime_OrchestrationTrace_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** invocationInput **   <a name="bedrock-Type-agent-runtime_OrchestrationTrace-invocationInput"></a>
Contains information pertaining to the action group or knowledge base that is being invoked.  
Type: [InvocationInput](API_agent-runtime_InvocationInput.md) object  
Required: No

 ** modelInvocationInput **   <a name="bedrock-Type-agent-runtime_OrchestrationTrace-modelInvocationInput"></a>
The input for the orchestration step.  
+ The `type` is `ORCHESTRATION`.
+ The `text` contains the prompt.
+ The `inferenceConfiguration`, `parserMode`, and `overrideLambda` values are set in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) object that was set when the agent was created or updated.
Type: [ModelInvocationInput](API_agent-runtime_ModelInvocationInput.md) object  
Required: No

 ** modelInvocationOutput **   <a name="bedrock-Type-agent-runtime_OrchestrationTrace-modelInvocationOutput"></a>
Contains information pertaining to the output from the foundation model that is being invoked.  
Type: [OrchestrationModelInvocationOutput](API_agent-runtime_OrchestrationModelInvocationOutput.md) object  
Required: No

 ** observation **   <a name="bedrock-Type-agent-runtime_OrchestrationTrace-observation"></a>
Details about the observation (the output of the action group Lambda or knowledge base) made by the agent.  
Type: [Observation](API_agent-runtime_Observation.md) object  
Required: No

 ** rationale **   <a name="bedrock-Type-agent-runtime_OrchestrationTrace-rationale"></a>
Details about the reasoning, based on the input, that the agent uses to justify carrying out an action group or getting information from a knowledge base.  
Type: [Rationale](API_agent-runtime_Rationale.md) object  
Required: No

## See Also
<a name="API_agent-runtime_OrchestrationTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/OrchestrationTrace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/OrchestrationTrace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/OrchestrationTrace) 