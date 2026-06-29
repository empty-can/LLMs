

# HarnessReasoningContentBlockDelta
<a name="API_HarnessReasoningContentBlockDelta"></a>

A delta update to a reasoning content block.

## Contents
<a name="API_HarnessReasoningContentBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** redactedContent **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlockDelta-redactedContent"></a>
Redacted reasoning content.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** signature **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlockDelta-signature"></a>
Signature for the reasoning content.  
Type: String  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-HarnessReasoningContentBlockDelta-text"></a>
Reasoning text delta.  
Type: String  
Required: No

## See Also
<a name="API_HarnessReasoningContentBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessReasoningContentBlockDelta) 