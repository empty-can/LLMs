

# OAuth2AuthorizationData
<a name="API_OAuth2AuthorizationData"></a>

OAuth2-specific authorization data, including the authorization URL and user identifier for the authorization session.

## Contents
<a name="API_OAuth2AuthorizationData_Contents"></a>

 ** authorizationUrl **   <a name="bedrockagentcorecontrol-Type-OAuth2AuthorizationData-authorizationUrl"></a>
The URL to initiate the authorization process. This URL is provided when the OAuth2 access token requires user authorization.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** userId **   <a name="bedrockagentcorecontrol-Type-OAuth2AuthorizationData-userId"></a>
The user identifier associated with the OAuth2 authorization session that is defined by AgentCore Gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

## See Also
<a name="API_OAuth2AuthorizationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OAuth2AuthorizationData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OAuth2AuthorizationData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OAuth2AuthorizationData) 