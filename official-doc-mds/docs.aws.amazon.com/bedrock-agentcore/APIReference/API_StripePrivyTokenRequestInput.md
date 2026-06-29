

# StripePrivyTokenRequestInput
<a name="API_StripePrivyTokenRequestInput"></a>

Stripe Privy token request parameters.

## Contents
<a name="API_StripePrivyTokenRequestInput_Contents"></a>

 ** requestBody **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-requestBody"></a>
Request body JSON for the Privy API call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16384.  
Pattern: `[\u0009\u000A\u000D\u0020-\u007E]+`   
Required: Yes

 ** requestPath **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-requestPath"></a>
The path of the Stripe Privy API request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `/[a-zA-Z0-9/_\-\.~%?=&]+`   
Required: Yes

 ** includeAuthorizationSignature **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-includeAuthorizationSignature"></a>
Set to true to generate privy-authorization-signature.  
Type: Boolean  
Required: No

 ** requestHost **   <a name="BedrockAgentCore-Type-StripePrivyTokenRequestInput-requestHost"></a>
The host for the Privy API request. Defaults to "api.privy.io".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\-\.]+`   
Required: No

## See Also
<a name="API_StripePrivyTokenRequestInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StripePrivyTokenRequestInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StripePrivyTokenRequestInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StripePrivyTokenRequestInput) 