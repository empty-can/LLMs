

# CoinbaseCdpConfigurationOutput
<a name="API_CoinbaseCdpConfigurationOutput"></a>

Coinbase CDP configuration output with secret ARNs.

## Contents
<a name="API_CoinbaseCdpConfigurationOutput_Contents"></a>

 ** apiKeyId **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-apiKeyId"></a>
The API key identifier provided by Coinbase Developer Platform.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** apiKeySecretArn **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-apiKeySecretArn"></a>
Contains information about a secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object  
Required: Yes

 ** walletSecretArn **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-walletSecretArn"></a>
Contains information about a secret in AWS Secrets Manager.  
Type: [Secret](API_Secret.md) object  
Required: Yes

 ** apiKeySecretJsonKey **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-apiKeySecretJsonKey"></a>
The JSON key used to extract the API key secret value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** apiKeySecretSource **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-apiKeySecretSource"></a>
The source type of the API key secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** walletSecretJsonKey **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-walletSecretJsonKey"></a>
The JSON key used to extract the wallet secret value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** walletSecretSource **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationOutput-walletSecretSource"></a>
The source type of the wallet secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

## See Also
<a name="API_CoinbaseCdpConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CoinbaseCdpConfigurationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CoinbaseCdpConfigurationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CoinbaseCdpConfigurationOutput) 