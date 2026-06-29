

# AutomatedReasoningPolicyAddVariableAnnotation
<a name="API_AutomatedReasoningPolicyAddVariableAnnotation"></a>

An annotation for adding a new variable to an Automated Reasoning policy, which can be used in rule expressions.

## Contents
<a name="API_AutomatedReasoningPolicyAddVariableAnnotation_Contents"></a>

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyAddVariableAnnotation-description"></a>
A description of what the variable represents and how it should be used in rules.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: Yes

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyAddVariableAnnotation-name"></a>
The name of the new variable. This name will be used to reference the variable in rule expressions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** type **   <a name="bedrock-Type-AutomatedReasoningPolicyAddVariableAnnotation-type"></a>
The type of the variable, which can be a built-in type (like string or number) or a custom type defined in the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyAddVariableAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAddVariableAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAddVariableAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAddVariableAnnotation) 