

# CredentialProviderConfiguration
<a name="API_CredentialProviderConfiguration"></a>

The configuration for a credential provider. This structure defines how the gateway authenticates with the target endpoint.

## Contents
<a name="API_CredentialProviderConfiguration_Contents"></a>

 ** credentialProviderType **   <a name="bedrockagentcorecontrol-Type-CredentialProviderConfiguration-credentialProviderType"></a>
The type of credential provider. This field specifies which authentication method the gateway uses.  
Type: String  
Valid Values: `GATEWAY_IAM_ROLE | OAUTH | API_KEY | CALLER_IAM_CREDENTIALS | JWT_PASSTHROUGH`   
Required: Yes

 ** credentialProvider **   <a name="bedrockagentcorecontrol-Type-CredentialProviderConfiguration-credentialProvider"></a>
The credential provider. This field contains the specific configuration for the credential provider type.  
Type: [CredentialProvider](API_CredentialProvider.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_CredentialProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CredentialProviderConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CredentialProviderConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CredentialProviderConfiguration) 