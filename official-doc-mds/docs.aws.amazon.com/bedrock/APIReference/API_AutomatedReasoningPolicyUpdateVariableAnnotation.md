

# AutomatedReasoningPolicyUpdateVariableAnnotation
<a name="API_AutomatedReasoningPolicyUpdateVariableAnnotation"></a>

An annotation for modifying an existing variable in an Automated Reasoning policy.

## Contents
<a name="API_AutomatedReasoningPolicyUpdateVariableAnnotation_Contents"></a>

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateVariableAnnotation-name"></a>
The current name of the variable to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateVariableAnnotation-description"></a>
The new description for the variable, replacing the previous description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

 ** newName **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateVariableAnnotation-newName"></a>
The new name for the variable, if you want to rename it. If not provided, the name remains unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyUpdateVariableAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateVariableAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateVariableAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateVariableAnnotation) 