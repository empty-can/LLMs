

# RerankingMetadataSelectiveModeConfiguration
<a name="API_agent-runtime_RerankingMetadataSelectiveModeConfiguration"></a>

Contains configurations for the metadata fields to include or exclude when considering reranking. If you include the `fieldsToExclude` field, the reranker ignores all the metadata fields that you specify. If you include the `fieldsToInclude` field, the reranker uses only the metadata fields that you specify and ignores all others. You can include only one of these fields.

## Contents
<a name="API_agent-runtime_RerankingMetadataSelectiveModeConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fieldsToExclude **   <a name="bedrock-Type-agent-runtime_RerankingMetadataSelectiveModeConfiguration-fieldsToExclude"></a>
An array of objects, each of which specifies a metadata field to exclude from consideration when reranking.  
Type: Array of [FieldForReranking](API_agent-runtime_FieldForReranking.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** fieldsToInclude **   <a name="bedrock-Type-agent-runtime_RerankingMetadataSelectiveModeConfiguration-fieldsToInclude"></a>
An array of objects, each of which specifies a metadata field to include in consideration when reranking. The remaining metadata fields are ignored.  
Type: Array of [FieldForReranking](API_agent-runtime_FieldForReranking.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

## See Also
<a name="API_agent-runtime_RerankingMetadataSelectiveModeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RerankingMetadataSelectiveModeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RerankingMetadataSelectiveModeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RerankingMetadataSelectiveModeConfiguration) 