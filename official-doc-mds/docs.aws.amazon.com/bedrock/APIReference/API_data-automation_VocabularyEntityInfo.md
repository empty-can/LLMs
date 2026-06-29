

# VocabularyEntityInfo
<a name="API_data-automation_VocabularyEntityInfo"></a>

Information about a vocabulary entity.

## Contents
<a name="API_data-automation_VocabularyEntityInfo_Contents"></a>

 ** language **   <a name="bedrock-Type-data-automation_VocabularyEntityInfo-language"></a>
The entity language.  
Type: String  
Valid Values: `EN | DE | ES | FR | IT | PT | JA | KO | CN | TW | HK`   
Required: Yes

 ** phrases **   <a name="bedrock-Type-data-automation_VocabularyEntityInfo-phrases"></a>
The entity phrases.  
Type: Array of [Phrase](API_data-automation_Phrase.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

 ** description **   <a name="bedrock-Type-data-automation_VocabularyEntityInfo-description"></a>
The entity description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Pattern: `[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*`   
Required: No

 ** entityId **   <a name="bedrock-Type-data-automation_VocabularyEntityInfo-entityId"></a>
The entity ID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: No

## See Also
<a name="API_data-automation_VocabularyEntityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/VocabularyEntityInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/VocabularyEntityInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/VocabularyEntityInfo) 