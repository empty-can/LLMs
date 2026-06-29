

# PaymentTokenRequestInput
<a name="API_PaymentTokenRequestInput"></a>

Vendor-specific token request configuration.

## Contents
<a name="API_PaymentTokenRequestInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCdpTokenRequest **   <a name="BedrockAgentCore-Type-PaymentTokenRequestInput-coinbaseCdpTokenRequest"></a>
The Coinbase CDP token request.  
Type: [CoinbaseCdpTokenRequestInput](API_CoinbaseCdpTokenRequestInput.md) object  
Required: No

 ** stripePrivyTokenRequest **   <a name="BedrockAgentCore-Type-PaymentTokenRequestInput-stripePrivyTokenRequest"></a>
The Stripe Privy token request.  
Type: [StripePrivyTokenRequestInput](API_StripePrivyTokenRequestInput.md) object  
Required: No

## See Also
<a name="API_PaymentTokenRequestInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentTokenRequestInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentTokenRequestInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentTokenRequestInput) 