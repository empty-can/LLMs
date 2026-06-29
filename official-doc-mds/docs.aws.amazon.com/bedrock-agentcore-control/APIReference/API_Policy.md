

# Policy
<a name="API_Policy"></a>

Represents a complete policy resource within the AgentCore Policy system. Policies are ARN-able resources that contain Cedar policy statements and associated metadata for controlling agent behavior and access decisions. Each policy belongs to a policy engine and defines fine-grained authorization rules that are evaluated in real-time as agents interact with tools through Gateway. Policies use the Cedar policy language to specify who (principals based on OAuth claims like username, role, or scope) can perform what actions (tool calls) on which resources (Gateways), with optional conditions for attribute-based access control. Multiple policies can apply to a single request, with Cedar's forbid-wins semantics ensuring that security restrictions are never accidentally overridden.

## Contents
<a name="API_Policy_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-Policy-createdAt"></a>
The timestamp when the policy was originally created. This is automatically set by the service and used for auditing and lifecycle management.  
Type: Timestamp  
Required: Yes

 ** definition **   <a name="bedrockagentcorecontrol-Type-Policy-definition"></a>
The Cedar policy statement that defines the access control rules. This contains the actual policy logic used for agent behavior control and access decisions.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-Policy-name"></a>
The customer-assigned immutable name for the policy. This human-readable identifier must be unique within the account and cannot exceed 48 characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** policyArn **   <a name="bedrockagentcorecontrol-Type-Policy-policyArn"></a>
The Amazon Resource Name (ARN) of the policy. This globally unique identifier can be used for cross-service references and IAM policy statements.  
Type: String  
Length Constraints: Minimum length of 96. Maximum length of 203.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** policyEngineId **   <a name="bedrockagentcorecontrol-Type-Policy-policyEngineId"></a>
The identifier of the policy engine that manages this policy. This establishes the policy engine context for policy evaluation and management.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** policyId **   <a name="bedrockagentcorecontrol-Type-Policy-policyId"></a>
The unique identifier for the policy. This system-generated identifier consists of the user name plus a 10-character generated suffix and serves as the primary key for policy operations.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-Policy-status"></a>
The current status of the policy.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** statusReasons **   <a name="bedrockagentcorecontrol-Type-Policy-statusReasons"></a>
Additional information about the policy status. This provides details about any failures or the current state of the policy lifecycle.  
Type: Array of strings  
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-Policy-updatedAt"></a>
The timestamp when the policy was last modified. This tracks the most recent changes to the policy configuration or metadata.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-Policy-description"></a>
A human-readable description of the policy's purpose and functionality. Limited to 4,096 characters, this helps administrators understand and manage the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** enforcementMode **   <a name="bedrockagentcorecontrol-Type-Policy-enforcementMode"></a>
The current enforcement mode of the policy.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY`   
Required: No

## See Also
<a name="API_Policy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Policy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Policy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Policy) 