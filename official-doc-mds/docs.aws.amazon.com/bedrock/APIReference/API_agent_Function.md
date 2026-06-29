

# Function
<a name="API_agent_Function"></a>

Defines parameters that the agent needs to invoke from the user to complete the function. Corresponds to an action in an action group.

This data type is used in the following API operations:
+  [CreateAgentActionGroup request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentActionGroup.html#API_agent_CreateAgentActionGroup_RequestSyntax) 
+  [CreateAgentActionGroup response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentActionGroup.html#API_agent_CreateAgentActionGroup_ResponseSyntax) 
+  [UpdateAgentActionGroup request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentActionGroup.html#API_agent_UpdateAgentActionGroup_RequestSyntax) 
+  [UpdateAgentActionGroup response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentActionGroup.html#API_agent_UpdateAgentActionGroup_ResponseSyntax) 
+  [GetAgentActionGroup response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html#API_agent_GetAgentActionGroup_ResponseSyntax) 

## Contents
<a name="API_agent_Function_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_Function-name"></a>
A name for the function.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** description **   <a name="bedrock-Type-agent_Function-description"></a>
A description of the function and its purpose.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1200.  
Required: No

 ** parameters **   <a name="bedrock-Type-agent_Function-parameters"></a>
The parameters that the agent elicits from the user to fulfill the function.  
Type: String to [ParameterDetail](API_agent_ParameterDetail.md) object map  
Key Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** requireConfirmation **   <a name="bedrock-Type-agent_Function-requireConfirmation"></a>
Contains information if user confirmation is required to invoke the function.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_agent_Function_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/Function) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/Function) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/Function) 