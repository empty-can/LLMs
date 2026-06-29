

# AgentVersion
<a name="API_agent_AgentVersion"></a>

Contains details about a version of an agent.

## Contents
<a name="API_agent_AgentVersion_Contents"></a>

 ** agentArn **   <a name="bedrock-Type-agent_AgentVersion-agentArn"></a>
The Amazon Resource Name (ARN) of the agent that the version belongs to.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent/[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent_AgentVersion-agentId"></a>
The unique identifier of the agent that the version belongs to.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentName **   <a name="bedrock-Type-agent_AgentVersion-agentName"></a>
The name of the agent that the version belongs to.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentResourceRoleArn **   <a name="bedrock-Type-agent_AgentVersion-agentResourceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** agentStatus **   <a name="bedrock-Type-agent_AgentVersion-agentStatus"></a>
The status of the agent that the version belongs to.  
Type: String  
Valid Values: `CREATING | PREPARING | PREPARED | NOT_PREPARED | DELETING | FAILED | VERSIONING | UPDATING`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentVersion-createdAt"></a>
The time at which the version was created.  
Type: Timestamp  
Required: Yes

 ** idleSessionTTLInSeconds **   <a name="bedrock-Type-agent_AgentVersion-idleSessionTTLInSeconds"></a>
The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.  
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 5400.  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentVersion-updatedAt"></a>
The time at which the version was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="bedrock-Type-agent_AgentVersion-version"></a>
The version number.  
Type: String  
Pattern: `[0-9]{1,5}`   
Required: Yes

 ** agentCollaboration **   <a name="bedrock-Type-agent_AgentVersion-agentCollaboration"></a>
The agent's collaboration settings.  
Type: String  
Valid Values: `SUPERVISOR | SUPERVISOR_ROUTER | DISABLED`   
Required: No

 ** customerEncryptionKeyArn **   <a name="bedrock-Type-agent_AgentVersion-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that encrypts the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** description **   <a name="bedrock-Type-agent_AgentVersion-description"></a>
The description of the version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** failureReasons **   <a name="bedrock-Type-agent_AgentVersion-failureReasons"></a>
A list of reasons that the API operation on the version failed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** foundationModel **   <a name="bedrock-Type-agent_AgentVersion-foundationModel"></a>
The foundation model that the version invokes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent_AgentVersion-guardrailConfiguration"></a>
Details about the guardrail associated with the agent.  
Type: [GuardrailConfiguration](API_agent_GuardrailConfiguration.md) object  
Required: No

 ** instruction **   <a name="bedrock-Type-agent_AgentVersion-instruction"></a>
The instructions provided to the agent.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 4000.  
Required: No

 ** memoryConfiguration **   <a name="bedrock-Type-agent_AgentVersion-memoryConfiguration"></a>
 Contains details of the memory configuration on the version of the agent.   
Type: [MemoryConfiguration](API_agent_MemoryConfiguration.md) object  
Required: No

 ** promptOverrideConfiguration **   <a name="bedrock-Type-agent_AgentVersion-promptOverrideConfiguration"></a>
Contains configurations to override prompt templates in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).  
Type: [PromptOverrideConfiguration](API_agent_PromptOverrideConfiguration.md) object  
Required: No

 ** recommendedActions **   <a name="bedrock-Type-agent_AgentVersion-recommendedActions"></a>
A list of recommended actions to take for the failed API operation on the version to succeed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

## See Also
<a name="API_agent_AgentVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentVersion) 