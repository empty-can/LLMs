

# StripePrivyConfigurationInput
<a name="API_StripePrivyConfigurationInput"></a>

Stripe Privy configuration — credentials provided by Stripe and Privy.

## Contents
<a name="API_StripePrivyConfigurationInput_Contents"></a>

 ** appId **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-appId"></a>
The app ID provided by Privy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** authorizationId **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-authorizationId"></a>
The authorization ID for the Stripe Privy integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** appSecret **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-appSecret"></a>
The app secret provided by Privy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9+/=\-_\s]*`   
Required: No

 ** appSecretConfig **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-appSecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the app secret. This includes the secret ID and the JSON key used to extract the app secret value from the secret. Required when `appSecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** appSecretSource **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-appSecretSource"></a>
The source type of the app secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** authorizationPrivateKey **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-authorizationPrivateKey"></a>
The authorization private key for the Stripe Privy integration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(wallet-auth:)?[a-zA-Z0-9+/=\-_\s]*`   
Required: No

 ** authorizationPrivateKeyConfig **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-authorizationPrivateKeyConfig"></a>
A reference to the AWS Secrets Manager secret that stores the authorization private key. This includes the secret ID and the JSON key used to extract the authorization private key value from the secret. Required when `authorizationPrivateKeySource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** authorizationPrivateKeySource **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationInput-authorizationPrivateKeySource"></a>
The source type of the authorization private key. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

## See Also
<a name="API_StripePrivyConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/StripePrivyConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/StripePrivyConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/StripePrivyConfigurationInput) 