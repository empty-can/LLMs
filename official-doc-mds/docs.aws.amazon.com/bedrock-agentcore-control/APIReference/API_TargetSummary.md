

# TargetSummary
<a name="API_TargetSummary"></a>

Contains summary information about a gateway target. A target represents an endpoint that the gateway can connect to.

## Contents
<a name="API_TargetSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-TargetSummary-createdAt"></a>
The timestamp when the target was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-TargetSummary-name"></a>
The name of the target.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-TargetSummary-status"></a>
The current status of the target.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED | SYNCHRONIZING | SYNCHRONIZE_UNSUCCESSFUL | CREATE_PENDING_AUTH | UPDATE_PENDING_AUTH | SYNCHRONIZE_PENDING_AUTH`   
Required: Yes

 ** targetId **   <a name="bedrockagentcorecontrol-Type-TargetSummary-targetId"></a>
The unique identifier of the target.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-TargetSummary-updatedAt"></a>
The timestamp when the target was last updated.  
Type: Timestamp  
Required: Yes

 ** authorizationData **   <a name="bedrockagentcorecontrol-Type-TargetSummary-authorizationData"></a>
Contains the authorization data that is returned when a gateway target is configured with a credential provider with authorization code grant type and requires user federation.  
Type: [AuthorizationData](API_AuthorizationData.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-TargetSummary-description"></a>
The description of the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** lastSynchronizedAt **   <a name="bedrockagentcorecontrol-Type-TargetSummary-lastSynchronizedAt"></a>
The timestamp when the target was last synchronized.  
Type: Timestamp  
Required: No

 ** listingMode **   <a name="bedrockagentcorecontrol-Type-TargetSummary-listingMode"></a>
The listing mode for the target. MCP resources for `DEFAULT` targets are cached at the control plane for faster access. MCP resources for `DYNAMIC` targets are retrieved dynamically when listing tools.  
Type: String  
Valid Values: `DEFAULT | DYNAMIC`   
Required: No

 ** resourcePriority **   <a name="bedrockagentcorecontrol-Type-TargetSummary-resourcePriority"></a>
Priority for resolving resource URI conflicts across targets. Lower values take precedence. Defaults to 1000 when not set.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000.  
Required: No

 ** targetType **   <a name="bedrockagentcorecontrol-Type-TargetSummary-targetType"></a>
The type of the target.  
Type: String  
Valid Values: `OPEN_API_SCHEMA | SMITHY_MODEL | MCP_SERVER | LAMBDA | API_GATEWAY | CONNECTOR | AGENTCORE_RUNTIME | PASSTHROUGH | PROVIDER`   
Required: No

## See Also
<a name="API_TargetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TargetSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TargetSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TargetSummary) 