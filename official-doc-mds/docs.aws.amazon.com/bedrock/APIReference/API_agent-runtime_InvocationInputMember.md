

# InvocationInputMember
<a name="API_agent-runtime_InvocationInputMember"></a>

Contains details about the API operation or function that the agent predicts should be called. 

This data type is used in the following API operations:
+ In the `returnControl` field of the [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) 

## Contents
<a name="API_agent-runtime_InvocationInputMember_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiInvocationInput **   <a name="bedrock-Type-agent-runtime_InvocationInputMember-apiInvocationInput"></a>
Contains information about the API operation that the agent predicts should be called.  
Type: [ApiInvocationInput](API_agent-runtime_ApiInvocationInput.md) object  
Required: No

 ** functionInvocationInput **   <a name="bedrock-Type-agent-runtime_InvocationInputMember-functionInvocationInput"></a>
Contains information about the function that the agent predicts should be called.  
Type: [FunctionInvocationInput](API_agent-runtime_FunctionInvocationInput.md) object  
Required: No

## See Also
<a name="API_agent-runtime_InvocationInputMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvocationInputMember) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvocationInputMember) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvocationInputMember) 