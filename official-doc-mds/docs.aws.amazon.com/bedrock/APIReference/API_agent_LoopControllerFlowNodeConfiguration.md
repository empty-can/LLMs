

# LoopControllerFlowNodeConfiguration
<a name="API_agent_LoopControllerFlowNodeConfiguration"></a>

Contains configurations for the controller node of a DoWhile loop in the flow.

## Contents
<a name="API_agent_LoopControllerFlowNodeConfiguration_Contents"></a>

 ** continueCondition **   <a name="bedrock-Type-agent_LoopControllerFlowNodeConfiguration-continueCondition"></a>
Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.  
Type: [FlowCondition](API_agent_FlowCondition.md) object  
Required: Yes

 ** maxIterations **   <a name="bedrock-Type-agent_LoopControllerFlowNodeConfiguration-maxIterations"></a>
Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

## See Also
<a name="API_agent_LoopControllerFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/LoopControllerFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/LoopControllerFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/LoopControllerFlowNodeConfiguration) 