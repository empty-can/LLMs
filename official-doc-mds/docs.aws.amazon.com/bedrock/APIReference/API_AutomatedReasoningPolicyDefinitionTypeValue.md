

# AutomatedReasoningPolicyDefinitionTypeValue
<a name="API_AutomatedReasoningPolicyDefinitionTypeValue"></a>

Represents a single value within a custom type definition, including its identifier and description.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionTypeValue_Contents"></a>

 ** value **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionTypeValue-value"></a>
The actual value or identifier for this type value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionTypeValue-description"></a>
A human-readable description explaining what this type value represents and when it should be used.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionTypeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionTypeValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionTypeValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionTypeValue) 