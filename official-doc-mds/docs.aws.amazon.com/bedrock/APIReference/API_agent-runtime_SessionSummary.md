

# SessionSummary
<a name="API_agent-runtime_SessionSummary"></a>

Contains details about a session. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Contents
<a name="API_agent-runtime_SessionSummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent-runtime_SessionSummary-createdAt"></a>
The timestamp for when the session was created.  
Type: Timestamp  
Required: Yes

 ** lastUpdatedAt **   <a name="bedrock-Type-agent-runtime_SessionSummary-lastUpdatedAt"></a>
The timestamp for when the session was last modified.  
Type: Timestamp  
Required: Yes

 ** sessionArn **   <a name="bedrock-Type-agent-runtime_SessionSummary-sessionArn"></a>
The Amazon Resource Name (ARN) of the session.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** sessionId **   <a name="bedrock-Type-agent-runtime_SessionSummary-sessionId"></a>
The unique identifier for the session.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** sessionStatus **   <a name="bedrock-Type-agent-runtime_SessionSummary-sessionStatus"></a>
The current status of the session.  
Type: String  
Valid Values: `ACTIVE | EXPIRED | ENDED`   
Required: Yes

## See Also
<a name="API_agent-runtime_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/SessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/SessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/SessionSummary) 