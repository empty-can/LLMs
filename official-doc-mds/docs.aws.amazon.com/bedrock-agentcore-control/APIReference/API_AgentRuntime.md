

# AgentRuntime
<a name="API_AgentRuntime"></a>

Contains information about an agent runtime. An agent runtime is the execution environment for a Amazon Bedrock AgentCore Agent.

## Contents
<a name="API_AgentRuntime_Contents"></a>

 ** agentRuntimeArn **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the agent runtime.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** agentRuntimeId **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-agentRuntimeId"></a>
The unique identifier of the agent runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** agentRuntimeName **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-agentRuntimeName"></a>
The name of the agent runtime.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** agentRuntimeVersion **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-agentRuntimeVersion"></a>
The version of the agent runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-description"></a>
The description of the agent runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: Yes

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-lastUpdatedAt"></a>
The timestamp when the agent runtime was last updated.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-AgentRuntime-status"></a>
The current status of the agent runtime.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING`   
Required: Yes

## See Also
<a name="API_AgentRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AgentRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AgentRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AgentRuntime) 