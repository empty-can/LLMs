

# MetadataSchemaEntry
<a name="API_MetadataSchemaEntry"></a>

A metadata field definition within a strategy's schema.

## Contents
<a name="API_MetadataSchemaEntry_Contents"></a>

 ** key **   <a name="bedrockagentcorecontrol-Type-MetadataSchemaEntry-key"></a>
The metadata field name. Must match an indexed key to be queryable via metadata filters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

 ** extractionConfig **   <a name="bedrockagentcorecontrol-Type-MetadataSchemaEntry-extractionConfig"></a>
Configuration for extracting this metadata value from conversational content. Applicable only if extractionType is LLM inferred.  
Type: [ExtractionConfig](API_ExtractionConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** extractionType **   <a name="bedrockagentcorecontrol-Type-MetadataSchemaEntry-extractionType"></a>
Specifies whether the metadata value is extracted by the LLM or passed through deterministically from the event.  
Type: String  
Valid Values: `LLM_INFERRED | STRICTLY_CONSISTENT`   
Required: No

 ** type **   <a name="bedrockagentcorecontrol-Type-MetadataSchemaEntry-type"></a>
The MetadataValueType.  
Type: String  
Valid Values: `STRING | STRINGLIST | NUMBER`   
Required: No

## See Also
<a name="API_MetadataSchemaEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MetadataSchemaEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MetadataSchemaEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MetadataSchemaEntry) 