

# PolicyGeneration
<a name="API_PolicyGeneration"></a>

Represents a policy generation request within the AgentCore Policy system. Tracks the AI-powered conversion of natural language descriptions into Cedar policy statements, enabling users to author policies by describing authorization requirements in plain English. The generation process analyzes the natural language input along with the Gateway's tool context and Cedar schema to produce one or more validated policy options. Each generation request tracks the status of the conversion process and maintains findings about the generated policies, including validation results and potential issues. Generated policy assets remain available for one week after successful generation, allowing time to review and create policies from the generated options.

## Contents
<a name="API_PolicyGeneration_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-createdAt"></a>
The timestamp when this policy generation request was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-name"></a>
The customer-assigned name for this policy generation request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** policyEngineId **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-policyEngineId"></a>
The identifier of the policy engine associated with this generation request.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** policyGenerationArn **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-policyGenerationArn"></a>
The ARN of this policy generation request.  
Type: String  
Length Constraints: Minimum length of 103. Maximum length of 210.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy-generation/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** policyGenerationId **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-policyGenerationId"></a>
The unique identifier for this policy generation request.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** resource **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-resource"></a>
The resource information associated with this policy generation.  
Type: [Resource](API_Resource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-status"></a>
The current status of this policy generation request.  
Type: String  
Valid Values: `GENERATING | GENERATED | GENERATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** statusReasons **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-statusReasons"></a>
Additional information about the generation status.  
Type: Array of strings  
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-updatedAt"></a>
The timestamp when this policy generation was last updated.  
Type: Timestamp  
Required: Yes

 ** findings **   <a name="bedrockagentcorecontrol-Type-PolicyGeneration-findings"></a>
Findings and insights from this policy generation process.  
Type: String  
Required: No

## See Also
<a name="API_PolicyGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyGeneration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyGeneration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyGeneration) 