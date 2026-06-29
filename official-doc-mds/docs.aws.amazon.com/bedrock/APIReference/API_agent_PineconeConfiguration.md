

# PineconeConfiguration
<a name="API_agent_PineconeConfiguration"></a>

Contains details about the storage configuration of the knowledge base in Pinecone. For more information, see [Create a vector index in Pinecone](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-pinecone.html).

## Contents
<a name="API_agent_PineconeConfiguration_Contents"></a>

 ** connectionString **   <a name="bedrock-Type-agent_PineconeConfiguration-connectionString"></a>
The endpoint URL for your index management page.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: Yes

 ** credentialsSecretArn **   <a name="bedrock-Type-agent_PineconeConfiguration-credentialsSecretArn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that is linked to your Pinecone API key.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: Yes

 ** fieldMapping **   <a name="bedrock-Type-agent_PineconeConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [PineconeFieldMapping](API_agent_PineconeFieldMapping.md) object  
Required: Yes

 ** namespace **   <a name="bedrock-Type-agent_PineconeConfiguration-namespace"></a>
The namespace to be used to write new data to your database.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*`   
Required: No

## See Also
<a name="API_agent_PineconeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PineconeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PineconeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PineconeConfiguration) 