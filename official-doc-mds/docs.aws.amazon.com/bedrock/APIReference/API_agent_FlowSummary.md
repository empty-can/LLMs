

# FlowSummary
<a name="API_agent_FlowSummary"></a>

Contains the definition of a flow.

## Contents
<a name="API_agent_FlowSummary_Contents"></a>

 ** arn **   <a name="bedrock-Type-agent_FlowSummary-arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_FlowSummary-createdAt"></a>
The time at which the flow was created.  
Type: Timestamp  
Required: Yes

 ** id **   <a name="bedrock-Type-agent_FlowSummary-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_FlowSummary-name"></a>
The name of the flow.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_FlowSummary-status"></a>
The status of the flow. The following statuses are possible:  
+ NotPrepared – The flow has been created or updated, but hasn't been prepared. If you just created the flow, you can't test it. If you updated the flow, the `DRAFT` version won't contain the latest changes for testing. Send a [PrepareFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PrepareFlow.html) request to package the latest changes into the `DRAFT` version.
+ Preparing – The flow is being prepared so that the `DRAFT` version contains the latest changes for testing.
+ Prepared – The flow is prepared and the `DRAFT` version contains the latest changes for testing.
+ Failed – The last API operation that you invoked on the flow failed. Send a [GetFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html) request and check the error message in the `validations` field.
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_FlowSummary-updatedAt"></a>
The time at which the flow was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="bedrock-Type-agent_FlowSummary-version"></a>
The latest version of the flow.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

 ** description **   <a name="bedrock-Type-agent_FlowSummary-description"></a>
A description of the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_FlowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowSummary) 