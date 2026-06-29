

# S3DataSourceConfiguration
<a name="API_agent_S3DataSourceConfiguration"></a>

The configuration information to connect to Amazon S3 as your data source for self-managed knowledge bases. To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html).

## Contents
<a name="API_agent_S3DataSourceConfiguration_Contents"></a>

 ** bucketArn **   <a name="bedrock-Type-agent_S3DataSourceConfiguration-bucketArn"></a>
The Amazon Resource Name (ARN) of the S3 bucket that contains your data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):s3:::[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`   
Required: Yes

 ** bucketOwnerAccountId **   <a name="bedrock-Type-agent_S3DataSourceConfiguration-bucketOwnerAccountId"></a>
The account ID for the owner of the S3 bucket.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: No

 ** inclusionPrefixes **   <a name="bedrock-Type-agent_S3DataSourceConfiguration-inclusionPrefixes"></a>
A list of S3 prefixes to include certain files or content. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

## See Also
<a name="API_agent_S3DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/S3DataSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/S3DataSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/S3DataSourceConfiguration) 