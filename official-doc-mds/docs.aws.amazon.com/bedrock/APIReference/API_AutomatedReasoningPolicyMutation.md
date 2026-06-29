

# AutomatedReasoningPolicyMutation
<a name="API_AutomatedReasoningPolicyMutation"></a>

A container for various mutation operations that can be applied to an Automated Reasoning policy, including adding, updating, and deleting policy elements.

## Contents
<a name="API_AutomatedReasoningPolicyMutation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** addRule **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-addRule"></a>
A mutation to add a new rule to the policy.  
Type: [AutomatedReasoningPolicyAddRuleMutation](API_AutomatedReasoningPolicyAddRuleMutation.md) object  
Required: No

 ** addType **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-addType"></a>
A mutation to add a new custom type to the policy.  
Type: [AutomatedReasoningPolicyAddTypeMutation](API_AutomatedReasoningPolicyAddTypeMutation.md) object  
Required: No

 ** addVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-addVariable"></a>
A mutation to add a new variable to the policy.  
Type: [AutomatedReasoningPolicyAddVariableMutation](API_AutomatedReasoningPolicyAddVariableMutation.md) object  
Required: No

 ** deleteRule **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-deleteRule"></a>
A mutation to remove a rule from the policy.  
Type: [AutomatedReasoningPolicyDeleteRuleMutation](API_AutomatedReasoningPolicyDeleteRuleMutation.md) object  
Required: No

 ** deleteType **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-deleteType"></a>
A mutation to remove a custom type from the policy.  
Type: [AutomatedReasoningPolicyDeleteTypeMutation](API_AutomatedReasoningPolicyDeleteTypeMutation.md) object  
Required: No

 ** deleteVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-deleteVariable"></a>
A mutation to remove a variable from the policy.  
Type: [AutomatedReasoningPolicyDeleteVariableMutation](API_AutomatedReasoningPolicyDeleteVariableMutation.md) object  
Required: No

 ** updateRule **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-updateRule"></a>
A mutation to modify an existing rule in the policy.  
Type: [AutomatedReasoningPolicyUpdateRuleMutation](API_AutomatedReasoningPolicyUpdateRuleMutation.md) object  
Required: No

 ** updateType **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-updateType"></a>
A mutation to modify an existing custom type in the policy.  
Type: [AutomatedReasoningPolicyUpdateTypeMutation](API_AutomatedReasoningPolicyUpdateTypeMutation.md) object  
Required: No

 ** updateVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyMutation-updateVariable"></a>
A mutation to modify an existing variable in the policy.  
Type: [AutomatedReasoningPolicyUpdateVariableMutation](API_AutomatedReasoningPolicyUpdateVariableMutation.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyMutation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyMutation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyMutation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyMutation) 