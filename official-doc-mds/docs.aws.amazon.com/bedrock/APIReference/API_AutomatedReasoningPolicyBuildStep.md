

# AutomatedReasoningPolicyBuildStep
<a name="API_AutomatedReasoningPolicyBuildStep"></a>

Represents a single step in the policy build process, containing context about what was being processed and any messages or results.

## Contents
<a name="API_AutomatedReasoningPolicyBuildStep_Contents"></a>

 ** context **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStep-context"></a>
Contextual information about what was being processed during this build step, such as the type of operation or the source material being analyzed.  
Type: [AutomatedReasoningPolicyBuildStepContext](API_AutomatedReasoningPolicyBuildStepContext.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** messages **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStep-messages"></a>
A list of messages generated during this build step, including informational messages, warnings, and error details.  
Type: Array of [AutomatedReasoningPolicyBuildStepMessage](API_AutomatedReasoningPolicyBuildStepMessage.md) objects  
Required: Yes

 ** priorElement **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStep-priorElement"></a>
Reference to the previous element or step in the build process, helping to trace the sequence of operations.  
Type: [AutomatedReasoningPolicyDefinitionElement](API_AutomatedReasoningPolicyDefinitionElement.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyBuildStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStep) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStep) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStep) 