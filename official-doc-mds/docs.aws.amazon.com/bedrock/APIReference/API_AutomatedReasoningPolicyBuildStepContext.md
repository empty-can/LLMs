

# AutomatedReasoningPolicyBuildStepContext
<a name="API_AutomatedReasoningPolicyBuildStepContext"></a>

Provides context about what type of operation was being performed during a build step.

## Contents
<a name="API_AutomatedReasoningPolicyBuildStepContext_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** mutation **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStepContext-mutation"></a>
Indicates that this build step involved modifying the policy structure, such as adding or updating rules, variables, or types.  
Type: [AutomatedReasoningPolicyMutation](API_AutomatedReasoningPolicyMutation.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** planning **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStepContext-planning"></a>
Indicates that this build step was part of the planning phase, where the system determines what operations to perform.  
Type: [AutomatedReasoningPolicyPlanning](API_AutomatedReasoningPolicyPlanning.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyBuildStepContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStepContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStepContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStepContext) 