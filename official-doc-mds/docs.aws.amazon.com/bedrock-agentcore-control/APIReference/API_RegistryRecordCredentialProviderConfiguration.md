

# RegistryRecordCredentialProviderConfiguration
<a name="API_RegistryRecordCredentialProviderConfiguration"></a>

A pairing of a credential provider type with its corresponding provider details for authenticating with external sources.

## Contents
<a name="API_RegistryRecordCredentialProviderConfiguration_Contents"></a>

 ** credentialProvider **   <a name="bedrockagentcorecontrol-Type-RegistryRecordCredentialProviderConfiguration-credentialProvider"></a>
The credential provider configuration details. The structure depends on the `credentialProviderType`.  
Type: [RegistryRecordCredentialProviderUnion](API_RegistryRecordCredentialProviderUnion.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** credentialProviderType **   <a name="bedrockagentcorecontrol-Type-RegistryRecordCredentialProviderConfiguration-credentialProviderType"></a>
The type of credential provider.  
+  `OAUTH` - OAuth-based authentication.
+  `IAM` - AWS IAM-based authentication using SigV4 signing.
Type: String  
Valid Values: `OAUTH | IAM`   
Required: Yes

## See Also
<a name="API_RegistryRecordCredentialProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RegistryRecordCredentialProviderConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RegistryRecordCredentialProviderConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RegistryRecordCredentialProviderConfiguration) 