

# ActionGroupInvocationInput
<a name="API_agent-runtime_ActionGroupInvocationInput"></a>

Contains information about the action group being invoked. For more information about the possible structures, see the InvocationInput tab in [OrchestrationTrace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-orchestration.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Contents
<a name="API_agent-runtime_ActionGroupInvocationInput_Contents"></a>

 ** actionGroupName **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-actionGroupName"></a>
The name of the action group.  
Type: String  
Required: No

 ** apiPath **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-apiPath"></a>
The path to the API to call, based off the action group.  
Type: String  
Required: No

 ** executionType **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-executionType"></a>
How fulfillment of the action is handled. For more information, see [Handling fulfillment of the action](https://docs.aws.amazon.com/bedrock/latest/userguide/action-handle.html).  
Type: String  
Valid Values: `LAMBDA | RETURN_CONTROL`   
Required: No

 ** function **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-function"></a>
The function in the action group to call.  
Type: String  
Required: No

 ** invocationId **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-invocationId"></a>
The unique identifier of the invocation. Only returned if the `executionType` is `RETURN_CONTROL`.  
Type: String  
Required: No

 ** parameters **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-parameters"></a>
The parameters in the Lambda input event.  
Type: Array of [Parameter](API_agent-runtime_Parameter.md) objects  
Required: No

 ** requestBody **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-requestBody"></a>
The parameters in the request body for the Lambda input event.  
Type: [RequestBody](API_agent-runtime_RequestBody.md) object  
Required: No

 ** verb **   <a name="bedrock-Type-agent-runtime_ActionGroupInvocationInput-verb"></a>
The API method being used, based off the action group.  
Type: String  
Required: No

## See Also
<a name="API_agent-runtime_ActionGroupInvocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ActionGroupInvocationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ActionGroupInvocationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ActionGroupInvocationInput) 