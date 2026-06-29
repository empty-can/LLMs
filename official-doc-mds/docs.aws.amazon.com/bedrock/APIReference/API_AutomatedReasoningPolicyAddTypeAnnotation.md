

# AutomatedReasoningPolicyAddTypeAnnotation
<a name="API_AutomatedReasoningPolicyAddTypeAnnotation"></a>

An annotation for adding a new custom type to an Automated Reasoning policy, defining a set of possible values for variables.

## Contents
<a name="API_AutomatedReasoningPolicyAddTypeAnnotation_Contents"></a>

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicyAddTypeAnnotation-description"></a>
A description of what the custom type represents and how it should be used in the policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: Yes

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyAddTypeAnnotation-name"></a>
The name of the new custom type. This name will be used to reference the type in variable definitions and rules.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** values **   <a name="bedrock-Type-AutomatedReasoningPolicyAddTypeAnnotation-values"></a>
The list of possible values that variables of this type can take, each with its own description and identifier.  
Type: Array of [AutomatedReasoningPolicyDefinitionTypeValue](API_AutomatedReasoningPolicyDefinitionTypeValue.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 150 items.  
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyAddTypeAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAddTypeAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAddTypeAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAddTypeAnnotation) 