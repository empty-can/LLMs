

# InvocationSummary
<a name="API_agent-runtime_InvocationSummary"></a>

Contains details about an invocation in a session. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Contents
<a name="API_agent-runtime_InvocationSummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent-runtime_InvocationSummary-createdAt"></a>
The timestamp for when the invocation was created.  
Type: Timestamp  
Required: Yes

 ** invocationId **   <a name="bedrock-Type-agent-runtime_InvocationSummary-invocationId"></a>
A unique identifier for the invocation in UUID format.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** sessionId **   <a name="bedrock-Type-agent-runtime_InvocationSummary-sessionId"></a>
The unique identifier for the session associated with the invocation.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## See Also
<a name="API_agent-runtime_InvocationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvocationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvocationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvocationSummary) 