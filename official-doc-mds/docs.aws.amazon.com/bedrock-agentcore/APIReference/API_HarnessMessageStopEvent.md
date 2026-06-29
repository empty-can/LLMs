

# HarnessMessageStopEvent
<a name="API_HarnessMessageStopEvent"></a>

Event indicating the end of a message.

## Contents
<a name="API_HarnessMessageStopEvent_Contents"></a>

 ** stopReason **   <a name="BedrockAgentCore-Type-HarnessMessageStopEvent-stopReason"></a>
The reason the agent stopped generating.  
Type: String  
Valid Values: `end_turn | tool_use | tool_result | max_tokens | stop_sequence | content_filtered | malformed_model_output | malformed_tool_use | interrupted | partial_turn | model_context_window_exceeded | max_iterations_exceeded | max_output_tokens_exceeded | timeout_exceeded`   
Required: Yes

## See Also
<a name="API_HarnessMessageStopEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessMessageStopEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessMessageStopEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessMessageStopEvent) 