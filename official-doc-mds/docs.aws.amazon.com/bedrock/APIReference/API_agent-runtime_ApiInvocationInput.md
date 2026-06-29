

# ApiInvocationInput
<a name="API_agent-runtime_ApiInvocationInput"></a>

Contains information about the API operation that the agent predicts should be called.

This data type is used in the following API operations:
+ In the `returnControl` field of the [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) 

## Contents
<a name="API_agent-runtime_ApiInvocationInput_Contents"></a>

 ** actionGroup **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-actionGroup"></a>
The action group that the API operation belongs to.  
Type: String  
Required: Yes

 ** actionInvocationType **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-actionInvocationType"></a>
Contains information about the API operation to invoke.  
Type: String  
Valid Values: `RESULT | USER_CONFIRMATION | USER_CONFIRMATION_AND_RESULT`   
Required: No

 ** agentId **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-agentId"></a>
The agent's ID.  
Type: String  
Required: No

 ** apiPath **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-apiPath"></a>
The path to the API operation.  
Type: String  
Required: No

 ** collaboratorName **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-collaboratorName"></a>
The agent collaborator's name.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** httpMethod **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-httpMethod"></a>
The HTTP method of the API operation.  
Type: String  
Required: No

 ** parameters **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-parameters"></a>
The parameters to provide for the API request, as the agent elicited from the user.  
Type: Array of [ApiParameter](API_agent-runtime_ApiParameter.md) objects  
Required: No

 ** requestBody **   <a name="bedrock-Type-agent-runtime_ApiInvocationInput-requestBody"></a>
The request body to provide for the API request, as the agent elicited from the user.  
Type: [ApiRequestBody](API_agent-runtime_ApiRequestBody.md) object  
Required: No

## See Also
<a name="API_agent-runtime_ApiInvocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ApiInvocationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ApiInvocationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ApiInvocationInput) 