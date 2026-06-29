

# ActionGroupSummary
<a name="API_agent_ActionGroupSummary"></a>

Contains details about an action group.

## Contents
<a name="API_agent_ActionGroupSummary_Contents"></a>

 ** actionGroupId **   <a name="bedrock-Type-agent_ActionGroupSummary-actionGroupId"></a>
The unique identifier of the action group.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** actionGroupName **   <a name="bedrock-Type-agent_ActionGroupSummary-actionGroupName"></a>
The name of the action group.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** actionGroupState **   <a name="bedrock-Type-agent_ActionGroupSummary-actionGroupState"></a>
Specifies whether the action group is available for the agent to invoke or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_ActionGroupSummary-updatedAt"></a>
The time at which the action group was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_ActionGroupSummary-description"></a>
The description of the action group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_ActionGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ActionGroupSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ActionGroupSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ActionGroupSummary) 