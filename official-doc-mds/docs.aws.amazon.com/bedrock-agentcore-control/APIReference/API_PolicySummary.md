

# PolicySummary
<a name="API_PolicySummary"></a>

Represents a metadata-only summary of a policy resource. This structure contains resource identifiers, status, and timestamps without customer-encrypted fields such as definition, description, or status reasons. Policy summaries are returned by operations that do not require access to the customer's AWS KMS key.

## Contents
<a name="API_PolicySummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-PolicySummary-createdAt"></a>
The timestamp when the policy was originally created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PolicySummary-name"></a>
The customer-assigned name of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** policyArn **   <a name="bedrockagentcorecontrol-Type-PolicySummary-policyArn"></a>
The Amazon Resource Name (ARN) of the policy.  
Type: String  
Length Constraints: Minimum length of 96. Maximum length of 203.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** policyEngineId **   <a name="bedrockagentcorecontrol-Type-PolicySummary-policyEngineId"></a>
The identifier of the policy engine that manages this policy.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** policyId **   <a name="bedrockagentcorecontrol-Type-PolicySummary-policyId"></a>
The unique identifier for the policy.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PolicySummary-status"></a>
The current status of the policy.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-PolicySummary-updatedAt"></a>
The timestamp when the policy was last modified.  
Type: Timestamp  
Required: Yes

 ** enforcementMode **   <a name="bedrockagentcorecontrol-Type-PolicySummary-enforcementMode"></a>
The current enforcement mode of the policy.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY`   
Required: No

## See Also
<a name="API_PolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicySummary) 