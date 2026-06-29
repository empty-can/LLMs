

# EncryptionConfiguration
<a name="API_data-automation-runtime_EncryptionConfiguration"></a>

Encryption settings for an invocation.

## Contents
<a name="API_data-automation-runtime_EncryptionConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="bedrock-Type-data-automation-runtime_EncryptionConfiguration-kmsKeyId"></a>
A KMS key ID to use for encryption.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`   
Required: Yes

 ** kmsEncryptionContext **   <a name="bedrock-Type-data-automation-runtime_EncryptionConfiguration-kmsEncryptionContext"></a>
Name-value pairs to include as an encryption context.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

## See Also
<a name="API_data-automation-runtime_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/EncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/EncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/EncryptionConfiguration) 