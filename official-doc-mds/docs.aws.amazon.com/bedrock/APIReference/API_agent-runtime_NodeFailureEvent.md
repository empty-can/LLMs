

# NodeFailureEvent
<a name="API_agent-runtime_NodeFailureEvent"></a>

Contains information about a failure that occurred at a specific node during a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_NodeFailureEvent_Contents"></a>

 ** errorCode **   <a name="bedrock-Type-agent-runtime_NodeFailureEvent-errorCode"></a>
The error code that identifies the type of failure that occurred at the node.  
Type: String  
Valid Values: `VALIDATION | DEPENDENCY_FAILED | BAD_GATEWAY | INTERNAL_SERVER`   
Required: Yes

 ** errorMessage **   <a name="bedrock-Type-agent-runtime_NodeFailureEvent-errorMessage"></a>
A descriptive message that provides details about the node failure.  
Type: String  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_NodeFailureEvent-nodeName"></a>
The name of the node where the failure occurred.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_NodeFailureEvent-timestamp"></a>
The timestamp when the node failure occurred.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_NodeFailureEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/NodeFailureEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/NodeFailureEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/NodeFailureEvent) 