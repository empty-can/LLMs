

# Observation
<a name="API_agent-runtime_Observation"></a>

Contains the result or output of an action group or knowledge base, or the response to the user.

## Contents
<a name="API_agent-runtime_Observation_Contents"></a>

 ** actionGroupInvocationOutput **   <a name="bedrock-Type-agent-runtime_Observation-actionGroupInvocationOutput"></a>
Contains the JSON-formatted string returned by the API invoked by the action group.  
Type: [ActionGroupInvocationOutput](API_agent-runtime_ActionGroupInvocationOutput.md) object  
Required: No

 ** agentCollaboratorInvocationOutput **   <a name="bedrock-Type-agent-runtime_Observation-agentCollaboratorInvocationOutput"></a>
A collaborator's invocation output.  
Type: [AgentCollaboratorInvocationOutput](API_agent-runtime_AgentCollaboratorInvocationOutput.md) object  
Required: No

 ** codeInterpreterInvocationOutput **   <a name="bedrock-Type-agent-runtime_Observation-codeInterpreterInvocationOutput"></a>
Contains the JSON-formatted string returned by the API invoked by the code interpreter.  
Type: [CodeInterpreterInvocationOutput](API_agent-runtime_CodeInterpreterInvocationOutput.md) object  
Required: No

 ** finalResponse **   <a name="bedrock-Type-agent-runtime_Observation-finalResponse"></a>
Contains details about the response to the user.  
Type: [FinalResponse](API_agent-runtime_FinalResponse.md) object  
Required: No

 ** knowledgeBaseLookupOutput **   <a name="bedrock-Type-agent-runtime_Observation-knowledgeBaseLookupOutput"></a>
Contains details about the results from looking up the knowledge base.  
Type: [KnowledgeBaseLookupOutput](API_agent-runtime_KnowledgeBaseLookupOutput.md) object  
Required: No

 ** repromptResponse **   <a name="bedrock-Type-agent-runtime_Observation-repromptResponse"></a>
Contains details about the response to reprompt the input.  
Type: [RepromptResponse](API_agent-runtime_RepromptResponse.md) object  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_Observation-traceId"></a>
The unique identifier of the trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_Observation-type"></a>
Specifies what kind of information the agent returns in the observation. The following values are possible.  
+  `ACTION_GROUP` – The agent returns the result of an action group.
+  `KNOWLEDGE_BASE` – The agent returns information from a knowledge base.
+  `FINISH` – The agent returns a final response to the user with no follow-up.
+  `ASK_USER` – The agent asks the user a question.
+  `REPROMPT` – The agent prompts the user again for the same information.
Type: String  
Valid Values: `ACTION_GROUP | AGENT_COLLABORATOR | KNOWLEDGE_BASE | FINISH | ASK_USER | REPROMPT`   
Required: No

## See Also
<a name="API_agent-runtime_Observation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Observation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Observation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Observation) 