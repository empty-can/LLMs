

# SupplementalDataStorageLocation
<a name="API_agent_SupplementalDataStorageLocation"></a>

Contains information about a storage location for multimedia content (images, audio, and video) extracted from multimodal documents in your data source.

## Contents
<a name="API_agent_SupplementalDataStorageLocation_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_SupplementalDataStorageLocation-type"></a>
Specifies the storage service used for this location.  
Type: String  
Valid Values: `S3`   
Required: Yes

 ** s3Location **   <a name="bedrock-Type-agent_SupplementalDataStorageLocation-s3Location"></a>
Contains information about the Amazon S3 location for the extracted multimedia content.  
Type: [S3Location](API_agent_S3Location.md) object  
Required: No

## See Also
<a name="API_agent_SupplementalDataStorageLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SupplementalDataStorageLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SupplementalDataStorageLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SupplementalDataStorageLocation) 