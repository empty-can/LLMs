

# MemoryRecordCreateInput
<a name="API_MemoryRecordCreateInput"></a>

Input structure to create a new memory record.

## Contents
<a name="API_MemoryRecordCreateInput_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-content"></a>
The content to be stored within the memory record.  
Type: [MemoryContent](API_MemoryContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-namespaces"></a>
A list of namespace identifiers that categorize or group the memory record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: Yes

 ** requestIdentifier **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-requestIdentifier"></a>
A client-provided identifier for tracking this specific record creation request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** timestamp **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-timestamp"></a>
Time at which the memory record was created.  
Type: Timestamp  
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-memoryStrategyId"></a>
The ID of the memory strategy that defines how this memory record is grouped.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecordCreateInput-metadata"></a>
Metadata key-value pairs to be stored with the memory record.  
Type: String to [MemoryRecordMetadataValue](API_MemoryRecordMetadataValue.md) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## See Also
<a name="API_MemoryRecordCreateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordCreateInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordCreateInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordCreateInput) 