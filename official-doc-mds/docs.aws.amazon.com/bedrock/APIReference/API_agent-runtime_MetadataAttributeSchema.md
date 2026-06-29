

# MetadataAttributeSchema
<a name="API_agent-runtime_MetadataAttributeSchema"></a>

Details about a metadata attribute.

## Contents
<a name="API_agent-runtime_MetadataAttributeSchema_Contents"></a>

 ** description **   <a name="bedrock-Type-agent-runtime_MetadataAttributeSchema-description"></a>
The attribute's description.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: Yes

 ** key **   <a name="bedrock-Type-agent-runtime_MetadataAttributeSchema-key"></a>
The attribute's key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\s\S]+`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent-runtime_MetadataAttributeSchema-type"></a>
The attribute's type.  
Type: String  
Valid Values: `STRING | NUMBER | BOOLEAN | STRING_LIST`   
Required: Yes

## See Also
<a name="API_agent-runtime_MetadataAttributeSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/MetadataAttributeSchema) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/MetadataAttributeSchema) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/MetadataAttributeSchema) 