

# AgentFlowNodeConfiguration
<a name="API_agent_AgentFlowNodeConfiguration"></a>

Defines an agent node in your flow. You specify the agent to invoke at this point in the flow. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_AgentFlowNodeConfiguration_Contents"></a>

 ** agentAliasArn **   <a name="bedrock-Type-agent_AgentFlowNodeConfiguration-agentAliasArn"></a>
The Amazon Resource Name (ARN) of the alias of the agent to invoke.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `$|^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}`   
Required: Yes

## See Also
<a name="API_agent_AgentFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentFlowNodeConfiguration) 