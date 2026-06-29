

# FlowVersionSummary
<a name="API_agent_FlowVersionSummary"></a>

Contains information about a version of a flow.

This data type is used in the following API operations:
+  [ListFlowVersions response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListFlowVersions.html#API_agent_ListFlowVersions_ResponseSyntax) 

## Contents
<a name="API_agent_FlowVersionSummary_Contents"></a>

 ** arn **   <a name="bedrock-Type-agent_FlowVersionSummary-arn"></a>
The Amazon Resource Name (ARN) of the flow that the version belongs to.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_FlowVersionSummary-createdAt"></a>
The time at the version was created.  
Type: Timestamp  
Required: Yes

 ** id **   <a name="bedrock-Type-agent_FlowVersionSummary-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_FlowVersionSummary-status"></a>
The status of the flow.  
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared`   
Required: Yes

 ** version **   <a name="bedrock-Type-agent_FlowVersionSummary-version"></a>
The version of the flow.  
Type: String  
Pattern: `[0-9]{1,5}`   
Required: Yes

## See Also
<a name="API_agent_FlowVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowVersionSummary) 