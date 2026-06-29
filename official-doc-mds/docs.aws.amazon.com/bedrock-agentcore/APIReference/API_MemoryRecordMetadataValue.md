

# MemoryRecordMetadataValue
<a name="API_MemoryRecordMetadataValue"></a>

The value of a memory record metadata entry.

## Contents
<a name="API_MemoryRecordMetadataValue_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dateTimeValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-dateTimeValue"></a>
A timestamp value in ISO 8601 UTC format.  
Type: Timestamp  
Required: No

 ** numberValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-numberValue"></a>
A numeric value.  
Type: Double  
Required: No

 ** stringListValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-stringListValue"></a>
A list of string values.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** stringValue **   <a name="BedrockAgentCore-Type-MemoryRecordMetadataValue-stringValue"></a>
A string value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## See Also
<a name="API_MemoryRecordMetadataValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordMetadataValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordMetadataValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordMetadataValue) 