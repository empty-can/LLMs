

# TokenBalance
<a name="API_TokenBalance"></a>

A single token balance entry.

## Contents
<a name="API_TokenBalance_Contents"></a>

 ** amount **   <a name="BedrockAgentCore-Type-TokenBalance-amount"></a>
Raw balance in the smallest denomination (e.g., USDC base units where 1 USDC = 1000000).  
Type: String  
Required: Yes

 ** chain **   <a name="BedrockAgentCore-Type-TokenBalance-chain"></a>
The specific blockchain chain.  
Type: String  
Valid Values: `BASE | BASE_SEPOLIA | ETHEREUM | SOLANA | SOLANA_DEVNET`   
Required: Yes

 ** decimals **   <a name="BedrockAgentCore-Type-TokenBalance-decimals"></a>
Number of decimal places for the token (e.g., 6 for USDC).  
Type: Integer  
Required: Yes

 ** network **   <a name="BedrockAgentCore-Type-TokenBalance-network"></a>
The blockchain network family (ETHEREUM or SOLANA).  
Type: String  
Valid Values: `ETHEREUM | SOLANA`   
Required: Yes

 ** token **   <a name="BedrockAgentCore-Type-TokenBalance-token"></a>
The supported token for this balance.  
Type: String  
Valid Values: `USDC`   
Required: Yes

## See Also
<a name="API_TokenBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/TokenBalance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/TokenBalance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/TokenBalance) 