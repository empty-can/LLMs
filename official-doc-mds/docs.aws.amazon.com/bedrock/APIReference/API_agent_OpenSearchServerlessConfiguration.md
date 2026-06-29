

# OpenSearchServerlessConfiguration
<a name="API_agent_OpenSearchServerlessConfiguration"></a>

Contains details about the storage configuration of the knowledge base in Amazon OpenSearch Service. For more information, see [Create a vector index in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html).

## Contents
<a name="API_agent_OpenSearchServerlessConfiguration_Contents"></a>

 ** collectionArn **   <a name="bedrock-Type-agent_OpenSearchServerlessConfiguration-collectionArn"></a>
The Amazon Resource Name (ARN) of the OpenSearch Service vector store.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws:aoss:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:collection/[a-z0-9-]{3,32}`   
Required: Yes

 ** fieldMapping **   <a name="bedrock-Type-agent_OpenSearchServerlessConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [OpenSearchServerlessFieldMapping](API_agent_OpenSearchServerlessFieldMapping.md) object  
Required: Yes

 ** vectorIndexName **   <a name="bedrock-Type-agent_OpenSearchServerlessConfiguration-vectorIndexName"></a>
The name of the vector store.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

## See Also
<a name="API_agent_OpenSearchServerlessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/OpenSearchServerlessConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/OpenSearchServerlessConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/OpenSearchServerlessConfiguration) 