

# StripePrivyTokenResponseOutput
<a name="API_StripePrivyTokenResponseOutput"></a>

Stripe Privy token response containing appId, basicAuthToken, and optionally authorizationSignature.

## Contents
<a name="API_StripePrivyTokenResponseOutput_Contents"></a>

 ** appId **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-appId"></a>
The Privy app ID for the privy-app-id header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** basicAuthToken **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-basicAuthToken"></a>
Base64-encoded Basic Auth token (appId:appSecret) for the Authorization header.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: Yes

 ** authorizationSignature **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-authorizationSignature"></a>
Base64-encoded ECDSA P-256 authorization signature (only present when includeAuthorizationSignature is true).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: No

 ** requestExpiry **   <a name="BedrockAgentCore-Type-StripePrivyTokenResponseOutput-requestExpiry"></a>
Unix timestamp in milliseconds when the authorization signature expires.  
Type: Long  
Required: No

## See Also
<a name="API_StripePrivyTokenResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StripePrivyTokenResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StripePrivyTokenResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StripePrivyTokenResponseOutput) 