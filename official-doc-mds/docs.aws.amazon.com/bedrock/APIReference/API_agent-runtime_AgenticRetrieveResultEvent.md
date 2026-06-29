

# AgenticRetrieveResultEvent
<a name="API_agent-runtime_AgenticRetrieveResultEvent"></a>

An event containing agentic retrieval results.

## Contents
<a name="API_agent-runtime_AgenticRetrieveResultEvent_Contents"></a>

 ** results **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveResultEvent-results"></a>
The list of retrieved result items.  
Type: Array of [AgenticRetrieveResultItem](API_agent-runtime_AgenticRetrieveResultItem.md) objects  
Required: Yes

 ** generatedResponse **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveResultEvent-generatedResponse"></a>
The generated response. Present only when generateResponse is true.  
Type: [AgenticRetrieveGeneratedResponse](API_agent-runtime_AgenticRetrieveGeneratedResponse.md) object  
Required: No

 ** nextToken **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveResultEvent-nextToken"></a>
Opaque continuation token for paginated results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveResultEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveResultEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveResultEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveResultEvent) 