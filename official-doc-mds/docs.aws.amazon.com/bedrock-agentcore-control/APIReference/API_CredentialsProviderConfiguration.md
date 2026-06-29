

# CredentialsProviderConfiguration
<a name="API_CredentialsProviderConfiguration"></a>

The credential provider configuration for a payment connector. Specifies the payment provider type and its associated credential provider.

## Contents
<a name="API_CredentialsProviderConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCDP **   <a name="bedrockagentcorecontrol-Type-CredentialsProviderConfiguration-coinbaseCDP"></a>
The credential provider configuration for a Coinbase CDP payment connector.  
Type: [PaymentCredentialProviderConfiguration](API_PaymentCredentialProviderConfiguration.md) object  
Required: No

 ** stripePrivy **   <a name="bedrockagentcorecontrol-Type-CredentialsProviderConfiguration-stripePrivy"></a>
The credential provider configuration for a Stripe Privy payment connector.  
Type: [PaymentCredentialProviderConfiguration](API_PaymentCredentialProviderConfiguration.md) object  
Required: No

## See Also
<a name="API_CredentialsProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CredentialsProviderConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CredentialsProviderConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CredentialsProviderConfiguration) 