

# AgenticRetrieveTraceEventAttributes
<a name="API_agent-runtime_AgenticRetrieveTraceEventAttributes"></a>

Attributes describing the details of an agentic retrieval trace event.

## Contents
<a name="API_agent-runtime_AgenticRetrieveTraceEventAttributes_Contents"></a>

 ** message **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-message"></a>
A human-readable message describing the trace event.  
Type: String  
Required: Yes

 ** status **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-status"></a>
The status of the current step.  
Type: String  
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`   
Required: Yes

 ** step **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-step"></a>
The current step in the retrieval process.  
Type: String  
Valid Values: `Planning | Retrieval | SpeculativeRetrieval | FullDocumentExpansion`   
Required: Yes

 ** actions **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-actions"></a>
The list of actions taken during this step.  
Type: Array of [AgenticRetrieveAction](API_agent-runtime_AgenticRetrieveAction.md) objects  
Required: No

 ** failures **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-failures"></a>
Failures that occurred during this step.  
Type: Array of [AgenticRetrieveFailure](API_agent-runtime_AgenticRetrieveFailure.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** retrievalMetadata **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-retrievalMetadata"></a>
Metadata about the retrieval sources used.  
Type: Array of [AgenticRetrieveSourceMetadata](API_agent-runtime_AgenticRetrieveSourceMetadata.md) objects  
Required: No

 ** retrievalResponse **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-retrievalResponse"></a>
The retrieval results from this step.  
Type: Array of [AgenticRetrieveTraceResultItem](API_agent-runtime_AgenticRetrieveTraceResultItem.md) objects  
Required: No

 ** warnings **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceEventAttributes-warnings"></a>
Warnings generated during this step.  
Type: Array of [AgenticRetrieveWarning](API_agent-runtime_AgenticRetrieveWarning.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveTraceEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveTraceEventAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveTraceEventAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveTraceEventAttributes) 