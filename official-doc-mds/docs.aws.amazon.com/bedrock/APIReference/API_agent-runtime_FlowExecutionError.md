

# FlowExecutionError
<a name="API_agent-runtime_FlowExecutionError"></a>

Contains information about an error that occurred during an flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowExecutionError_Contents"></a>

 ** error **   <a name="bedrock-Type-agent-runtime_FlowExecutionError-error"></a>
The error code for the type of error that occurred.  
Type: String  
Valid Values: `ExecutionTimedOut`   
Required: No

 ** message **   <a name="bedrock-Type-agent-runtime_FlowExecutionError-message"></a>
A descriptive message that provides details about the error.  
Type: String  
Required: No

 ** nodeName **   <a name="bedrock-Type-agent-runtime_FlowExecutionError-nodeName"></a>
The name of the node in the flow where the error occurred (if applicable).  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: No

## See Also
<a name="API_agent-runtime_FlowExecutionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowExecutionError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowExecutionError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowExecutionError) 