

# RerankingMetadataSelectiveModeConfiguration
<a name="API_RerankingMetadataSelectiveModeConfiguration"></a>

Configuration for selectively including or excluding metadata fields during the reranking process. This allows you to control which metadata attributes are considered when reordering search results.

## Contents
<a name="API_RerankingMetadataSelectiveModeConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fieldsToExclude **   <a name="bedrock-Type-RerankingMetadataSelectiveModeConfiguration-fieldsToExclude"></a>
A list of metadata field names to explicitly exclude from the reranking process. All metadata fields except these will be considered when reordering search results. This parameter cannot be used together with fieldsToInclude.  
Type: Array of [FieldForReranking](API_FieldForReranking.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** fieldsToInclude **   <a name="bedrock-Type-RerankingMetadataSelectiveModeConfiguration-fieldsToInclude"></a>
A list of metadata field names to explicitly include in the reranking process. Only these fields will be considered when reordering search results. This parameter cannot be used together with fieldsToExclude.  
Type: Array of [FieldForReranking](API_FieldForReranking.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

## See Also
<a name="API_RerankingMetadataSelectiveModeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RerankingMetadataSelectiveModeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RerankingMetadataSelectiveModeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RerankingMetadataSelectiveModeConfiguration) 