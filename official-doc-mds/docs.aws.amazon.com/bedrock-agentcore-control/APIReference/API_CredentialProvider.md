

# CredentialProvider
<a name="API_CredentialProvider"></a>

A credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint.

## Contents
<a name="API_CredentialProvider_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiKeyCredentialProvider **   <a name="bedrockagentcorecontrol-Type-CredentialProvider-apiKeyCredentialProvider"></a>
The API key credential provider. This provider uses an API key to authenticate with the target endpoint.  
Type: [ApiKeyCredentialProvider](API_ApiKeyCredentialProvider.md) object  
Required: No

 ** iamCredentialProvider **   <a name="bedrockagentcorecontrol-Type-CredentialProvider-iamCredentialProvider"></a>
The IAM credential provider. This provider uses IAM authentication with SigV4 signing to access the target endpoint.  
Type: [IamCredentialProvider](API_IamCredentialProvider.md) object  
Required: No

 ** oauthCredentialProvider **   <a name="bedrockagentcorecontrol-Type-CredentialProvider-oauthCredentialProvider"></a>
The OAuth credential provider. This provider uses OAuth authentication to access the target endpoint.  
Type: [OAuthCredentialProvider](API_OAuthCredentialProvider.md) object  
Required: No

## See Also
<a name="API_CredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CredentialProvider) 