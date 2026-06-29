

# AutomatedReasoningPolicyAddTypeValue
<a name="API_AutomatedReasoningPolicyAddTypeValue"></a>

Represents a single value that can be added to an existing custom type in the policy.

## Contents
<a name="API_AutomatedReasoningPolicyAddTypeValue_Contents"></a>

 ** value **   <a name="bedrock-Type-AutomatedReasoningPolicyAddTypeValue-value"></a>
The identifier or name of the new value to add to the type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyAddTypeValue-description"></a>
A description of what this new type value represents and when it should be used.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyAddTypeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAddTypeValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAddTypeValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAddTypeValue) 