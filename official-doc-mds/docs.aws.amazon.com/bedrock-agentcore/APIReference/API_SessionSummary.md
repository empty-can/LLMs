

# SessionSummary
<a name="API_SessionSummary"></a>

Contains summary information about a session in an AgentCore Memory resource.

## Contents
<a name="API_SessionSummary_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-SessionSummary-actorId"></a>
The identifier of the actor associated with the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-SessionSummary-createdAt"></a>
The timestamp when the session was created.  
Type: Timestamp  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-SessionSummary-sessionId"></a>
The unique identifier of the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

## See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionSummary) 