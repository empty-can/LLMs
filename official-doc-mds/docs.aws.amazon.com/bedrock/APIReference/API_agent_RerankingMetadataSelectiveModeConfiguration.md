

# RerankingMetadataSelectiveModeConfiguration
<a name="API_agent_RerankingMetadataSelectiveModeConfiguration"></a>

Configures the metadata fields to include or exclude during the reranking process when using selective mode.

## Contents
<a name="API_agent_RerankingMetadataSelectiveModeConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fieldsToExclude **   <a name="bedrock-Type-agent_RerankingMetadataSelectiveModeConfiguration-fieldsToExclude"></a>
Specifies the metadata fields to exclude from the reranking process.  
Type: Array of [FieldForReranking](API_agent_FieldForReranking.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** fieldsToInclude **   <a name="bedrock-Type-agent_RerankingMetadataSelectiveModeConfiguration-fieldsToInclude"></a>
Specifies the metadata fields to include in the reranking process.  
Type: Array of [FieldForReranking](API_agent_FieldForReranking.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

## See Also
<a name="API_agent_RerankingMetadataSelectiveModeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RerankingMetadataSelectiveModeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RerankingMetadataSelectiveModeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RerankingMetadataSelectiveModeConfiguration) 