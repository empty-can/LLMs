

# CoinbaseCdpTokenRequestInput
<a name="API_CoinbaseCdpTokenRequestInput"></a>

Coinbase CDP token request parameters.

## Contents
<a name="API_CoinbaseCdpTokenRequestInput_Contents"></a>

 ** requestMethod **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestMethod"></a>
The HTTP method for the payment API request.  
Type: String  
Valid Values: `GET | POST | PUT | DELETE | PATCH`   
Required: Yes

 ** requestPath **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestPath"></a>
The path of the payment API request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `/[a-zA-Z0-9/_\-\.~%?=&]+`   
Required: Yes

 ** includeWalletAuthToken **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-includeWalletAuthToken"></a>
Set to true for wallet write operations (requires walletSecret configured).  
Type: Boolean  
Required: No

 ** requestBody **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestBody"></a>
Request body JSON — used to generate wallet auth JWT.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16384.  
Pattern: `[\u0009\u000A\u000D\u0020-\u007E]+`   
Required: No

 ** requestHost **   <a name="BedrockAgentCore-Type-CoinbaseCdpTokenRequestInput-requestHost"></a>
The host for the payment API request. Defaults to "api.cdp.coinbase.com".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9\-\.]+`   
Required: No

## See Also
<a name="API_CoinbaseCdpTokenRequestInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenRequestInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenRequestInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CoinbaseCdpTokenRequestInput) 