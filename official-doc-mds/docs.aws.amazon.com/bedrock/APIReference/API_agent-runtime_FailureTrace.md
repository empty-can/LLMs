

# FailureTrace
<a name="API_agent-runtime_FailureTrace"></a>

Contains information about the failure of the interaction.

## Contents
<a name="API_agent-runtime_FailureTrace_Contents"></a>

 ** failureCode **   <a name="bedrock-Type-agent-runtime_FailureTrace-failureCode"></a>
The failure code for the trace.  
Type: Integer  
Required: No

 ** failureReason **   <a name="bedrock-Type-agent-runtime_FailureTrace-failureReason"></a>
The reason the interaction failed.  
Type: String  
Required: No

 ** metadata **   <a name="bedrock-Type-agent-runtime_FailureTrace-metadata"></a>
Information about the failure that occurred.  
Type: [Metadata](API_agent-runtime_Metadata.md) object  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_FailureTrace-traceId"></a>
The unique identifier of the trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

## See Also
<a name="API_agent-runtime_FailureTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FailureTrace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FailureTrace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FailureTrace) 