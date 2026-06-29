

# OpenSearchManagedClusterConfiguration
<a name="API_agent_OpenSearchManagedClusterConfiguration"></a>

Contains details about the Managed Cluster configuration of the knowledge base in Amazon OpenSearch Service. For more information, see [Create a vector index in OpenSearch Managed Cluster](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html).

## Contents
<a name="API_agent_OpenSearchManagedClusterConfiguration_Contents"></a>

 ** domainArn **   <a name="bedrock-Type-agent_OpenSearchManagedClusterConfiguration-domainArn"></a>
The Amazon Resource Name (ARN) of the OpenSearch domain.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov|-iso):es:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:domain/[a-z][a-z0-9-]{3,28}`   
Required: Yes

 ** domainEndpoint **   <a name="bedrock-Type-agent_OpenSearchManagedClusterConfiguration-domainEndpoint"></a>
The endpoint URL the OpenSearch domain.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `https://.*`   
Required: Yes

 ** fieldMapping **   <a name="bedrock-Type-agent_OpenSearchManagedClusterConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [OpenSearchManagedClusterFieldMapping](API_agent_OpenSearchManagedClusterFieldMapping.md) object  
Required: Yes

 ** vectorIndexName **   <a name="bedrock-Type-agent_OpenSearchManagedClusterConfiguration-vectorIndexName"></a>
The name of the vector store.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?![\-_+.])[a-z0-9][a-z0-9\-_\.]*`   
Required: Yes

## See Also
<a name="API_agent_OpenSearchManagedClusterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/OpenSearchManagedClusterConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/OpenSearchManagedClusterConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/OpenSearchManagedClusterConfiguration) 