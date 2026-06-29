

# PaymentCredentialProviderItem
<a name="API_PaymentCredentialProviderItem"></a>

Contains summary information about a payment credential provider.

## Contents
<a name="API_PaymentCredentialProviderItem_Contents"></a>

 ** createdTime **   <a name="bedrockagentcorecontrol-Type-PaymentCredentialProviderItem-createdTime"></a>
The timestamp when the payment credential provider was created.  
Type: Timestamp  
Required: Yes

 ** credentialProviderArn **   <a name="bedrockagentcorecontrol-Type-PaymentCredentialProviderItem-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the payment credential provider.  
Type: String  
Pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/paymentcredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** credentialProviderVendor **   <a name="bedrockagentcorecontrol-Type-PaymentCredentialProviderItem-credentialProviderVendor"></a>
The vendor type for the payment credential provider.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy`   
Required: Yes

 ** lastUpdatedTime **   <a name="bedrockagentcorecontrol-Type-PaymentCredentialProviderItem-lastUpdatedTime"></a>
The timestamp when the payment credential provider was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PaymentCredentialProviderItem-name"></a>
The name of the payment credential provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

## See Also
<a name="API_PaymentCredentialProviderItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PaymentCredentialProviderItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PaymentCredentialProviderItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PaymentCredentialProviderItem) 