

# AutomatedReasoningPolicyDefinitionVariable
<a name="API_AutomatedReasoningPolicyDefinitionVariable"></a>

Represents a variable in an Automated Reasoning policy. Variables represent concepts that can have values assigned during natural language translation.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionVariable_Contents"></a>

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionVariable-description"></a>
The description of the variable that explains what it represents and how users might refer to it. Clear and comprehensive descriptions are essential for accurate natural language translation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: Yes

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionVariable-name"></a>
The name of the variable. Use descriptive names that clearly indicate the concept being represented.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** type **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionVariable-type"></a>
The data type of the variable. Valid types include bool, int, real, enum, and custom types that you can provide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionVariable) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionVariable) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionVariable) 