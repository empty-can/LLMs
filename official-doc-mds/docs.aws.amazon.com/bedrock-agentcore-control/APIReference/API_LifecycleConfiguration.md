

# LifecycleConfiguration
<a name="API_LifecycleConfiguration"></a>

LifecycleConfiguration lets you manage the lifecycle of runtime sessions and resources in AgentCore Runtime. This configuration helps optimize resource utilization by automatically cleaning up idle sessions and preventing long-running instances from consuming resources indefinitely.

## Contents
<a name="API_LifecycleConfiguration_Contents"></a>

 ** idleRuntimeSessionTimeout **   <a name="bedrockagentcorecontrol-Type-LifecycleConfiguration-idleRuntimeSessionTimeout"></a>
Timeout in seconds for idle runtime sessions. When a session remains idle for this duration, it will be automatically terminated. Default: 900 seconds (15 minutes).  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 28800.  
Required: No

 ** maxLifetime **   <a name="bedrockagentcorecontrol-Type-LifecycleConfiguration-maxLifetime"></a>
Maximum lifetime for the instance in seconds. Once reached, instances will be automatically terminated and replaced. Default: 28800 seconds (8 hours).  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 28800.  
Required: No

## See Also
<a name="API_LifecycleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LifecycleConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LifecycleConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LifecycleConfiguration) 