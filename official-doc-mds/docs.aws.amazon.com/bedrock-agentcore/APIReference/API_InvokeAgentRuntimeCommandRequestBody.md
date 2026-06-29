

# InvokeAgentRuntimeCommandRequestBody
<a name="API_InvokeAgentRuntimeCommandRequestBody"></a>

The request body structure for the `InvokeAgentRuntimeCommand` operation, containing the command to execute and optional configuration parameters.

## Contents
<a name="API_InvokeAgentRuntimeCommandRequestBody_Contents"></a>

 ** command **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandRequestBody-command"></a>
The shell command to execute on the agent runtime. This command is executed in the runtime environment and its output is streamed back to the caller.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Required: Yes

 ** timeout **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandRequestBody-timeout"></a>
The maximum duration in seconds to wait for the command to complete. If the command execution exceeds this timeout, it will be terminated. Default is 300 seconds. Minimum is 1 second. Maximum is 3600 seconds.  
Type: Integer  
Required: No

## See Also
<a name="API_InvokeAgentRuntimeCommandRequestBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandRequestBody) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandRequestBody) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandRequestBody) 