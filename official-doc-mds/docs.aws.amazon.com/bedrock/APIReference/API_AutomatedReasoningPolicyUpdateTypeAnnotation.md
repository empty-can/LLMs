

# AutomatedReasoningPolicyUpdateTypeAnnotation
<a name="API_AutomatedReasoningPolicyUpdateTypeAnnotation"></a>

An annotation for modifying an existing custom type in an Automated Reasoning policy.

## Contents
<a name="API_AutomatedReasoningPolicyUpdateTypeAnnotation_Contents"></a>

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeAnnotation-name"></a>
The current name of the custom type to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** values **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeAnnotation-values"></a>
The updated list of values for the custom type, which can include additions, modifications, or removals.  
Type: Array of [AutomatedReasoningPolicyTypeValueAnnotation](API_AutomatedReasoningPolicyTypeValueAnnotation.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeAnnotation-description"></a>
The new description for the custom type, replacing the previous description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

 ** newName **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateTypeAnnotation-newName"></a>
The new name for the custom type, if you want to rename it. If not provided, the name remains unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyUpdateTypeAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateTypeAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateTypeAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateTypeAnnotation) 