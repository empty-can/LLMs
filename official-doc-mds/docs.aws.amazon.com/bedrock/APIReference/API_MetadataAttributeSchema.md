

# MetadataAttributeSchema
<a name="API_MetadataAttributeSchema"></a>

Defines the schema for a metadata attribute used in Knowledge Base vector searches. Metadata attributes provide additional context for documents and can be used for filtering and reranking search results.

## Contents
<a name="API_MetadataAttributeSchema_Contents"></a>

 ** description **   <a name="bedrock-Type-MetadataAttributeSchema-description"></a>
An optional description of the metadata attribute that provides additional context about its purpose and usage.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: Yes

 ** key **   <a name="bedrock-Type-MetadataAttributeSchema-key"></a>
The unique identifier for the metadata attribute. This key is used to reference the attribute in filter expressions and reranking configurations.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\s\S]+`   
Required: Yes

 ** type **   <a name="bedrock-Type-MetadataAttributeSchema-type"></a>
The data type of the metadata attribute. The type determines how the attribute can be used in filter expressions and reranking.  
Type: String  
Valid Values: `STRING | NUMBER | BOOLEAN | STRING_LIST`   
Required: Yes

## See Also
<a name="API_MetadataAttributeSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/MetadataAttributeSchema) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/MetadataAttributeSchema) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/MetadataAttributeSchema) 