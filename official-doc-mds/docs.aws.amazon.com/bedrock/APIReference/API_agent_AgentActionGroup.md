

# AgentActionGroup
<a name="API_agent_AgentActionGroup"></a>

Contains details about an action group.

## Contents
<a name="API_agent_AgentActionGroup_Contents"></a>

 ** actionGroupId **   <a name="bedrock-Type-agent_AgentActionGroup-actionGroupId"></a>
The unique identifier of the action group.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** actionGroupName **   <a name="bedrock-Type-agent_AgentActionGroup-actionGroupName"></a>
The name of the action group.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** actionGroupState **   <a name="bedrock-Type-agent_AgentActionGroup-actionGroupState"></a>
Specifies whether the action group is available for the agent to invoke or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent_AgentActionGroup-agentId"></a>
The unique identifier of the agent to which the action group belongs.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentVersion **   <a name="bedrock-Type-agent_AgentActionGroup-agentVersion"></a>
The version of the agent to which the action group belongs.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentActionGroup-createdAt"></a>
The time at which the action group was created.  
Type: Timestamp  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentActionGroup-updatedAt"></a>
The time at which the action group was last updated.  
Type: Timestamp  
Required: Yes

 ** actionGroupExecutor **   <a name="bedrock-Type-agent_AgentActionGroup-actionGroupExecutor"></a>
The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.  
Type: [ActionGroupExecutor](API_agent_ActionGroupExecutor.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** apiSchema **   <a name="bedrock-Type-agent_AgentActionGroup-apiSchema"></a>
Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html).  
Type: [APISchema](API_agent_APISchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** clientToken **   <a name="bedrock-Type-agent_AgentActionGroup-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** description **   <a name="bedrock-Type-agent_AgentActionGroup-description"></a>
The description of the action group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** functionSchema **   <a name="bedrock-Type-agent_AgentActionGroup-functionSchema"></a>
Defines functions that each define parameters that the agent needs to invoke from the user. Each function represents an action in an action group.  
Type: [FunctionSchema](API_agent_FunctionSchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** parentActionGroupSignatureParams **   <a name="bedrock-Type-agent_AgentActionGroup-parentActionGroupSignatureParams"></a>
The configuration settings for a computer use action.  
 Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html). 
Type: String to string map  
Key Length Constraints: Minimum length of 0. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 100.  
Required: No

 ** parentActionSignature **   <a name="bedrock-Type-agent_AgentActionGroup-parentActionSignature"></a>
If this field is set as `AMAZON.UserInput`, the agent can request the user for additional information when trying to complete a task. The `description`, `apiSchema`, and `actionGroupExecutor` fields must be blank for this action group.  
During orchestration, if the agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an [Observation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html) reprompting the user for more information.  
Type: String  
Valid Values: `AMAZON.UserInput | AMAZON.CodeInterpreter | ANTHROPIC.Computer | ANTHROPIC.Bash | ANTHROPIC.TextEditor`   
Required: No

## See Also
<a name="API_agent_AgentActionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentActionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentActionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentActionGroup) 