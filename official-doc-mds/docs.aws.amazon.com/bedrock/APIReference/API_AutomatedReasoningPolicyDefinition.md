

# AutomatedReasoningPolicyDefinition
<a name="API_AutomatedReasoningPolicyDefinition"></a>

Contains the formal logic rules, variables, and custom variable types that define an Automated Reasoning policy. The policy definition specifies the constraints used to validate foundation model responses for accuracy and logical consistency.

## Contents
<a name="API_AutomatedReasoningPolicyDefinition_Contents"></a>

 ** rules **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinition-rules"></a>
The formal logic rules extracted from the source document. Rules define the logical constraints that determine whether model responses are valid, invalid, or satisfiable.  
Type: Array of [AutomatedReasoningPolicyDefinitionRule](API_AutomatedReasoningPolicyDefinitionRule.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1500 items.  
Required: No

 ** types **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinition-types"></a>
The custom user-defined vairable types used in the policy. Types are enum-based variable types that provide additional context beyond the predefined variable types.  
Type: Array of [AutomatedReasoningPolicyDefinitionType](API_AutomatedReasoningPolicyDefinitionType.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 150 items.  
Required: No

 ** variables **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinition-variables"></a>
The variables that represent concepts in the policy. Variables can have values assigned when translating natural language into formal logic. Their descriptions are crucial for accurate translation.  
Type: Array of [AutomatedReasoningPolicyDefinitionVariable](API_AutomatedReasoningPolicyDefinitionVariable.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 600 items.  
Required: No

 ** version **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinition-version"></a>
The version of the policy definition format.  
Type: String  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinition) 