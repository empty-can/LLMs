

# Agent
<a name="API_agent_Agent"></a>

Contains details about an agent.

## Contents
<a name="API_agent_Agent_Contents"></a>

 ** agentArn **   <a name="bedrock-Type-agent_Agent-agentArn"></a>
The Amazon Resource Name (ARN) of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent/[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent_Agent-agentId"></a>
The unique identifier of the agent.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentName **   <a name="bedrock-Type-agent_Agent-agentName"></a>
The name of the agent.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentResourceRoleArn **   <a name="bedrock-Type-agent_Agent-agentResourceRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** agentStatus **   <a name="bedrock-Type-agent_Agent-agentStatus"></a>
The status of the agent and whether it is ready for use. The following statuses are possible:  
+ CREATING – The agent is being created.
+ PREPARING – The agent is being prepared.
+ PREPARED – The agent is prepared and ready to be invoked.
+ NOT\_PREPARED – The agent has been created but not yet prepared.
+ FAILED – The agent API operation failed.
+ UPDATING – The agent is being updated.
+ DELETING – The agent is being deleted.
Type: String  
Valid Values: `CREATING | PREPARING | PREPARED | NOT_PREPARED | DELETING | FAILED | VERSIONING | UPDATING`   
Required: Yes

 ** agentVersion **   <a name="bedrock-Type-agent_Agent-agentVersion"></a>
The version of the agent.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_Agent-createdAt"></a>
The time at which the agent was created.  
Type: Timestamp  
Required: Yes

 ** idleSessionTTLInSeconds **   <a name="bedrock-Type-agent_Agent-idleSessionTTLInSeconds"></a>
The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.  
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 5400.  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_Agent-updatedAt"></a>
The time at which the agent was last updated.  
Type: Timestamp  
Required: Yes

 ** agentCollaboration **   <a name="bedrock-Type-agent_Agent-agentCollaboration"></a>
The agent's collaboration settings.  
Type: String  
Valid Values: `SUPERVISOR | SUPERVISOR_ROUTER | DISABLED`   
Required: No

 ** clientToken **   <a name="bedrock-Type-agent_Agent-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** customerEncryptionKeyArn **   <a name="bedrock-Type-agent_Agent-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that encrypts the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** customOrchestration **   <a name="bedrock-Type-agent_Agent-customOrchestration"></a>
 Contains custom orchestration configurations for the agent.   
Type: [CustomOrchestration](API_agent_CustomOrchestration.md) object  
Required: No

 ** description **   <a name="bedrock-Type-agent_Agent-description"></a>
The description of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** failureReasons **   <a name="bedrock-Type-agent_Agent-failureReasons"></a>
Contains reasons that the agent-related API that you invoked failed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** foundationModel **   <a name="bedrock-Type-agent_Agent-foundationModel"></a>
The foundation model used for orchestration by the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent_Agent-guardrailConfiguration"></a>
Details about the guardrail associated with the agent.  
Type: [GuardrailConfiguration](API_agent_GuardrailConfiguration.md) object  
Required: No

 ** instruction **   <a name="bedrock-Type-agent_Agent-instruction"></a>
Instructions that tell the agent what it should do and how it should interact with users.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 4000.  
Required: No

 ** memoryConfiguration **   <a name="bedrock-Type-agent_Agent-memoryConfiguration"></a>
Contains memory configuration for the agent.  
Type: [MemoryConfiguration](API_agent_MemoryConfiguration.md) object  
Required: No

 ** orchestrationType **   <a name="bedrock-Type-agent_Agent-orchestrationType"></a>
 Specifies the orchestration strategy for the agent.   
Type: String  
Valid Values: `DEFAULT | CUSTOM_ORCHESTRATION`   
Required: No

 ** preparedAt **   <a name="bedrock-Type-agent_Agent-preparedAt"></a>
The time at which the agent was last prepared.  
Type: Timestamp  
Required: No

 ** promptOverrideConfiguration **   <a name="bedrock-Type-agent_Agent-promptOverrideConfiguration"></a>
Contains configurations to override prompt templates in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).  
Type: [PromptOverrideConfiguration](API_agent_PromptOverrideConfiguration.md) object  
Required: No

 ** recommendedActions **   <a name="bedrock-Type-agent_Agent-recommendedActions"></a>
Contains recommended actions to take for the agent-related API that you invoked to succeed.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

## See Also
<a name="API_agent_Agent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/Agent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/Agent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/Agent) 