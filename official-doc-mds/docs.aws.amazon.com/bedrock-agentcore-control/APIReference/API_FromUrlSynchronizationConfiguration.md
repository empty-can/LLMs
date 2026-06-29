

# FromUrlSynchronizationConfiguration
<a name="API_FromUrlSynchronizationConfiguration"></a>

Configuration for synchronizing from a URL-based MCP server.

## Contents
<a name="API_FromUrlSynchronizationConfiguration_Contents"></a>

 ** url **   <a name="bedrockagentcorecontrol-Type-FromUrlSynchronizationConfiguration-url"></a>
The HTTPS URL of the MCP server to synchronize from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://.*`   
Required: Yes

 ** credentialProviderConfigurations **   <a name="bedrockagentcorecontrol-Type-FromUrlSynchronizationConfiguration-credentialProviderConfigurations"></a>
Optional list of credential provider configurations for authenticating with the MCP server. At most one credential provider configuration can be specified.  
Type: Array of [RegistryRecordCredentialProviderConfiguration](API_RegistryRecordCredentialProviderConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

## See Also
<a name="API_FromUrlSynchronizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/FromUrlSynchronizationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/FromUrlSynchronizationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/FromUrlSynchronizationConfiguration) 