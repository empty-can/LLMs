

# ExtractionJobMetadata
<a name="API_ExtractionJobMetadata"></a>

Metadata information associated with this extraction job.

## Contents
<a name="API_ExtractionJobMetadata_Contents"></a>

 ** jobID **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-jobID"></a>
The unique identifier for the extraction job.  
Type: String  
Required: Yes

 ** messages **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-messages"></a>
The messages associated with the extraction job.  
Type: [ExtractionJobMessages](API_ExtractionJobMessages.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** actorId **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-actorId"></a>
The identifier of the actor for this extraction job.  
Type: String  
Required: No

 ** failureReason **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-failureReason"></a>
The cause of failure, if the job did not complete successfully.  
Type: String  
Required: No

 ** sessionId **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-sessionId"></a>
The identifier of the session for this extraction job.  
Type: String  
Required: No

 ** status **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-status"></a>
The current status of the extraction job.  
Type: String  
Valid Values: `FAILED`   
Required: No

 ** strategyId **   <a name="BedrockAgentCore-Type-ExtractionJobMetadata-strategyId"></a>
The identifier of the memory strategy for this extraction job.  
Type: String  
Required: No

## See Also
<a name="API_ExtractionJobMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionJobMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionJobMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionJobMetadata) 