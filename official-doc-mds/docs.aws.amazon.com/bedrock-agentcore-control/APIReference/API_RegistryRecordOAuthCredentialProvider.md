

# RegistryRecordOAuthCredentialProvider
<a name="API_RegistryRecordOAuthCredentialProvider"></a>

OAuth credential provider configuration for authenticating with an external source during synchronization.

## Contents
<a name="API_RegistryRecordOAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="bedrockagentcorecontrol-Type-RegistryRecordOAuthCredentialProvider-providerArn"></a>
The Amazon Resource Name (ARN) of the OAuth credential provider resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`   
Required: Yes

 ** customParameters **   <a name="bedrockagentcorecontrol-Type-RegistryRecordOAuthCredentialProvider-customParameters"></a>
Additional custom parameters for the OAuth flow.  
Type: String to string map  
Required: No

 ** grantType **   <a name="bedrockagentcorecontrol-Type-RegistryRecordOAuthCredentialProvider-grantType"></a>
The OAuth grant type. Currently only `CLIENT_CREDENTIALS` is supported.  
Type: String  
Valid Values: `CLIENT_CREDENTIALS`   
Required: No

 ** scopes **   <a name="bedrockagentcorecontrol-Type-RegistryRecordOAuthCredentialProvider-scopes"></a>
The OAuth scopes to request during authentication.  
Type: Array of strings  
Required: No

## See Also
<a name="API_RegistryRecordOAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RegistryRecordOAuthCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RegistryRecordOAuthCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RegistryRecordOAuthCredentialProvider) 