

# CoinbaseCdpConfigurationInput
<a name="API_CoinbaseCdpConfigurationInput"></a>

Coinbase CDP configuration — credentials provided by Coinbase Developer Platform.

## Contents
<a name="API_CoinbaseCdpConfigurationInput_Contents"></a>

 ** apiKeyId **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-apiKeyId"></a>
The API key identifier provided by Coinbase Developer Platform.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[a-zA-Z0-9\-_]+`   
Required: Yes

 ** apiKeySecret **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-apiKeySecret"></a>
The API key secret provided by Coinbase Developer Platform.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9+/=\-_\s]*`   
Required: No

 ** apiKeySecretConfig **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-apiKeySecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the API key secret. This includes the secret ID and the JSON key used to extract the API key secret value from the secret. Required when `apiKeySecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** apiKeySecretSource **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-apiKeySecretSource"></a>
The source type of the API key secret for the Coinbase Developer Platform. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

 ** walletSecret **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-walletSecret"></a>
The wallet secret provided by Coinbase Developer Platform.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9+/=\-_\s]*`   
Required: No

 ** walletSecretConfig **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-walletSecretConfig"></a>
A reference to the AWS Secrets Manager secret that stores the wallet secret. This includes the secret ID and the JSON key used to extract the wallet secret value from the secret. Required when `walletSecretSource` is set to `EXTERNAL`.  
Type: [SecretReference](API_SecretReference.md) object  
Required: No

 ** walletSecretSource **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpConfigurationInput-walletSecretSource"></a>
The source type of the wallet secret for the Coinbase Developer Platform. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.  
Type: String  
Valid Values: `MANAGED | EXTERNAL`   
Required: No

## See Also
<a name="API_CoinbaseCdpConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CoinbaseCdpConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CoinbaseCdpConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CoinbaseCdpConfigurationInput) 