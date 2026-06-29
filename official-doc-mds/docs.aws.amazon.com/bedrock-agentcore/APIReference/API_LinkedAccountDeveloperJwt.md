

# LinkedAccountDeveloperJwt
<a name="API_LinkedAccountDeveloperJwt"></a>

Authentication method using JWT with key ID and subject claims.

## Contents
<a name="API_LinkedAccountDeveloperJwt_Contents"></a>

 ** kid **   <a name="BedrockAgentCore-Type-LinkedAccountDeveloperJwt-kid"></a>
The key ID (kid) from the JWT header. Identifies which key was used to sign the JWT.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9_-]{1,255}`   
Required: Yes

 ** sub **   <a name="BedrockAgentCore-Type-LinkedAccountDeveloperJwt-sub"></a>
The subject (sub) claim from the JWT payload. Identifies the principal that is the subject of the JWT.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_LinkedAccountDeveloperJwt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccountDeveloperJwt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccountDeveloperJwt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccountDeveloperJwt) 