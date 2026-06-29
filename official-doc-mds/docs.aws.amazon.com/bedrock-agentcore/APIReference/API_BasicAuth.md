

# BasicAuth
<a name="API_BasicAuth"></a>

Configuration for HTTP Basic Authentication using credentials stored in AWS Secrets Manager. The secret must contain a JSON object with `username` and `password` string fields. Username allows alphanumeric characters and `@._+=-` symbols (pattern: `^[a-zA-Z0-9@._+=\-]+$`). Password allows alphanumeric characters and `@._+=-!#$%&*` symbols (pattern: `^[a-zA-Z0-9@._+=\-!#$%&*]+$`). Both fields have a maximum length of 256 characters.

## Contents
<a name="API_BasicAuth_Contents"></a>

 ** secretArn **   <a name="BedrockAgentCore-Type-BasicAuth-secretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing proxy credentials. The secret must be a JSON object with `username` and `password` string fields that meet validation requirements. The caller must have `secretsmanager:GetSecretValue` permission for this ARN. Example secret format: `{"username": "proxy_user", "password": "secure_password"}`   
Type: String  
Pattern: `arn:aws(-[a-z-]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`   
Required: Yes

## See Also
<a name="API_BasicAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BasicAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BasicAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BasicAuth) 