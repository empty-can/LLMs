

# TriggerConditionInput
<a name="API_TriggerConditionInput"></a>

Condition that triggers memory processing.

## Contents
<a name="API_TriggerConditionInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** messageBasedTrigger **   <a name="bedrockagentcorecontrol-Type-TriggerConditionInput-messageBasedTrigger"></a>
Message based trigger configuration.  
Type: [MessageBasedTriggerInput](API_MessageBasedTriggerInput.md) object  
Required: No

 ** timeBasedTrigger **   <a name="bedrockagentcorecontrol-Type-TriggerConditionInput-timeBasedTrigger"></a>
Time based trigger configuration.  
Type: [TimeBasedTriggerInput](API_TimeBasedTriggerInput.md) object  
Required: No

 ** tokenBasedTrigger **   <a name="bedrockagentcorecontrol-Type-TriggerConditionInput-tokenBasedTrigger"></a>
Token based trigger configuration.  
Type: [TokenBasedTriggerInput](API_TokenBasedTriggerInput.md) object  
Required: No

## See Also
<a name="API_TriggerConditionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TriggerConditionInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TriggerConditionInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TriggerConditionInput) 