

# PaymentProviderConfigurationOutput
<a name="API_PaymentProviderConfigurationOutput"></a>

Provider configuration output — no raw secrets, only ARNs. Varies by vendor type.

## Contents
<a name="API_PaymentProviderConfigurationOutput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCdpConfiguration **   <a name="bedrockagentcorecontrol-Type-PaymentProviderConfigurationOutput-coinbaseCdpConfiguration"></a>
The Coinbase CDP configuration.  
Type: [CoinbaseCdpConfigurationOutput](API_CoinbaseCdpConfigurationOutput.md) object  
Required: No

 ** stripePrivyConfiguration **   <a name="bedrockagentcorecontrol-Type-PaymentProviderConfigurationOutput-stripePrivyConfiguration"></a>
The Stripe Privy configuration.  
Type: [StripePrivyConfigurationOutput](API_StripePrivyConfigurationOutput.md) object  
Required: No

## See Also
<a name="API_PaymentProviderConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PaymentProviderConfigurationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PaymentProviderConfigurationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PaymentProviderConfigurationOutput) 