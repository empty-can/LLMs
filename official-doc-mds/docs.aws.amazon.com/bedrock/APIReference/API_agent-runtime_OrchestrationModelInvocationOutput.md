

# OrchestrationModelInvocationOutput
<a name="API_agent-runtime_OrchestrationModelInvocationOutput"></a>

The foundation model output from the orchestration step.

## Contents
<a name="API_agent-runtime_OrchestrationModelInvocationOutput_Contents"></a>

 ** metadata **   <a name="bedrock-Type-agent-runtime_OrchestrationModelInvocationOutput-metadata"></a>
Contains information about the foundation model output from the orchestration step.  
Type: [Metadata](API_agent-runtime_Metadata.md) object  
Required: No

 ** rawResponse **   <a name="bedrock-Type-agent-runtime_OrchestrationModelInvocationOutput-rawResponse"></a>
Contains details of the raw response from the foundation model output.  
Type: [RawResponse](API_agent-runtime_RawResponse.md) object  
Required: No

 ** reasoningContent **   <a name="bedrock-Type-agent-runtime_OrchestrationModelInvocationOutput-reasoningContent"></a>
Contains content about the reasoning that the model made during the orchestration step.   
Type: [ReasoningContentBlock](API_agent-runtime_ReasoningContentBlock.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_OrchestrationModelInvocationOutput-traceId"></a>
The unique identifier of the trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

## See Also
<a name="API_agent-runtime_OrchestrationModelInvocationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/OrchestrationModelInvocationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/OrchestrationModelInvocationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/OrchestrationModelInvocationOutput) 