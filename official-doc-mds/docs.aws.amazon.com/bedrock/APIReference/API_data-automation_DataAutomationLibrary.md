

# DataAutomationLibrary
<a name="API_data-automation_DataAutomationLibrary"></a>

A data automation library.

## Contents
<a name="API_data-automation_DataAutomationLibrary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-creationTime"></a>
When the library was created.  
Type: Timestamp  
Required: Yes

 ** libraryArn **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-libraryArn"></a>
The library's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** libraryName **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-libraryName"></a>
The library's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** status **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-status"></a>
The library's status.  
Type: String  
Valid Values: `ACTIVE | DELETING`   
Required: Yes

 ** entityTypes **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-entityTypes"></a>
The entity types supported by the library.  
Type: Array of [EntityTypeInfo](API_data-automation_EntityTypeInfo.md) objects  
Required: No

 ** kmsEncryptionContext **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-kmsEncryptionContext"></a>
The AWS KMS encryption context to use for encryption.  
Type: String to string map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

 ** kmsKeyId **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-kmsKeyId"></a>
The AWS KMS key to use for encryption.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`   
Required: No

 ** libraryDescription **   <a name="bedrock-Type-data-automation_DataAutomationLibrary-libraryDescription"></a>
The library's description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Pattern: `[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*`   
Required: No

## See Also
<a name="API_data-automation_DataAutomationLibrary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DataAutomationLibrary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DataAutomationLibrary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DataAutomationLibrary) 