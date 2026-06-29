

# GuardrailTraceAssessment
<a name="API_runtime_GuardrailTraceAssessment"></a>

A Top level guardrail trace object. For more information, see [ConverseTrace](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseTrace.html).

## Contents
<a name="API_runtime_GuardrailTraceAssessment_Contents"></a>

 ** actionReason **   <a name="bedrock-Type-runtime_GuardrailTraceAssessment-actionReason"></a>
Provides the reason for the action taken when harmful content is detected.  
Type: String  
Required: No

 ** inputAssessment **   <a name="bedrock-Type-runtime_GuardrailTraceAssessment-inputAssessment"></a>
The input assessment.  
Type: String to [GuardrailAssessment](API_runtime_GuardrailAssessment.md) object map  
Required: No

 ** modelOutput **   <a name="bedrock-Type-runtime_GuardrailTraceAssessment-modelOutput"></a>
The output from the model.  
Type: Array of strings  
Required: No

 ** outputAssessments **   <a name="bedrock-Type-runtime_GuardrailTraceAssessment-outputAssessments"></a>
the output assessments.  
Type: String to array of [GuardrailAssessment](API_runtime_GuardrailAssessment.md) objects map  
Required: No

## See Also
<a name="API_runtime_GuardrailTraceAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailTraceAssessment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailTraceAssessment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailTraceAssessment) 