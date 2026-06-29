

# RdsFieldMapping
<a name="API_agent_RdsFieldMapping"></a>

Contains the names of the fields to which to map information about the vector store.

## Contents
<a name="API_agent_RdsFieldMapping_Contents"></a>

 ** metadataField **   <a name="bedrock-Type-agent_RdsFieldMapping-metadataField"></a>
The name of the field in which Amazon Bedrock stores metadata about the vector store.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

 ** primaryKeyField **   <a name="bedrock-Type-agent_RdsFieldMapping-primaryKeyField"></a>
The name of the field in which Amazon Bedrock stores the ID for each entry.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

 ** textField **   <a name="bedrock-Type-agent_RdsFieldMapping-textField"></a>
The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

 ** vectorField **   <a name="bedrock-Type-agent_RdsFieldMapping-vectorField"></a>
The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

 ** customMetadataField **   <a name="bedrock-Type-agent_RdsFieldMapping-customMetadataField"></a>
Provide a name for the universal metadata field where Amazon Bedrock will store any custom metadata from your data source.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 63.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: No

## See Also
<a name="API_agent_RdsFieldMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RdsFieldMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RdsFieldMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RdsFieldMapping) 