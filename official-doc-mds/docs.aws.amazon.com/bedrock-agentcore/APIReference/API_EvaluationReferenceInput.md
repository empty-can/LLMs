

# EvaluationReferenceInput
<a name="API_EvaluationReferenceInput"></a>

 A reference input containing ground truth data for evaluation, scoped to a specific context level (session or trace) through its span context. 

## Contents
<a name="API_EvaluationReferenceInput_Contents"></a>

 ** context **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-context"></a>
 The span context that identifies which session or trace this reference input applies to, used for correlating ground truth with agent output.   
Type: [Context](API_Context.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** assertions **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-assertions"></a>
 A list of assertion statements for session-level evaluation. Each assertion describes an expected behavior or outcome the agent should demonstrate during the session.   
Type: Array of [EvaluationContent](API_EvaluationContent.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** expectedResponse **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-expectedResponse"></a>
 The expected response for trace-level evaluation. Built-in evaluators that support this field compare the agent's actual response against this value for assessment. Custom evaluators can access it through the `{expected_response}` placeholder in their instructions.   
Type: [EvaluationContent](API_EvaluationContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** expectedTrajectory **   <a name="BedrockAgentCore-Type-EvaluationReferenceInput-expectedTrajectory"></a>
 The expected tool call sequence for session-level trajectory evaluation. Contains a list of tool names representing the tools the agent is expected to invoke.   
Type: [EvaluationExpectedTrajectory](API_EvaluationExpectedTrajectory.md) object  
Required: No

## See Also
<a name="API_EvaluationReferenceInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationReferenceInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationReferenceInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationReferenceInput) 