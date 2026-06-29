

# CustomS3Location
<a name="API_agent_CustomS3Location"></a>

Contains information about the Amazon S3 location of the file containing the content to ingest into a knowledge base connected to a custom data source.

## Contents
<a name="API_agent_CustomS3Location_Contents"></a>

 ** uri **   <a name="bedrock-Type-agent_CustomS3Location-uri"></a>
The S3 URI of the file containing the content to ingest.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.{1,1024}`   
Required: Yes

 ** bucketOwnerAccountId **   <a name="bedrock-Type-agent_CustomS3Location-bucketOwnerAccountId"></a>
The identifier of the AWS account that owns the S3 bucket containing the content to ingest.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: No

## See Also
<a name="API_agent_CustomS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CustomS3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CustomS3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CustomS3Location) 