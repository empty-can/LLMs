

# SessionMetadataShape
<a name="API_SessionMetadataShape"></a>

Metadata for a specific session in a batch evaluation, including ground truth data and test scenario identifiers.

## Contents
<a name="API_SessionMetadataShape_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SessionMetadataShape-sessionId"></a>
The unique identifier of the session this metadata applies to.  
Type: String  
Required: Yes

 ** groundTruth **   <a name="BedrockAgentCore-Type-SessionMetadataShape-groundTruth"></a>
The ground truth data for this session, including expected responses and assertions.  
Type: [GroundTruthSource](API_GroundTruthSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-SessionMetadataShape-metadata"></a>
Additional key-value metadata associated with this session.  
Type: String to string map  
Required: No

 ** testScenarioId **   <a name="BedrockAgentCore-Type-SessionMetadataShape-testScenarioId"></a>
An optional test scenario identifier for categorizing and tracking evaluation results.  
Type: String  
Required: No

## See Also
<a name="API_SessionMetadataShape_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionMetadataShape) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionMetadataShape) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionMetadataShape) 