

# AutomatedReasoningPolicyAnnotation
<a name="API_AutomatedReasoningPolicyAnnotation"></a>

Contains the various operations that can be performed on an Automated Reasoning policy, including adding, updating, and deleting rules, variables, and types.

## Contents
<a name="API_AutomatedReasoningPolicyAnnotation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** addRule **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-addRule"></a>
An operation to add a new logical rule to the policy using formal mathematical expressions.  
Type: [AutomatedReasoningPolicyAddRuleAnnotation](API_AutomatedReasoningPolicyAddRuleAnnotation.md) object  
Required: No

 ** addRuleFromNaturalLanguage **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-addRuleFromNaturalLanguage"></a>
An operation to add a new rule by converting natural language descriptions into formal logical expressions.  
Type: [AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation](API_AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation.md) object  
Required: No

 ** addType **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-addType"></a>
An operation to add a new custom type to the policy, defining a set of possible values for policy variables.  
Type: [AutomatedReasoningPolicyAddTypeAnnotation](API_AutomatedReasoningPolicyAddTypeAnnotation.md) object  
Required: No

 ** addVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-addVariable"></a>
An operation to add a new variable to the policy, which can be used in rule expressions to represent dynamic values.  
Type: [AutomatedReasoningPolicyAddVariableAnnotation](API_AutomatedReasoningPolicyAddVariableAnnotation.md) object  
Required: No

 ** deleteRule **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-deleteRule"></a>
An operation to remove a rule from the policy.  
Type: [AutomatedReasoningPolicyDeleteRuleAnnotation](API_AutomatedReasoningPolicyDeleteRuleAnnotation.md) object  
Required: No

 ** deleteType **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-deleteType"></a>
An operation to remove a custom type from the policy. The type must not be referenced by any variables or rules.  
Type: [AutomatedReasoningPolicyDeleteTypeAnnotation](API_AutomatedReasoningPolicyDeleteTypeAnnotation.md) object  
Required: No

 ** deleteVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-deleteVariable"></a>
An operation to remove a variable from the policy. The variable must not be referenced by any rules.  
Type: [AutomatedReasoningPolicyDeleteVariableAnnotation](API_AutomatedReasoningPolicyDeleteVariableAnnotation.md) object  
Required: No

 ** ingestContent **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-ingestContent"></a>
An operation to process and incorporate new content into the policy, extracting additional rules and concepts.  
Type: [AutomatedReasoningPolicyIngestContentAnnotation](API_AutomatedReasoningPolicyIngestContentAnnotation.md) object  
Required: No

 ** updateFromRulesFeedback **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-updateFromRulesFeedback"></a>
An operation to update the policy based on feedback about how specific rules performed during testing or validation.  
Type: [AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation](API_AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation.md) object  
Required: No

 ** updateFromScenarioFeedback **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-updateFromScenarioFeedback"></a>
An operation to update the policy based on feedback about how it performed on specific test scenarios.  
Type: [AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation](API_AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation.md) object  
Required: No

 ** updateRule **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-updateRule"></a>
An operation to modify an existing rule in the policy, such as changing its logical expression or conditions.  
Type: [AutomatedReasoningPolicyUpdateRuleAnnotation](API_AutomatedReasoningPolicyUpdateRuleAnnotation.md) object  
Required: No

 ** updateType **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-updateType"></a>
An operation to modify an existing custom type in the policy, such as changing its name, description, or allowed values.  
Type: [AutomatedReasoningPolicyUpdateTypeAnnotation](API_AutomatedReasoningPolicyUpdateTypeAnnotation.md) object  
Required: No

 ** updateVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotation-updateVariable"></a>
An operation to modify an existing variable in the policy, such as changing its name, type, or description.  
Type: [AutomatedReasoningPolicyUpdateVariableAnnotation](API_AutomatedReasoningPolicyUpdateVariableAnnotation.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAnnotation) 