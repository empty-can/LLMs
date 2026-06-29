

# FunctionResult
<a name="API_agent-runtime_FunctionResult"></a>

Contains information about the function that was called from the action group and the response that was returned.

This data type is used in the following API operations:
+ In the `returnControlInvocationResults` of the [InvokeAgent request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_RequestSyntax) 

## Contents
<a name="API_agent-runtime_FunctionResult_Contents"></a>

 ** actionGroup **   <a name="bedrock-Type-agent-runtime_FunctionResult-actionGroup"></a>
The action group that the function belongs to.  
Type: String  
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent-runtime_FunctionResult-agentId"></a>
The agent's ID.  
Type: String  
Required: No

 ** confirmationState **   <a name="bedrock-Type-agent-runtime_FunctionResult-confirmationState"></a>
Contains the user confirmation information about the function that was called.  
Type: String  
Valid Values: `CONFIRM | DENY`   
Required: No

 ** function **   <a name="bedrock-Type-agent-runtime_FunctionResult-function"></a>
The name of the function that was called.  
Type: String  
Required: No

 ** responseBody **   <a name="bedrock-Type-agent-runtime_FunctionResult-responseBody"></a>
The response from the function call using the parameters. The response might be returned directly or from the Lambda function. Specify `TEXT` or `IMAGES`. The key of the object is the content type. You can only specify one type. If you specify `IMAGES`, you can specify only one image. You can specify images only when the function in the `returnControlInvocationResults` is a computer use action. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html).  
Type: String to [ContentBody](API_agent-runtime_ContentBody.md) object map  
Required: No

 ** responseState **   <a name="bedrock-Type-agent-runtime_FunctionResult-responseState"></a>
Controls the final response state returned to end user when API/Function execution failed. When this state is FAILURE, the request would fail with dependency failure exception. When this state is REPROMPT, the API/function response will be sent to model for re-prompt  
Type: String  
Valid Values: `FAILURE | REPROMPT`   
Required: No

## See Also
<a name="API_agent-runtime_FunctionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FunctionResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FunctionResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FunctionResult) 