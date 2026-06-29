

# FlowAliasSummary
<a name="API_agent_FlowAliasSummary"></a>

Contains information about an alias of a flow.

This data type is used in the following API operations:
+  [ListFlowAliases response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListFlowAliases.html#API_agent_ListFlowAliases_ResponseSyntax) 

## Contents
<a name="API_agent_FlowAliasSummary_Contents"></a>

 ** arn **   <a name="bedrock-Type-agent_FlowAliasSummary-arn"></a>
The Amazon Resource Name (ARN) of the alias.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/(TSTALIASID|[0-9a-zA-Z]{10})`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_FlowAliasSummary-createdAt"></a>
The time at which the alias was created.  
Type: Timestamp  
Required: Yes

 ** flowId **   <a name="bedrock-Type-agent_FlowAliasSummary-flowId"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** id **   <a name="bedrock-Type-agent_FlowAliasSummary-id"></a>
The unique identifier of the alias of the flow.  
Type: String  
Pattern: `(TSTALIASID|[0-9a-zA-Z]{10})`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_FlowAliasSummary-name"></a>
The name of the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** routingConfiguration **   <a name="bedrock-Type-agent_FlowAliasSummary-routingConfiguration"></a>
A list of configurations about the versions that the alias maps to. Currently, you can only specify one.  
Type: Array of [FlowAliasRoutingConfigurationListItem](API_agent_FlowAliasRoutingConfigurationListItem.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_FlowAliasSummary-updatedAt"></a>
The time at which the alias was last updated.  
Type: Timestamp  
Required: Yes

 ** concurrencyConfiguration **   <a name="bedrock-Type-agent_FlowAliasSummary-concurrencyConfiguration"></a>
The configuration that specifies how nodes in the flow are executed concurrently.  
Type: [FlowAliasConcurrencyConfiguration](API_agent_FlowAliasConcurrencyConfiguration.md) object  
Required: No

 ** description **   <a name="bedrock-Type-agent_FlowAliasSummary-description"></a>
A description of the alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_FlowAliasSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowAliasSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowAliasSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowAliasSummary) 