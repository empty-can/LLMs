

# TriggerCondition
<a name="API_TriggerCondition"></a>

Condition that triggers memory processing.

## Contents
<a name="API_TriggerCondition_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** messageBasedTrigger **   <a name="bedrockagentcorecontrol-Type-TriggerCondition-messageBasedTrigger"></a>
Message based trigger configuration.  
Type: [MessageBasedTrigger](API_MessageBasedTrigger.md) object  
Required: No

 ** timeBasedTrigger **   <a name="bedrockagentcorecontrol-Type-TriggerCondition-timeBasedTrigger"></a>
Time based trigger configuration.  
Type: [TimeBasedTrigger](API_TimeBasedTrigger.md) object  
Required: No

 ** tokenBasedTrigger **   <a name="bedrockagentcorecontrol-Type-TriggerCondition-tokenBasedTrigger"></a>
Token based trigger configuration.  
Type: [TokenBasedTrigger](API_TokenBasedTrigger.md) object  
Required: No

## See Also
<a name="API_TriggerCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TriggerCondition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TriggerCondition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TriggerCondition) 