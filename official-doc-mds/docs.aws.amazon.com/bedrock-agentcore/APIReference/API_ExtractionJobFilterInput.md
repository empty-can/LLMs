

# ExtractionJobFilterInput
<a name="API_ExtractionJobFilterInput"></a>

Filters for querying memory extraction jobs based on various criteria.

## Contents
<a name="API_ExtractionJobFilterInput_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-actorId"></a>
The identifier of the actor. If specified, only extraction jobs with this actor ID are returned.  
Type: String  
Required: No

 ** sessionId **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-sessionId"></a>
The unique identifier of the session. If specified, only extraction jobs with this session ID are returned.  
Type: String  
Required: No

 ** status **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-status"></a>
The status of the extraction job. If specified, only extraction jobs with this status are returned.  
Type: String  
Valid Values: `FAILED`   
Required: No

 ** strategyId **   <a name="BedrockAgentCore-Type-ExtractionJobFilterInput-strategyId"></a>
The memory strategy identifier to filter extraction jobs by. If specified, only extraction jobs with this strategy ID are returned.  
Type: String  
Required: No

## See Also
<a name="API_ExtractionJobFilterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionJobFilterInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionJobFilterInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionJobFilterInput) 