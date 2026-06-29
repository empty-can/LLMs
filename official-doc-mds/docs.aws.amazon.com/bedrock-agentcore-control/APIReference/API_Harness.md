

# Harness
<a name="API_Harness"></a>

Representation of a harness.

## Contents
<a name="API_Harness_Contents"></a>

 ** allowedTools **   <a name="bedrockagentcorecontrol-Type-Harness-allowedTools"></a>
The allowed tools of the harness. All tools are allowed by default.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `(\*|@?[^/]+(/[^/]+)?)`   
Required: Yes

 ** arn **   <a name="bedrockagentcorecontrol-Type-Harness-arn"></a>
The ARN of the harness.  
Type: String  
Pattern: `arn:([^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:harness/[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-Harness-createdAt"></a>
The createdAt time of the harness.  
Type: Timestamp  
Required: Yes

 ** environment **   <a name="bedrockagentcorecontrol-Type-Harness-environment"></a>
The compute environment on which the Harness runs.  
Type: [HarnessEnvironmentProvider](API_HarnessEnvironmentProvider.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** executionRoleArn **   <a name="bedrockagentcorecontrol-Type-Harness-executionRoleArn"></a>
IAM role the harness assumes when running.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** harnessId **   <a name="bedrockagentcorecontrol-Type-Harness-harnessId"></a>
The ID of the harness.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** harnessName **   <a name="bedrockagentcorecontrol-Type-Harness-harnessName"></a>
The name of the harness.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}`   
Required: Yes

 ** model **   <a name="bedrockagentcorecontrol-Type-Harness-model"></a>
The configuration of the default model used by the Harness.  
Type: [HarnessModelConfiguration](API_HarnessModelConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** skills **   <a name="bedrockagentcorecontrol-Type-Harness-skills"></a>
The skills of the harness.  
Type: Array of [HarnessSkill](API_HarnessSkill.md) objects  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-Harness-status"></a>
The status of the harness.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED`   
Required: Yes

 ** systemPrompt **   <a name="bedrockagentcorecontrol-Type-Harness-systemPrompt"></a>
The system prompt of the harness.  
Type: Array of [HarnessSystemContentBlock](API_HarnessSystemContentBlock.md) objects  
Required: Yes

 ** tools **   <a name="bedrockagentcorecontrol-Type-Harness-tools"></a>
The tools of the harness.  
Type: Array of [HarnessTool](API_HarnessTool.md) objects  
Required: Yes

 ** truncation **   <a name="bedrockagentcorecontrol-Type-Harness-truncation"></a>
Configuration for truncating model context.  
Type: [HarnessTruncationConfiguration](API_HarnessTruncationConfiguration.md) object  
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-Harness-updatedAt"></a>
The updatedAt time of the harness.  
Type: Timestamp  
Required: Yes

 ** authorizerConfiguration **   <a name="bedrockagentcorecontrol-Type-Harness-authorizerConfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.   
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** environmentArtifact **   <a name="bedrockagentcorecontrol-Type-Harness-environmentArtifact"></a>
The environment artifact (e.g., container) in which the Harness operates.  
Type: [HarnessEnvironmentArtifact](API_HarnessEnvironmentArtifact.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** environmentVariables **   <a name="bedrockagentcorecontrol-Type-Harness-environmentVariables"></a>
Environment variables exposed in the environment in which the harness operates.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.  
Required: No

 ** failureReason **   <a name="bedrockagentcorecontrol-Type-Harness-failureReason"></a>
Reason why create or update operations fail.  
Type: String  
Required: No

 ** harnessVersion **   <a name="bedrockagentcorecontrol-Type-Harness-harnessVersion"></a>
The version of the harness. Incremented on every successful UpdateHarness.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

 ** maxIterations **   <a name="bedrockagentcorecontrol-Type-Harness-maxIterations"></a>
The maximum number of iterations in the agent loop allowed before exiting per invocation.  
Type: Integer  
Required: No

 ** maxTokens **   <a name="bedrockagentcorecontrol-Type-Harness-maxTokens"></a>
The maximum total number of output tokens the agent can generate across all model calls within a single invocation.  
Type: Integer  
Required: No

 ** memory **   <a name="bedrockagentcorecontrol-Type-Harness-memory"></a>
AgentCore Memory instance configuration for short and long term memory.  
Type: [HarnessMemoryConfiguration](API_HarnessMemoryConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** timeoutSeconds **   <a name="bedrockagentcorecontrol-Type-Harness-timeoutSeconds"></a>
The maximum duration per invocation.  
Type: Integer  
Required: No

## See Also
<a name="API_Harness_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Harness) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Harness) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Harness) 