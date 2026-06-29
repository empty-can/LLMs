

# Metadata
<a name="API_agent-runtime_Metadata"></a>

Provides information about the execution process for different types of invocations, such as model invocation, knowledge base invocation, agent collaborator invocation, guardrail invocation, and code interpreter Invocation.

## Contents
<a name="API_agent-runtime_Metadata_Contents"></a>

 ** clientRequestId **   <a name="bedrock-Type-agent-runtime_Metadata-clientRequestId"></a>
A unique identifier associated with the downstream invocation. This ID can be used for tracing, debugging, and identifying specific invocations in customer logs or systems.  
Type: String  
Required: No

 ** endTime **   <a name="bedrock-Type-agent-runtime_Metadata-endTime"></a>
In the final response, `endTime` is the end time of the agent invocation operation.  
Type: Timestamp  
Required: No

 ** operationTotalTimeMs **   <a name="bedrock-Type-agent-runtime_Metadata-operationTotalTimeMs"></a>
The total time it took for the agent to complete execution. This field is only set for the final response.  
Type: Long  
Required: No

 ** startTime **   <a name="bedrock-Type-agent-runtime_Metadata-startTime"></a>
In the final response, `startTime` is the start time of the agent invocation operation.  
Type: Timestamp  
Required: No

 ** totalTimeMs **   <a name="bedrock-Type-agent-runtime_Metadata-totalTimeMs"></a>
 The total execution time for the specific invocation being processed (model, knowledge base, guardrail, agent collaborator, or code interpreter). It represents how long the individual invocation took.  
Type: Long  
Required: No

 ** usage **   <a name="bedrock-Type-agent-runtime_Metadata-usage"></a>
Specific to model invocation and contains details about the usage of a foundation model.  
Type: [Usage](API_agent-runtime_Usage.md) object  
Required: No

## See Also
<a name="API_agent-runtime_Metadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Metadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Metadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Metadata) 