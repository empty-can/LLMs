

# MetadataConfigurationForReranking
<a name="API_MetadataConfigurationForReranking"></a>

Configuration for how metadata should be used during the reranking process in Knowledge Base vector searches. This determines which metadata fields are included or excluded when reordering search results.

## Contents
<a name="API_MetadataConfigurationForReranking_Contents"></a>

 ** selectionMode **   <a name="bedrock-Type-MetadataConfigurationForReranking-selectionMode"></a>
The mode for selecting which metadata fields to include in the reranking process. Valid values are ALL (use all available metadata fields) or SELECTIVE (use only specified fields).  
Type: String  
Valid Values: `SELECTIVE | ALL`   
Required: Yes

 ** selectiveModeConfiguration **   <a name="bedrock-Type-MetadataConfigurationForReranking-selectiveModeConfiguration"></a>
Configuration for selective mode, which allows you to explicitly include or exclude specific metadata fields during reranking. This is only used when selectionMode is set to SELECTIVE.  
Type: [RerankingMetadataSelectiveModeConfiguration](API_RerankingMetadataSelectiveModeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_MetadataConfigurationForReranking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/MetadataConfigurationForReranking) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/MetadataConfigurationForReranking) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/MetadataConfigurationForReranking) 