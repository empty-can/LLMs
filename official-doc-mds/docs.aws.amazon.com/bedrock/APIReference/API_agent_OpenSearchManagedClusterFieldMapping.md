

# OpenSearchManagedClusterFieldMapping
<a name="API_agent_OpenSearchManagedClusterFieldMapping"></a>

Contains the names of the fields to which to map information about the vector store.

## Contents
<a name="API_agent_OpenSearchManagedClusterFieldMapping_Contents"></a>

 ** metadataField **   <a name="bedrock-Type-agent_OpenSearchManagedClusterFieldMapping-metadataField"></a>
The name of the field in which Amazon Bedrock stores metadata about the vector store.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

 ** textField **   <a name="bedrock-Type-agent_OpenSearchManagedClusterFieldMapping-textField"></a>
The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

 ** vectorField **   <a name="bedrock-Type-agent_OpenSearchManagedClusterFieldMapping-vectorField"></a>
The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

## See Also
<a name="API_agent_OpenSearchManagedClusterFieldMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/OpenSearchManagedClusterFieldMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/OpenSearchManagedClusterFieldMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/OpenSearchManagedClusterFieldMapping) 