

# ConditionResultEvent
<a name="API_agent-runtime_ConditionResultEvent"></a>

Contains information about a condition evaluation result during a flow execution. This event is generated when a condition node in the flow evaluates its conditions.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_ConditionResultEvent_Contents"></a>

 ** nodeName **   <a name="bedrock-Type-agent-runtime_ConditionResultEvent-nodeName"></a>
The name of the condition node that evaluated the conditions.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** satisfiedConditions **   <a name="bedrock-Type-agent-runtime_ConditionResultEvent-satisfiedConditions"></a>
A list of conditions that were satisfied during the evaluation.  
Type: Array of [SatisfiedCondition](API_agent-runtime_SatisfiedCondition.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** timestamp **   <a name="bedrock-Type-agent-runtime_ConditionResultEvent-timestamp"></a>
The timestamp when the condition evaluation occurred.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent-runtime_ConditionResultEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ConditionResultEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ConditionResultEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ConditionResultEvent) 