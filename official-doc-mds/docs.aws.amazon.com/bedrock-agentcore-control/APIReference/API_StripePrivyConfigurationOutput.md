

# StripePrivyConfigurationOutput
<a name="API_StripePrivyConfigurationOutput"></a>

Stripe Privy configuration output with secret ARNs.

## Contents
<a name="API_StripePrivyConfigurationOutput_Contents"></a>

 ** appId **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-appId"></a>
The app ID provided by Privy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** appSecretArn **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-appSecretArn"></a>
Contains information about a secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object  
Required: Yes

 ** authorizationId **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-authorizationId"></a>
The authorization ID for the Stripe Privy integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** authorizationPrivateKeyArn **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-authorizationPrivateKeyArn"></a>
Contains information about a secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object  
Required: Yes

 ** appSecretJsonKey **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-appSecretJsonKey"></a>
The JSON key used to extract the app secret value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** appSecretSource **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-appSecretSource"></a>
The source type of the app secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** authorizationPrivateKeyJsonKey **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-authorizationPrivateKeyJsonKey"></a>
The JSON key used to extract the authorization private key value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** authorizationPrivateKeySource **   <a name="bedrockagentcorecontrol-Type-StripePrivyConfigurationOutput-authorizationPrivateKeySource"></a>
The source type of the authorization private key. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

## See Also
<a name="API_StripePrivyConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/StripePrivyConfigurationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/StripePrivyConfigurationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/StripePrivyConfigurationOutput) 