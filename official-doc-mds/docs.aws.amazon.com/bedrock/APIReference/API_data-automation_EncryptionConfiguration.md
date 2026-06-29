

# EncryptionConfiguration
<a name="API_data-automation_EncryptionConfiguration"></a>

Encryption settings for a project.

## Contents
<a name="API_data-automation_EncryptionConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="bedrock-Type-data-automation_EncryptionConfiguration-kmsKeyId"></a>
The AWS KMS key to use for encryption.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`   
Required: Yes

 ** kmsEncryptionContext **   <a name="bedrock-Type-data-automation_EncryptionConfiguration-kmsEncryptionContext"></a>
The AWS KMS encryption context to use for encryption.  
Type: String to string map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

## See Also
<a name="API_data-automation_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/EncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/EncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/EncryptionConfiguration) 