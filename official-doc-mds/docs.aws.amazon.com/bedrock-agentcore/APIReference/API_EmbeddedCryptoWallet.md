

# EmbeddedCryptoWallet
<a name="API_EmbeddedCryptoWallet"></a>

Embedded crypto wallet instrument details.

## Contents
<a name="API_EmbeddedCryptoWallet_Contents"></a>

 ** linkedAccounts **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-linkedAccounts"></a>
List of linked accounts linked to this wallet. Each represents a way the end user can authenticate to this wallet.  
Type: Array of [LinkedAccount](API_LinkedAccount.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: Yes

 ** network **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-network"></a>
The blockchain network for this embedded crypto wallet. Supported networks: ETHEREUM, SOLANA.  
Type: String  
Valid Values: `ETHEREUM | SOLANA`   
Required: Yes

 ** redirectUrl **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-redirectUrl"></a>
URL for the end user to complete a provider-specific action such as wallet linking or onboarding.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** walletAddress **   <a name="BedrockAgentCore-Type-EmbeddedCryptoWallet-walletAddress"></a>
The wallet address on the specified blockchain network.  
Type: String  
Required: No

## See Also
<a name="API_EmbeddedCryptoWallet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EmbeddedCryptoWallet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EmbeddedCryptoWallet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EmbeddedCryptoWallet) 