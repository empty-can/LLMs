

# S3FilesAccessPointConfiguration
<a name="API_S3FilesAccessPointConfiguration"></a>

Configuration for an Amazon S3 Files access point filesystem mounted into the AgentCore Runtime. S3 Files access points provide shared file storage accessible from your AgentCore Runtime sessions.

## Contents
<a name="API_S3FilesAccessPointConfiguration_Contents"></a>

 ** accessPointArn **   <a name="bedrockagentcorecontrol-Type-S3FilesAccessPointConfiguration-accessPointArn"></a>
The ARN of the S3 Files access point to mount into the AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`   
Required: Yes

 ** mountPath **   <a name="bedrockagentcorecontrol-Type-S3FilesAccessPointConfiguration-mountPath"></a>
The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 200.  
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`   
Required: Yes

## See Also
<a name="API_S3FilesAccessPointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/S3FilesAccessPointConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/S3FilesAccessPointConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/S3FilesAccessPointConfiguration) 