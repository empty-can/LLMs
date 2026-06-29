

# AffectedSession
<a name="API_AffectedSession"></a>

A session affected by a detected failure pattern, including root cause details.

## Contents
<a name="API_AffectedSession_Contents"></a>

 ** explanation **   <a name="BedrockAgentCore-Type-AffectedSession-explanation"></a>
An explanation of how the failure manifested in this session.  
Type: String  
Required: Yes

 ** failureSpans **   <a name="BedrockAgentCore-Type-AffectedSession-failureSpans"></a>
The list of spans where failures were detected in this session.  
Type: Array of [FailureSpanDetail](API_FailureSpanDetail.md) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** fixType **   <a name="BedrockAgentCore-Type-AffectedSession-fixType"></a>
The type of fix recommended for this failure.  
Type: String  
Required: Yes

 ** recommendation **   <a name="BedrockAgentCore-Type-AffectedSession-recommendation"></a>
The specific fix recommendation for this session.  
Type: String  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-AffectedSession-sessionId"></a>
The unique identifier of the affected session.  
Type: String  
Required: Yes

## See Also
<a name="API_AffectedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AffectedSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AffectedSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AffectedSession) 