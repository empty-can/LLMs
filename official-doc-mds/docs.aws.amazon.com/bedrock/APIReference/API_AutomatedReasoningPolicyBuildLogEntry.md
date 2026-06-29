

# AutomatedReasoningPolicyBuildLogEntry
<a name="API_AutomatedReasoningPolicyBuildLogEntry"></a>

Represents a single entry in the policy build log, containing information about a specific step or event in the build process.

## Contents
<a name="API_AutomatedReasoningPolicyBuildLogEntry_Contents"></a>

 ** annotation **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildLogEntry-annotation"></a>
The annotation or operation that was being processed when this log entry was created.  
Type: [AutomatedReasoningPolicyAnnotation](API_AutomatedReasoningPolicyAnnotation.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** buildSteps **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildLogEntry-buildSteps"></a>
Detailed information about the specific build steps that were executed, including any sub-operations or transformations.  
Type: Array of [AutomatedReasoningPolicyBuildStep](API_AutomatedReasoningPolicyBuildStep.md) objects  
Required: Yes

 ** status **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildLogEntry-status"></a>
The status of the build step (e.g., SUCCESS, FAILED, IN\_PROGRESS).  
Type: String  
Valid Values: `APPLIED | FAILED`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyBuildLogEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildLogEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildLogEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildLogEntry) 