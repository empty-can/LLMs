

# ApiKeyCredentialProviderItem
<a name="API_ApiKeyCredentialProviderItem"></a>

Contains information about an API key credential provider.

## Contents
<a name="API_ApiKeyCredentialProviderItem_Contents"></a>

 ** createdTime **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProviderItem-createdTime"></a>
The timestamp when the API key credential provider was created.  
Type: Timestamp  
Required: Yes

 ** credentialProviderArn **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProviderItem-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the API key credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** lastUpdatedTime **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProviderItem-lastUpdatedTime"></a>
The timestamp when the API key credential provider was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProviderItem-name"></a>
The name of the API key credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

## See Also
<a name="API_ApiKeyCredentialProviderItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ApiKeyCredentialProviderItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ApiKeyCredentialProviderItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ApiKeyCredentialProviderItem) 