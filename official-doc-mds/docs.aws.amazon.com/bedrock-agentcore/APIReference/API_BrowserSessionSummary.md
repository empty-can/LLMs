

# BrowserSessionSummary
<a name="API_BrowserSessionSummary"></a>

A condensed representation of a browser session in Amazon Bedrock AgentCore. This structure contains key information about a browser session, including identifiers, status, and timestamps, without the full details of the session configuration and streams.

## Contents
<a name="API_BrowserSessionSummary_Contents"></a>

 ** browserIdentifier **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-browserIdentifier"></a>
The unique identifier of the browser associated with the session. This identifier specifies which browser environment is used for the session.  
Type: String  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-createdAt"></a>
The timestamp when the browser session was created. This value is in ISO 8601 format.  
Type: Timestamp  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-sessionId"></a>
The unique identifier of the browser session. This identifier is used in operations that interact with the session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-status"></a>
The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: Yes

 ** lastUpdatedAt **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-lastUpdatedAt"></a>
The timestamp when the browser session was last updated. This value is in ISO 8601 format.  
Type: Timestamp  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-BrowserSessionSummary-name"></a>
The name of the browser session. This name helps identify and manage the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_BrowserSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserSessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserSessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserSessionSummary) 