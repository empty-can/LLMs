

# EvaluationTarget
<a name="API_EvaluationTarget"></a>

 The specification of which trace or span IDs to evaluate within the provided input data. Allows precise targeting of evaluation at different levels: tool calls, traces, or sessions. 

## Contents
<a name="API_EvaluationTarget_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** spanIds **   <a name="BedrockAgentCore-Type-EvaluationTarget-spanIds"></a>
 The list of specific span IDs to evaluate within the provided traces. Used to target evaluation at individual tool calls or specific operations within the agent's execution flow.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Fixed length of 16.  
Required: No

 ** traceIds **   <a name="BedrockAgentCore-Type-EvaluationTarget-traceIds"></a>
 The list of trace IDs to evaluate, representing complete request-response interactions. Used to evaluate entire conversation turns or specific agent interactions within a session.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Fixed length of 32.  
Required: No

## See Also
<a name="API_EvaluationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationTarget) 