

# InvocationResultMember
<a name="API_agent-runtime_InvocationResultMember"></a>

A result from the invocation of an action. For more information, see [Return control to the agent developer](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html) and [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html).

This data type is used in the following API operations:
+  [InvokeAgent request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_RequestSyntax) 

## Contents
<a name="API_agent-runtime_InvocationResultMember_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiResult **   <a name="bedrock-Type-agent-runtime_InvocationResultMember-apiResult"></a>
The result from the API response from the action group invocation.  
Type: [ApiResult](API_agent-runtime_ApiResult.md) object  
Required: No

 ** functionResult **   <a name="bedrock-Type-agent-runtime_InvocationResultMember-functionResult"></a>
The result from the function from the action group invocation.  
Type: [FunctionResult](API_agent-runtime_FunctionResult.md) object  
Required: No

## See Also
<a name="API_agent-runtime_InvocationResultMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvocationResultMember) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvocationResultMember) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvocationResultMember) 