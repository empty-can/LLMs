

# LinkedAccountOAuth2
<a name="API_LinkedAccountOAuth2"></a>

Authentication method using OAuth2 providers. Supports Google, Apple, X, Telegram, and GitHub providers.

## Contents
<a name="API_LinkedAccountOAuth2_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apple **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-apple"></a>
Apple OAuth2 authentication.  
Type: [OAuth2Authentication](API_OAuth2Authentication.md) object  
Required: No

 ** github **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-github"></a>
GitHub OAuth2 authentication.  
Type: [OAuth2Authentication](API_OAuth2Authentication.md) object  
Required: No

 ** google **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-google"></a>
Google OAuth2 authentication.  
Type: [OAuth2Authentication](API_OAuth2Authentication.md) object  
Required: No

 ** telegram **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-telegram"></a>
Telegram OAuth2 authentication.  
Type: [OAuth2Authentication](API_OAuth2Authentication.md) object  
Required: No

 ** x **   <a name="BedrockAgentCore-Type-LinkedAccountOAuth2-x"></a>
X (formerly Twitter) OAuth2 authentication.  
Type: [OAuth2Authentication](API_OAuth2Authentication.md) object  
Required: No

## See Also
<a name="API_LinkedAccountOAuth2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccountOAuth2) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccountOAuth2) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccountOAuth2) 