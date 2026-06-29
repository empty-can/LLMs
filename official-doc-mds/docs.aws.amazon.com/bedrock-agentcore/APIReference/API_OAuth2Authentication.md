

# OAuth2Authentication
<a name="API_OAuth2Authentication"></a>

OAuth2 authentication information for third-party providers.

## Contents
<a name="API_OAuth2Authentication_Contents"></a>

 ** sub **   <a name="BedrockAgentCore-Type-OAuth2Authentication-sub"></a>
The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** emailAddress **   <a name="BedrockAgentCore-Type-OAuth2Authentication-emailAddress"></a>
The email address from the OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 254.  
Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`   
Required: No

 ** name **   <a name="BedrockAgentCore-Type-OAuth2Authentication-name"></a>
The user's name from the OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** username **   <a name="BedrockAgentCore-Type-OAuth2Authentication-username"></a>
The username from the OAuth2 provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_OAuth2Authentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OAuth2Authentication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OAuth2Authentication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OAuth2Authentication) 