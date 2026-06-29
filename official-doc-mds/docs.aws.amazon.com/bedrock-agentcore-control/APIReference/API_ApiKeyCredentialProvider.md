

# ApiKeyCredentialProvider
<a name="API_ApiKeyCredentialProvider"></a>

An API key credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint using an API key.

## Contents
<a name="API_ApiKeyCredentialProvider_Contents"></a>

 ** providerArn **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProvider-providerArn"></a>
The Amazon Resource Name (ARN) of the API key credential provider. This ARN identifies the provider in AWS.  
Type: String  
Pattern: `arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)`   
Required: Yes

 ** credentialLocation **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProvider-credentialLocation"></a>
The location of the API key credential. This field specifies where in the request the API key should be placed.  
Type: String  
Valid Values: `HEADER | QUERY_PARAMETER`   
Required: No

 ** credentialParameterName **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProvider-credentialParameterName"></a>
The name of the credential parameter for the API key. This parameter name is used when sending the API key to the target endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** credentialPrefix **   <a name="bedrockagentcorecontrol-Type-ApiKeyCredentialProvider-credentialPrefix"></a>
The prefix for the API key credential. This prefix is added to the API key when sending it to the target endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

## See Also
<a name="API_ApiKeyCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ApiKeyCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ApiKeyCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ApiKeyCredentialProvider) 