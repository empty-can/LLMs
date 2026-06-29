

# SecretReference
<a name="API_SecretReference"></a>

Contains a reference to a secret stored in AWS Secrets Manager.

## Contents
<a name="API_SecretReference_Contents"></a>

 ** jsonKey **   <a name="bedrockagentcorecontrol-Type-SecretReference-jsonKey"></a>
The JSON key used to extract the secret value from the AWS Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** secretId **   <a name="bedrockagentcorecontrol-Type-SecretReference-secretId"></a>
The ID of the AWS Secrets Manager secret that stores the secret value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

## See Also
<a name="API_SecretReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SecretReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SecretReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SecretReference) 