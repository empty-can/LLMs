

# AutomatedReasoningPolicyUpdateTypeValue
<a name="API_AutomatedReasoningPolicyUpdateTypeValue"></a>

Represents a modification to a value within an existing custom type.

## Contents
<a name="API_AutomatedReasoningPolicyUpdateTypeValue_Contents"></a>

 ** value **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeValue-value"></a>
The current identifier or name of the type value to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeValue-description"></a>
The new description for the type value, replacing the previous description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

 ** newValue **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeValue-newValue"></a>
The new identifier or name for the type value, if you want to rename it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyUpdateTypeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateTypeValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateTypeValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateTypeValue) 