

# GuardrailTrace
<a name="API_agent-runtime_GuardrailTrace"></a>

The trace details used in the Guardrail.

## Contents
<a name="API_agent-runtime_GuardrailTrace_Contents"></a>

 ** action **   <a name="bedrock-Type-agent-runtime_GuardrailTrace-action"></a>
The trace action details used with the Guardrail.  
Type: String  
Valid Values: `INTERVENED | NONE`   
Required: No

 ** inputAssessments **   <a name="bedrock-Type-agent-runtime_GuardrailTrace-inputAssessments"></a>
The details of the input assessments used in the Guardrail Trace.  
Type: Array of [GuardrailAssessment](API_agent-runtime_GuardrailAssessment.md) objects  
Required: No

 ** metadata **   <a name="bedrock-Type-agent-runtime_GuardrailTrace-metadata"></a>
Contains information about the Guardrail output.  
Type: [Metadata](API_agent-runtime_Metadata.md) object  
Required: No

 ** outputAssessments **   <a name="bedrock-Type-agent-runtime_GuardrailTrace-outputAssessments"></a>
The details of the output assessments used in the Guardrail Trace.  
Type: Array of [GuardrailAssessment](API_agent-runtime_GuardrailAssessment.md) objects  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_GuardrailTrace-traceId"></a>
The details of the trace Id used in the Guardrail Trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

## See Also
<a name="API_agent-runtime_GuardrailTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GuardrailTrace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GuardrailTrace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GuardrailTrace) 