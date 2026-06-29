

# MetadataConfigurationForReranking
<a name="API_agent-runtime_MetadataConfigurationForReranking"></a>

Contains configurations for the metadata to use in reranking.

## Contents
<a name="API_agent-runtime_MetadataConfigurationForReranking_Contents"></a>

 ** selectionMode **   <a name="bedrock-Type-agent-runtime_MetadataConfigurationForReranking-selectionMode"></a>
Specifies whether to consider all metadata when reranking, or only the metadata that you select. If you specify `SELECTIVE`, include the `selectiveModeConfiguration` field.  
Type: String  
Valid Values: `SELECTIVE | ALL`   
Required: Yes

 ** selectiveModeConfiguration **   <a name="bedrock-Type-agent-runtime_MetadataConfigurationForReranking-selectiveModeConfiguration"></a>
Contains configurations for the metadata fields to include or exclude when considering reranking.  
Type: [RerankingMetadataSelectiveModeConfiguration](API_agent-runtime_RerankingMetadataSelectiveModeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_agent-runtime_MetadataConfigurationForReranking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/MetadataConfigurationForReranking) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/MetadataConfigurationForReranking) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/MetadataConfigurationForReranking) 