

# PolicyEngine
<a name="API_PolicyEngine"></a>

Represents a policy engine resource within the AgentCore Policy system. Policy engines serve as containers for grouping related policies and provide the execution context for policy evaluation and management. Each policy engine can be associated with one Gateway (one engine per Gateway), where it intercepts all agent tool calls and evaluates them against the contained policies before allowing tools to execute. The policy engine maintains the Cedar schema generated from the Gateway's tool manifest, ensuring that policies are validated against the actual tools and parameters available. Policy engines support two enforcement modes that can be configured when associating with a Gateway: log-only mode for testing (evaluates decisions without blocking) and enforce mode for production (actively allows or denies based on policy evaluation).

## Contents
<a name="API_PolicyEngine_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-createdAt"></a>
The timestamp when the policy engine was originally created. This is automatically set by the service and used for auditing and lifecycle management.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-name"></a>
The customer-assigned immutable name for the policy engine. This human-readable identifier must be unique within the account and cannot exceed 48 characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** policyEngineArn **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-policyEngineArn"></a>
The Amazon Resource Name (ARN) of the policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.  
Type: String  
Length Constraints: Minimum length of 76. Maximum length of 136.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** policyEngineId **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-policyEngineId"></a>
The unique identifier for the policy engine. This system-generated identifier consists of the user name plus a 10-character generated suffix and serves as the primary key for policy engine operations.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-status"></a>
The current status of the policy engine.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** statusReasons **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-statusReasons"></a>
Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine lifecycle.  
Type: Array of strings  
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-updatedAt"></a>
The timestamp when the policy engine was last modified. This tracks the most recent changes to the policy engine configuration or metadata.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-description"></a>
A human-readable description of the policy engine's purpose and scope. Limited to 4,096 characters, this helps administrators understand the policy engine's role in the overall governance strategy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** encryptionKeyArn **   <a name="bedrockagentcorecontrol-Type-PolicyEngine-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the policy engine data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

## See Also
<a name="API_PolicyEngine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyEngine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyEngine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyEngine) 