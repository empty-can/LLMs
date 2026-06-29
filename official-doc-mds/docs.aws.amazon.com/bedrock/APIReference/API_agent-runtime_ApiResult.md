

# ApiResult
<a name="API_agent-runtime_ApiResult"></a>

Contains information about the API operation that was called from the action group and the response body that was returned.

This data type is used in the following API operations:
+ In the `returnControlInvocationResults` of the [InvokeAgent request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_RequestSyntax) 

## Contents
<a name="API_agent-runtime_ApiResult_Contents"></a>

 ** actionGroup **   <a name="bedrock-Type-agent-runtime_ApiResult-actionGroup"></a>
The action group that the API operation belongs to.  
Type: String  
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent-runtime_ApiResult-agentId"></a>
The agent's ID.  
Type: String  
Required: No

 ** apiPath **   <a name="bedrock-Type-agent-runtime_ApiResult-apiPath"></a>
The path to the API operation.  
Type: String  
Required: No

 ** confirmationState **   <a name="bedrock-Type-agent-runtime_ApiResult-confirmationState"></a>
Controls the API operations or functions to invoke based on the user confirmation.  
Type: String  
Valid Values: `CONFIRM | DENY`   
Required: No

 ** httpMethod **   <a name="bedrock-Type-agent-runtime_ApiResult-httpMethod"></a>
The HTTP method for the API operation.  
Type: String  
Required: No

 ** httpStatusCode **   <a name="bedrock-Type-agent-runtime_ApiResult-httpStatusCode"></a>
http status code from API execution response (for example: 200, 400, 500).  
Type: Integer  
Required: No

 ** responseBody **   <a name="bedrock-Type-agent-runtime_ApiResult-responseBody"></a>
The response body from the API operation. The key of the object is the content type (currently, only `TEXT` is supported). The response may be returned directly or from the Lambda function.  
Type: String to [ContentBody](API_agent-runtime_ContentBody.md) object map  
Required: No

 ** responseState **   <a name="bedrock-Type-agent-runtime_ApiResult-responseState"></a>
Controls the final response state returned to end user when API/Function execution failed. When this state is FAILURE, the request would fail with dependency failure exception. When this state is REPROMPT, the API/function response will be sent to model for re-prompt  
Type: String  
Valid Values: `FAILURE | REPROMPT`   
Required: No

## See Also
<a name="API_agent-runtime_ApiResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ApiResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ApiResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ApiResult) 