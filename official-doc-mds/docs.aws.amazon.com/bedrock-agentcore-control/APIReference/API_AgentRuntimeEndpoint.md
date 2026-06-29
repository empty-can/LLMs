

# AgentRuntimeEndpoint
<a name="API_AgentRuntimeEndpoint"></a>

Contains information about an agent runtime endpoint. An endpoint provides a way to connect to and interact with an agent runtime.

## Contents
<a name="API_AgentRuntimeEndpoint_Contents"></a>

 ** agentRuntimeArn **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the agent runtime associated with the endpoint.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agent/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}:([0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** agentRuntimeEndpointArn **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-agentRuntimeEndpointArn"></a>
The Amazon Resource Name (ARN) of the agent runtime endpoint.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:agentEndpoint/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-createdAt"></a>
The timestamp when the agent runtime endpoint was created.  
Type: Timestamp  
Required: Yes

 ** id **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-id"></a>
The unique identifier of the agent runtime endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-lastUpdatedAt"></a>
The timestamp when the agent runtime endpoint was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-name"></a>
The name of the agent runtime endpoint.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-status"></a>
The current status of the agent runtime endpoint.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-description"></a>
The description of the agent runtime endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** liveVersion **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-liveVersion"></a>
The live version of the agent runtime endpoint. This is the version that is currently serving requests.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

 ** targetVersion **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeEndpoint-targetVersion"></a>
The target version of the agent runtime endpoint. This is the version that the endpoint is being updated to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

## See Also
<a name="API_AgentRuntimeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AgentRuntimeEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AgentRuntimeEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AgentRuntimeEndpoint) 