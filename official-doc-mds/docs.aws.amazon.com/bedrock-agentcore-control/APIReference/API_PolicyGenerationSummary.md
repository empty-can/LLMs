

# PolicyGenerationSummary
<a name="API_PolicyGenerationSummary"></a>

Represents a metadata-only summary of a policy generation resource. This structure contains resource identifiers, status, timestamps, and findings without customer-encrypted fields such as status reasons. Policy generation summaries are returned by operations that do not require access to the customer's AWS KMS key.

## Contents
<a name="API_PolicyGenerationSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-createdAt"></a>
The timestamp when this policy generation request was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-name"></a>
The customer-assigned name for this policy generation request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** policyEngineId **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-policyEngineId"></a>
The identifier of the policy engine associated with this generation request.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** policyGenerationArn **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-policyGenerationArn"></a>
The ARN of this policy generation request.  
Type: String  
Length Constraints: Minimum length of 103. Maximum length of 210.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy-generation/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** policyGenerationId **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-policyGenerationId"></a>
The unique identifier for this policy generation request.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** resource **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-resource"></a>
The resource information associated with this policy generation.  
Type: [Resource](API_Resource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-status"></a>
The current status of this policy generation request.  
Type: String  
Valid Values: `GENERATING | GENERATED | GENERATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-updatedAt"></a>
The timestamp when this policy generation was last updated.  
Type: Timestamp  
Required: Yes

 ** findings **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationSummary-findings"></a>
Findings and insights from this policy generation process.  
Type: String  
Required: No

## See Also
<a name="API_PolicyGenerationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyGenerationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyGenerationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyGenerationSummary) 