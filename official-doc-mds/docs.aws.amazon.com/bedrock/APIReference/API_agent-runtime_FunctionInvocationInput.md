

# FunctionInvocationInput
<a name="API_agent-runtime_FunctionInvocationInput"></a>

Contains information about the function that the agent predicts should be called.

This data type is used in the following API operations:
+ In the `returnControl` field of the [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) 

## Contents
<a name="API_agent-runtime_FunctionInvocationInput_Contents"></a>

 ** actionGroup **   <a name="bedrock-Type-agent-runtime_FunctionInvocationInput-actionGroup"></a>
The action group that the function belongs to.  
Type: String  
Required: Yes

 ** actionInvocationType **   <a name="bedrock-Type-agent-runtime_FunctionInvocationInput-actionInvocationType"></a>
Contains information about the function to invoke,  
Type: String  
Valid Values: `RESULT | USER_CONFIRMATION | USER_CONFIRMATION_AND_RESULT`   
Required: No

 ** agentId **   <a name="bedrock-Type-agent-runtime_FunctionInvocationInput-agentId"></a>
The agent's ID.  
Type: String  
Required: No

 ** collaboratorName **   <a name="bedrock-Type-agent-runtime_FunctionInvocationInput-collaboratorName"></a>
The collaborator's name.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** function **   <a name="bedrock-Type-agent-runtime_FunctionInvocationInput-function"></a>
The name of the function.  
Type: String  
Required: No

 ** parameters **   <a name="bedrock-Type-agent-runtime_FunctionInvocationInput-parameters"></a>
A list of parameters of the function.  
Type: Array of [FunctionParameter](API_agent-runtime_FunctionParameter.md) objects  
Required: No

## See Also
<a name="API_agent-runtime_FunctionInvocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FunctionInvocationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FunctionInvocationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FunctionInvocationInput) 