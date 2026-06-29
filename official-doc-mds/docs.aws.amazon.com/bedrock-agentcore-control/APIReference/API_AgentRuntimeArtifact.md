

# AgentRuntimeArtifact
<a name="API_AgentRuntimeArtifact"></a>

The artifact of the agent.

## Contents
<a name="API_AgentRuntimeArtifact_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** codeConfiguration **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeArtifact-codeConfiguration"></a>
The code configuration for the agent runtime artifact, including the source code location and execution settings.  
Type: [CodeConfiguration](API_CodeConfiguration.md) object  
Required: No

 ** containerConfiguration **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeArtifact-containerConfiguration"></a>
The container configuration for the agent artifact.  
Type: [ContainerConfiguration](API_ContainerConfiguration.md) object  
Required: No

## See Also
<a name="API_AgentRuntimeArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AgentRuntimeArtifact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AgentRuntimeArtifact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AgentRuntimeArtifact) 