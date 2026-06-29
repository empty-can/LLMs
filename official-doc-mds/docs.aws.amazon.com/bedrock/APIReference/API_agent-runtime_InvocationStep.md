

# InvocationStep
<a name="API_agent-runtime_InvocationStep"></a>

Stores fine-grained state checkpoints, including text and images, for each interaction in an invocation in a session. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html). 

## Contents
<a name="API_agent-runtime_InvocationStep_Contents"></a>

 ** invocationId **   <a name="bedrock-Type-agent-runtime_InvocationStep-invocationId"></a>
The unique identifier (in UUID format) for the invocation that includes the invocation step.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** invocationStepId **   <a name="bedrock-Type-agent-runtime_InvocationStep-invocationStepId"></a>
The unique identifier (in UUID format) for the invocation step.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** invocationStepTime **   <a name="bedrock-Type-agent-runtime_InvocationStep-invocationStepTime"></a>
The timestamp for when the invocation step was created.  
Type: Timestamp  
Required: Yes

 ** payload **   <a name="bedrock-Type-agent-runtime_InvocationStep-payload"></a>
Payload content, such as text and images, for the invocation step.  
Type: [InvocationStepPayload](API_agent-runtime_InvocationStepPayload.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** sessionId **   <a name="bedrock-Type-agent-runtime_InvocationStep-sessionId"></a>
The unique identifier of the session containing the invocation step.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## See Also
<a name="API_agent-runtime_InvocationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvocationStep) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvocationStep) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvocationStep) 