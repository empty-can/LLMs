

# MemoryRecord
<a name="API_MemoryRecord"></a>

Contains information about a memory record in an AgentCore Memory resource.

## Contents
<a name="API_MemoryRecord_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-MemoryRecord-content"></a>
The content of the memory record.  
Type: [MemoryContent](API_MemoryContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** createdAt **   <a name="BedrockAgentCore-Type-MemoryRecord-createdAt"></a>
The timestamp when the memory record was created.  
Type: Timestamp  
Required: Yes

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecord-memoryRecordId"></a>
The unique identifier of the memory record.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** memoryStrategyId **   <a name="BedrockAgentCore-Type-MemoryRecord-memoryStrategyId"></a>
The identifier of the memory strategy associated with this record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** namespaces **   <a name="BedrockAgentCore-Type-MemoryRecord-namespaces"></a>
The namespaces associated with this memory record. Namespaces help organize and categorize memory records.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: Yes

 ** metadata **   <a name="BedrockAgentCore-Type-MemoryRecord-metadata"></a>
A map of metadata key-value pairs associated with a memory record.  
Type: String to [MemoryRecordMetadataValue](API_MemoryRecordMetadataValue.md) object map  
Map Entries: Maximum number of 20 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## See Also
<a name="API_MemoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecord) 