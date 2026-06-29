

# GatewayRuleDetail
<a name="API_GatewayRuleDetail"></a>

Detailed information about a gateway rule.

## Contents
<a name="API_GatewayRuleDetail_Contents"></a>

 ** actions **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-actions"></a>
The actions to take when the rule conditions are met.  
Type: Array of [Action](API_Action.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-createdAt"></a>
The timestamp when the rule was created.  
Type: Timestamp  
Required: Yes

 ** gatewayArn **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway that the rule belongs to.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** priority **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-priority"></a>
The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000000.  
Required: Yes

 ** ruleId **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-ruleId"></a>
The unique identifier of the gateway rule.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-status"></a>
The current status of the rule.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING`   
Required: Yes

 ** conditions **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-conditions"></a>
The conditions that must be met for the rule to apply.  
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-description"></a>
The description of the gateway rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** system **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-system"></a>
System-managed metadata for rules created by automated processes.  
Type: [SystemManagedBlock](API_SystemManagedBlock.md) object  
Required: No

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-GatewayRuleDetail-updatedAt"></a>
The timestamp when the rule was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_GatewayRuleDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GatewayRuleDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GatewayRuleDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GatewayRuleDetail) 