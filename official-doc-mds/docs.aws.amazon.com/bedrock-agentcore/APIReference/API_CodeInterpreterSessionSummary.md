

# CodeInterpreterSessionSummary
<a name="API_CodeInterpreterSessionSummary"></a>

A condensed representation of a code interpreter session in Amazon Bedrock AgentCore. This structure contains key information about a code interpreter session, including identifiers, status, and timestamps, without the full details of the session configuration.

## Contents
<a name="API_CodeInterpreterSessionSummary_Contents"></a>

 ** codeInterpreterIdentifier **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session. This identifier specifies which code interpreter environment is used for the session.  
Type: String  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-createdAt"></a>
The timestamp when the code interpreter session was created. This value is in ISO 8601 format.  
Type: Timestamp  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-sessionId"></a>
The unique identifier of the code interpreter session. This identifier is used in operations that interact with the session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-status"></a>
The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: Yes

 ** lastUpdatedAt **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-lastUpdatedAt"></a>
The timestamp when the code interpreter session was last updated. This value is in ISO 8601 format.  
Type: Timestamp  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-CodeInterpreterSessionSummary-name"></a>
The name of the code interpreter session. This name helps identify and manage the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_CodeInterpreterSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CodeInterpreterSessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CodeInterpreterSessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CodeInterpreterSessionSummary) 