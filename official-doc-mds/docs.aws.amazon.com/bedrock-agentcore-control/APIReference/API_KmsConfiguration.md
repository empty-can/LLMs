

# KmsConfiguration
<a name="API_KmsConfiguration"></a>

Contains the KMS configuration for a resource.

## Contents
<a name="API_KmsConfiguration_Contents"></a>

 ** keyType **   <a name="bedrockagentcorecontrol-Type-KmsConfiguration-keyType"></a>
The type of KMS key (CustomerManagedKey or ServiceManagedKey).  
Type: String  
Valid Values: `CustomerManagedKey | ServiceManagedKey`   
Required: Yes

 ** kmsKeyArn **   <a name="bedrockagentcorecontrol-Type-KmsConfiguration-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

## See Also
<a name="API_KmsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/KmsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/KmsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/KmsConfiguration) 