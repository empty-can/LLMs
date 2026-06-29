

# FlowFailureEvent
<a name="API_agent-runtime_FlowFailureEvent"></a>

Contains information about a failure that occurred at the flow level during a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowFailureEvent_Contents"></a>

 ** errorCode **   <a name="bedrock-Type-agent-runtime_FlowFailureEvent-errorCode"></a>
The error code that identifies the type of failure that occurred.  
Type: String  
Valid Values: `VALIDATION | INTERNAL_SERVER | NODE_EXECUTION_FAILED`   
Required: Yes

 ** errorMessage **   <a name="bedrock-Type-agent-runtime_FlowFailureEvent-errorMessage"></a>
A descriptive message that provides details about the failure.  
Type: String  
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_FlowFailureEvent-timestamp"></a>
The timestamp when the failure occurred.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_FlowFailureEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowFailureEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowFailureEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowFailureEvent) 