

# PaymentCredentialProviderConfiguration
<a name="API_PaymentCredentialProviderConfiguration"></a>

Configuration for a payment credential provider that stores authentication credentials for a payment provider.

## Contents
<a name="API_PaymentCredentialProviderConfiguration_Contents"></a>

 ** credentialProviderArn **   <a name="bedrockagentcorecontrol-Type-PaymentCredentialProviderConfiguration-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the credential provider that stores the authentication credentials for the payment provider.  
Type: String  
Length Constraints: Minimum length of 69. Maximum length of 2048.  
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):(acps|bedrock-agentcore):[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/paymentcredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

## See Also
<a name="API_PaymentCredentialProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PaymentCredentialProviderConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PaymentCredentialProviderConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PaymentCredentialProviderConfiguration) 