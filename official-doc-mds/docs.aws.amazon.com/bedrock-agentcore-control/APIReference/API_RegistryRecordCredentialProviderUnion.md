

# RegistryRecordCredentialProviderUnion
<a name="API_RegistryRecordCredentialProviderUnion"></a>

Union of supported credential provider types for registry record synchronization.

## Contents
<a name="API_RegistryRecordCredentialProviderUnion_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** iamCredentialProvider **   <a name="bedrockagentcorecontrol-Type-RegistryRecordCredentialProviderUnion-iamCredentialProvider"></a>
The IAM credential provider configuration for authenticating with the external source using SigV4 signing.  
Type: [RegistryRecordIamCredentialProvider](API_RegistryRecordIamCredentialProvider.md) object  
Required: No

 ** oauthCredentialProvider **   <a name="bedrockagentcorecontrol-Type-RegistryRecordCredentialProviderUnion-oauthCredentialProvider"></a>
The OAuth credential provider configuration for authenticating with the external source.  
Type: [RegistryRecordOAuthCredentialProvider](API_RegistryRecordOAuthCredentialProvider.md) object  
Required: No

## See Also
<a name="API_RegistryRecordCredentialProviderUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RegistryRecordCredentialProviderUnion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RegistryRecordCredentialProviderUnion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RegistryRecordCredentialProviderUnion) 