

# AutomatedReasoningPolicyDefinitionType
<a name="API_AutomatedReasoningPolicyDefinitionType"></a>

Represents a custom user-defined viarble type in an Automated Reasoning policy. Types are enum-based and provide additional context beyond predefined variable types.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionType_Contents"></a>

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionType-name"></a>
The name of the custom type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** values **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionType-values"></a>
The possible values for this enum-based type, each with its own description.  
Type: Array of [AutomatedReasoningPolicyDefinitionTypeValue](API_AutomatedReasoningPolicyDefinitionTypeValue.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 150 items.  
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionType-description"></a>
The description of what the custom type represents.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionType) 