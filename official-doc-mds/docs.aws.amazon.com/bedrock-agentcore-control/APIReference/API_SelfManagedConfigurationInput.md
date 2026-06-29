

# SelfManagedConfigurationInput
<a name="API_SelfManagedConfigurationInput"></a>

Input configuration for a self-managed memory strategy.

## Contents
<a name="API_SelfManagedConfigurationInput_Contents"></a>

 ** invocationConfiguration **   <a name="bedrockagentcorecontrol-Type-SelfManagedConfigurationInput-invocationConfiguration"></a>
Configuration to invoke a self-managed memory processing pipeline with.  
Type: [InvocationConfigurationInput](API_InvocationConfigurationInput.md) object  
Required: Yes

 ** historicalContextWindowSize **   <a name="bedrockagentcorecontrol-Type-SelfManagedConfigurationInput-historicalContextWindowSize"></a>
Number of historical messages to include in processing context.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 50.  
Required: No

 ** triggerConditions **   <a name="bedrockagentcorecontrol-Type-SelfManagedConfigurationInput-triggerConditions"></a>
A list of conditions that trigger memory processing.  
Type: Array of [TriggerConditionInput](API_TriggerConditionInput.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## See Also
<a name="API_SelfManagedConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SelfManagedConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SelfManagedConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SelfManagedConfigurationInput) 