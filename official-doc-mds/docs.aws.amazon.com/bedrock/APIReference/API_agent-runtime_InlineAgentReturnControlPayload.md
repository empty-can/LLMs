

# InlineAgentReturnControlPayload
<a name="API_agent-runtime_InlineAgentReturnControlPayload"></a>

Contains information to return from the action group that the agent has predicted to invoke.

This data type is used in the [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) API operation.

## Contents
<a name="API_agent-runtime_InlineAgentReturnControlPayload_Contents"></a>

 ** invocationId **   <a name="bedrock-Type-agent-runtime_InlineAgentReturnControlPayload-invocationId"></a>
The identifier of the action group invocation.   
Type: String  
Required: No

 ** invocationInputs **   <a name="bedrock-Type-agent-runtime_InlineAgentReturnControlPayload-invocationInputs"></a>
A list of objects that contain information about the parameters and inputs that need to be sent into the API operation or function, based on what the agent determines from its session with the user.  
Type: Array of [InvocationInputMember](API_agent-runtime_InvocationInputMember.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_agent-runtime_InlineAgentReturnControlPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InlineAgentReturnControlPayload) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InlineAgentReturnControlPayload) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InlineAgentReturnControlPayload) 