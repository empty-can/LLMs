

# PolicyEngineSummary
<a name="API_PolicyEngineSummary"></a>

Represents a metadata-only summary of a policy engine resource. This structure contains resource identifiers, status, and timestamps without customer-encrypted fields such as description or status reasons. Policy engine summaries are returned by operations that do not require access to the customer's AWS KMS key.

## Contents
<a name="API_PolicyEngineSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-createdAt"></a>
The timestamp when the policy engine was originally created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-name"></a>
The customer-assigned name of the policy engine.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** policyEngineArn **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-policyEngineArn"></a>
The Amazon Resource Name (ARN) of the policy engine.  
Type: String  
Length Constraints: Minimum length of 76. Maximum length of 136.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** policyEngineId **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-policyEngineId"></a>
The unique identifier for the policy engine.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-status"></a>
The current status of the policy engine.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-updatedAt"></a>
The timestamp when the policy engine was last modified.  
Type: Timestamp  
Required: Yes

 ** encryptionKeyArn **   <a name="bedrockagentcorecontrol-Type-PolicyEngineSummary-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the policy engine data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

## See Also
<a name="API_PolicyEngineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyEngineSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyEngineSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyEngineSummary) 