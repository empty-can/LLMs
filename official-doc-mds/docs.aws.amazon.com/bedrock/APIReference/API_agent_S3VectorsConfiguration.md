

# S3VectorsConfiguration
<a name="API_agent_S3VectorsConfiguration"></a>

Contains the storage configuration of the knowledge base for S3 vectors.

## Contents
<a name="API_agent_S3VectorsConfiguration_Contents"></a>

 ** indexArn **   <a name="bedrock-Type-agent_S3VectorsConfiguration-indexArn"></a>
The Amazon Resource Name (ARN) of the vector index used for the knowledge base. This ARN identifies the specific vector index resource within Amazon Bedrock.  
Type: String  
Required: No

 ** indexName **   <a name="bedrock-Type-agent_S3VectorsConfiguration-indexName"></a>
The name of the vector index used for the knowledge base. This name identifies the vector index within the Amazon Bedrock service.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Required: No

 ** vectorBucketArn **   <a name="bedrock-Type-agent_S3VectorsConfiguration-vectorBucketArn"></a>
The Amazon Resource Name (ARN) of the S3 bucket where vector embeddings are stored. This bucket contains the vector data used by the knowledge base.  
Type: String  
Required: No

## See Also
<a name="API_agent_S3VectorsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/S3VectorsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/S3VectorsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/S3VectorsConfiguration) 