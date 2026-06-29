

# MemorySessionSummary
<a name="API_agent-runtime_MemorySessionSummary"></a>

Contains details of a session summary.

## Contents
<a name="API_agent-runtime_MemorySessionSummary_Contents"></a>

 ** memoryId **   <a name="bedrock-Type-agent-runtime_MemorySessionSummary-memoryId"></a>
The unique identifier of the memory where the session summary is stored.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: No

 ** sessionExpiryTime **   <a name="bedrock-Type-agent-runtime_MemorySessionSummary-sessionExpiryTime"></a>
The time when the memory duration for the session is set to end.  
Type: Timestamp  
Required: No

 ** sessionId **   <a name="bedrock-Type-agent-runtime_MemorySessionSummary-sessionId"></a>
The identifier for this session.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: No

 ** sessionStartTime **   <a name="bedrock-Type-agent-runtime_MemorySessionSummary-sessionStartTime"></a>
The start time for this session.  
Type: Timestamp  
Required: No

 ** summaryText **   <a name="bedrock-Type-agent-runtime_MemorySessionSummary-summaryText"></a>
The summarized text for this session.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 25000000.  
Required: No

## See Also
<a name="API_agent-runtime_MemorySessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/MemorySessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/MemorySessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/MemorySessionSummary) 