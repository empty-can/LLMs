

# IamCredentialProvider
<a name="API_IamCredentialProvider"></a>

An IAM credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint using IAM credentials and SigV4 signing.

## Contents
<a name="API_IamCredentialProvider_Contents"></a>

 ** service **   <a name="bedrockagentcorecontrol-Type-IamCredentialProvider-service"></a>
The target AWS service name used for SigV4 signing. This value identifies the service that the gateway authenticates with when making requests to the target endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

 ** region **   <a name="bedrockagentcorecontrol-Type-IamCredentialProvider-region"></a>
The AWS Region used for SigV4 signing. If not specified, defaults to the gateway's Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `[a-zA-Z0-9-]+`   
Required: No

## See Also
<a name="API_IamCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/IamCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/IamCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/IamCredentialProvider) 