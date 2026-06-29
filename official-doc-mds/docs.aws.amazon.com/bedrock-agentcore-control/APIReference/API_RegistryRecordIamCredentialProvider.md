

# RegistryRecordIamCredentialProvider
<a name="API_RegistryRecordIamCredentialProvider"></a>

IAM credential provider configuration for authenticating with an external source using SigV4 signing during synchronization.

## Contents
<a name="API_RegistryRecordIamCredentialProvider_Contents"></a>

 ** region **   <a name="bedrockagentcorecontrol-Type-RegistryRecordIamCredentialProvider-region"></a>
The AWS region for SigV4 signing (for example, `us-west-2`). If not specified, the region is extracted from the MCP server URL hostname, with fallback to the service's own region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9-]+`   
Required: No

 ** roleArn **   <a name="bedrockagentcorecontrol-Type-RegistryRecordIamCredentialProvider-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assume for SigV4 signing.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

 ** service **   <a name="bedrockagentcorecontrol-Type-RegistryRecordIamCredentialProvider-service"></a>
The SigV4 signing service name (for example, `execute-api` or `bedrock-agentcore`).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## See Also
<a name="API_RegistryRecordIamCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RegistryRecordIamCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RegistryRecordIamCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RegistryRecordIamCredentialProvider) 