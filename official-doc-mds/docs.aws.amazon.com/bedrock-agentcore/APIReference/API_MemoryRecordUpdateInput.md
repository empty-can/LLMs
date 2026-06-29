

# MemoryRecordUpdateInput
<a name="API_MemoryRecordUpdateInput"></a>

Input structure to update an existing memory record.

## Contents
<a name="API_MemoryRecordUpdateInput_Contents"></a>

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-memoryRecordId"></a>
The unique ID of the memory record to be updated.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** timestamp **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-timestamp"></a>
Time at which the memory record was updated  
Type: Timestamp  
Required: Yes

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-content"></a>
The content to be stored within the memory record.  
Type: [MemoryContent](API_MemoryContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-memoryStrategyId"></a>
The updated ID of the memory strategy that defines how this memory record is grouped.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-metadata"></a>
Metadata key-value pairs to be stored with the memory record.  
Type: String to [MemoryRecordMetadataValue](API_MemoryRecordMetadataValue.md) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecordUpdateInput-namespaces"></a>
The updated list of namespace identifiers for categorizing the memory record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

## See Also
<a name="API_MemoryRecordUpdateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordUpdateInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordUpdateInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordUpdateInput) 