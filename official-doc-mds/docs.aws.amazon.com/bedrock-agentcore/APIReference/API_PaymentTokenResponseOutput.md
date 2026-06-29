

# PaymentTokenResponseOutput
<a name="API_PaymentTokenResponseOutput"></a>

Vendor-specific token response configuration.

## Contents
<a name="API_PaymentTokenResponseOutput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCdpTokenResponse **   <a name="BedrockAgentCore-Type-PaymentTokenResponseOutput-coinbaseCdpTokenResponse"></a>
The Coinbase CDP token response.  
Type: [CoinbaseCdpTokenResponseOutput](API_CoinbaseCdpTokenResponseOutput.md) object  
Required: No

 ** stripePrivyTokenResponse **   <a name="BedrockAgentCore-Type-PaymentTokenResponseOutput-stripePrivyTokenResponse"></a>
The Stripe Privy token response.  
Type: [StripePrivyTokenResponseOutput](API_StripePrivyTokenResponseOutput.md) object  
Required: No

## See Also
<a name="API_PaymentTokenResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentTokenResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentTokenResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentTokenResponseOutput) 