

# HarnessAgentCoreRuntimeEnvironment
<a name="API_HarnessAgentCoreRuntimeEnvironment"></a>

The AgentCore Runtime environment for a harness.

## Contents
<a name="API_HarnessAgentCoreRuntimeEnvironment_Contents"></a>

 ** agentRuntimeArn **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironment-agentRuntimeArn"></a>
The ARN of the underlying AgentCore Runtime.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Required: Yes

 ** agentRuntimeId **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironment-agentRuntimeId"></a>
The ID of the underlying AgentCore Runtime.  
Type: String  
Required: Yes

 ** agentRuntimeName **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironment-agentRuntimeName"></a>
The name of the underlying AgentCore Runtime.  
Type: String  
Required: Yes

 ** lifecycleConfiguration **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironment-lifecycleConfiguration"></a>
LifecycleConfiguration lets you manage the lifecycle of runtime sessions and resources in AgentCore Runtime. This configuration helps optimize resource utilization by automatically cleaning up idle sessions and preventing long-running instances from consuming resources indefinitely.  
Type: [LifecycleConfiguration](API_LifecycleConfiguration.md) object  
Required: Yes

 ** networkConfiguration **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironment-networkConfiguration"></a>
SecurityConfig for the Agent.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: Yes

 ** filesystemConfigurations **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreRuntimeEnvironment-filesystemConfigurations"></a>
The filesystem configurations for the runtime environment.  
Type: Array of [FilesystemConfiguration](API_FilesystemConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_HarnessAgentCoreRuntimeEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreRuntimeEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreRuntimeEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreRuntimeEnvironment) 