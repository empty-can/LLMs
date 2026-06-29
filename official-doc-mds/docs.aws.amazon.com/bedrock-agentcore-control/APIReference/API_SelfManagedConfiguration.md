

# SelfManagedConfiguration
<a name="API_SelfManagedConfiguration"></a>

A configuration for a self-managed memory strategy.

## Contents
<a name="API_SelfManagedConfiguration_Contents"></a>

 ** historicalContextWindowSize **   <a name="bedrockagentcorecontrol-Type-SelfManagedConfiguration-historicalContextWindowSize"></a>
The number of historical messages to include in processing context.  
Type: Integer  
Required: Yes

 ** invocationConfiguration **   <a name="bedrockagentcorecontrol-Type-SelfManagedConfiguration-invocationConfiguration"></a>
The configuration to use when invoking memory processing.  
Type: [InvocationConfiguration](API_InvocationConfiguration.md) object  
Required: Yes

 ** triggerConditions **   <a name="bedrockagentcorecontrol-Type-SelfManagedConfiguration-triggerConditions"></a>
A list of conditions that trigger memory processing.  
Type: Array of [TriggerCondition](API_TriggerCondition.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## See Also
<a name="API_SelfManagedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SelfManagedConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SelfManagedConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SelfManagedConfiguration) 