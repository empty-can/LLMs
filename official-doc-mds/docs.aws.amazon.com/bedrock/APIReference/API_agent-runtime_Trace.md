

# Trace
<a name="API_agent-runtime_Trace"></a>

Contains one part of the agent's reasoning process and results from calling API actions and querying knowledge bases. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see [Trace enablement](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement).

## Contents
<a name="API_agent-runtime_Trace_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customOrchestrationTrace **   <a name="bedrock-Type-agent-runtime_Trace-customOrchestrationTrace"></a>
 Details about the custom orchestration step in which the agent determines the order in which actions are executed.   
Type: [CustomOrchestrationTrace](API_agent-runtime_CustomOrchestrationTrace.md) object  
Required: No

 ** failureTrace **   <a name="bedrock-Type-agent-runtime_Trace-failureTrace"></a>
Contains information about the failure of the interaction.  
Type: [FailureTrace](API_agent-runtime_FailureTrace.md) object  
Required: No

 ** guardrailTrace **   <a name="bedrock-Type-agent-runtime_Trace-guardrailTrace"></a>
The trace details for a trace defined in the Guardrail filter.  
Type: [GuardrailTrace](API_agent-runtime_GuardrailTrace.md) object  
Required: No

 ** orchestrationTrace **   <a name="bedrock-Type-agent-runtime_Trace-orchestrationTrace"></a>
Details about the orchestration step, in which the agent determines the order in which actions are executed and which knowledge bases are retrieved.  
Type: [OrchestrationTrace](API_agent-runtime_OrchestrationTrace.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** postProcessingTrace **   <a name="bedrock-Type-agent-runtime_Trace-postProcessingTrace"></a>
Details about the post-processing step, in which the agent shapes the response..  
Type: [PostProcessingTrace](API_agent-runtime_PostProcessingTrace.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** preProcessingTrace **   <a name="bedrock-Type-agent-runtime_Trace-preProcessingTrace"></a>
Details about the pre-processing step, in which the agent contextualizes and categorizes user inputs.  
Type: [PreProcessingTrace](API_agent-runtime_PreProcessingTrace.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** routingClassifierTrace **   <a name="bedrock-Type-agent-runtime_Trace-routingClassifierTrace"></a>
A routing classifier's trace.  
Type: [RoutingClassifierTrace](API_agent-runtime_RoutingClassifierTrace.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_agent-runtime_Trace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Trace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Trace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Trace) 