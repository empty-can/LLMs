

# ServerSideEncryptionConfiguration
<a name="API_agent_ServerSideEncryptionConfiguration"></a>

Contains the configuration for server-side encryption for your managed knowledge base.

## Contents
<a name="API_agent_ServerSideEncryptionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="bedrock-Type-agent_ServerSideEncryptionConfiguration-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

## See Also
<a name="API_agent_ServerSideEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ServerSideEncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ServerSideEncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ServerSideEncryptionConfiguration) 