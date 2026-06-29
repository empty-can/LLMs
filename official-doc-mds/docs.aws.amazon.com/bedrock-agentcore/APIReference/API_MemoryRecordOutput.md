

# MemoryRecordOutput
<a name="API_MemoryRecordOutput"></a>

Output information returned after processing a memory record operation.

## Contents
<a name="API_MemoryRecordOutput_Contents"></a>

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-memoryRecordId"></a>
The unique ID associated to the memory record.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-status"></a>
The status of the memory record operation (e.g., SUCCEEDED, FAILED).  
Type: String  
Valid Values: `SUCCEEDED | FAILED`   
Required: Yes

 ** errorCode **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-errorCode"></a>
The error code returned when the memory record operation fails.  
Type: Integer  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-errorMessage"></a>
A human-readable error message describing why the memory record operation failed.  
Type: String  
Required: No

 ** requestIdentifier **   <a name="BedrockAgentCore-Type-MemoryRecordOutput-requestIdentifier"></a>
The client-provided identifier that was used to track this record operation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## See Also
<a name="API_MemoryRecordOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordOutput) 