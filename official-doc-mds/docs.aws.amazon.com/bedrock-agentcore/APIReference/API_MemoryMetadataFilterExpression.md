

# MemoryMetadataFilterExpression
<a name="API_MemoryMetadataFilterExpression"></a>

Filters to apply to metadata associated with a memory. Specify the metadata key and value in the `left` and `right` fields and use the `operator` field to define the relationship to match.

## Contents
<a name="API_MemoryMetadataFilterExpression_Contents"></a>

 ** left **   <a name="BedrockAgentCore-Type-MemoryMetadataFilterExpression-left"></a>
The metadata key to evaluate.  
Type: [MemoryRecordLeftExpression](API_MemoryRecordLeftExpression.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** operator **   <a name="BedrockAgentCore-Type-MemoryMetadataFilterExpression-operator"></a>
The relationship between the metadata key and value to match when applying the metadata filter.  
Type: String  
Valid Values: `EQUALS_TO | EXISTS | NOT_EXISTS | BEFORE | AFTER | CONTAINS | GREATER_THAN | GREATER_THAN_OR_EQUALS | LESS_THAN | LESS_THAN_OR_EQUALS`   
Required: Yes

 ** right **   <a name="BedrockAgentCore-Type-MemoryMetadataFilterExpression-right"></a>
The value to compare against. Required for all operators except EXISTS and NOT\_EXISTS.  
Type: [MemoryRecordRightExpression](API_MemoryRecordRightExpression.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_MemoryMetadataFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryMetadataFilterExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryMetadataFilterExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryMetadataFilterExpression) 