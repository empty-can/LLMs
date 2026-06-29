

# ConditionFlowNodeConfiguration
<a name="API_agent_ConditionFlowNodeConfiguration"></a>

Defines a condition node in your flow. You can specify conditions that determine which node comes next in the flow. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_ConditionFlowNodeConfiguration_Contents"></a>

 ** conditions **   <a name="bedrock-Type-agent_ConditionFlowNodeConfiguration-conditions"></a>
An array of conditions. Each member contains the name of a condition and an expression that defines the condition.  
Type: Array of [FlowCondition](API_agent_FlowCondition.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

## See Also
<a name="API_agent_ConditionFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ConditionFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ConditionFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ConditionFlowNodeConfiguration) 