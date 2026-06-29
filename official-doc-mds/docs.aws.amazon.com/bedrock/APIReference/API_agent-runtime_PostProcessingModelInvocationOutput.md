

# PostProcessingModelInvocationOutput
<a name="API_agent-runtime_PostProcessingModelInvocationOutput"></a>

The foundation model output from the post-processing step.

## Contents
<a name="API_agent-runtime_PostProcessingModelInvocationOutput_Contents"></a>

 ** metadata **   <a name="bedrock-Type-agent-runtime_PostProcessingModelInvocationOutput-metadata"></a>
 Contains information about the foundation model output from the post-processing step.   
Type: [Metadata](API_agent-runtime_Metadata.md) object  
Required: No

 ** parsedResponse **   <a name="bedrock-Type-agent-runtime_PostProcessingModelInvocationOutput-parsedResponse"></a>
Details about the response from the Lambda parsing of the output of the post-processing step.  
Type: [PostProcessingParsedResponse](API_agent-runtime_PostProcessingParsedResponse.md) object  
Required: No

 ** rawResponse **   <a name="bedrock-Type-agent-runtime_PostProcessingModelInvocationOutput-rawResponse"></a>
 Details of the raw response from the foundation model output.   
Type: [RawResponse](API_agent-runtime_RawResponse.md) object  
Required: No

 ** reasoningContent **   <a name="bedrock-Type-agent-runtime_PostProcessingModelInvocationOutput-reasoningContent"></a>
Contains content about the reasoning that the model made during the post-processing step.  
Type: [ReasoningContentBlock](API_agent-runtime_ReasoningContentBlock.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_PostProcessingModelInvocationOutput-traceId"></a>
The unique identifier of the trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

## See Also
<a name="API_agent-runtime_PostProcessingModelInvocationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/PostProcessingModelInvocationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/PostProcessingModelInvocationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/PostProcessingModelInvocationOutput) 