

# VocabularyEntity
<a name="API_data-automation_VocabularyEntity"></a>

A vocabulary entity.

## Contents
<a name="API_data-automation_VocabularyEntity_Contents"></a>

 ** description **   <a name="bedrock-Type-data-automation_VocabularyEntity-description"></a>
The entity description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Pattern: `[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*`   
Required: No

 ** entityId **   <a name="bedrock-Type-data-automation_VocabularyEntity-entityId"></a>
The entity ID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: No

 ** language **   <a name="bedrock-Type-data-automation_VocabularyEntity-language"></a>
The entity language.  
Type: String  
Valid Values: `EN | DE | ES | FR | IT | PT | JA | KO | CN | TW | HK`   
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-data-automation_VocabularyEntity-lastModifiedTime"></a>
When the entity was last modified.  
Type: Timestamp  
Required: No

 ** phrases **   <a name="bedrock-Type-data-automation_VocabularyEntity-phrases"></a>
The entity phrases.  
Type: Array of [Phrase](API_data-automation_Phrase.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## See Also
<a name="API_data-automation_VocabularyEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/VocabularyEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/VocabularyEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/VocabularyEntity) 