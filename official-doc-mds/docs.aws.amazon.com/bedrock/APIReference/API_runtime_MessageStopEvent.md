

# MessageStopEvent
<a name="API_runtime_MessageStopEvent"></a>

The stop event for a message.

## Contents
<a name="API_runtime_MessageStopEvent_Contents"></a>

 ** stopReason **   <a name="bedrock-Type-runtime_MessageStopEvent-stopReason"></a>
The reason why the model stopped generating output.  
Type: String  
Valid Values: `end_turn | tool_use | max_tokens | stop_sequence | guardrail_intervened | content_filtered | malformed_model_output | malformed_tool_use | model_context_window_exceeded`   
Required: Yes

 ** additionalModelResponseFields **   <a name="bedrock-Type-runtime_MessageStopEvent-additionalModelResponseFields"></a>
The additional model response fields.  
Type: JSON value  
Required: No

## See Also
<a name="API_runtime_MessageStopEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/MessageStopEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/MessageStopEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/MessageStopEvent) 