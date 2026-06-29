

# PolicyDefinition
<a name="API_PolicyDefinition"></a>

Represents the definition structure for policies within the AgentCore Policy system. This structure encapsulates different policy formats and languages that can be used to define access control rules.

## Contents
<a name="API_PolicyDefinition_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cedar **   <a name="bedrockagentcorecontrol-Type-PolicyDefinition-cedar"></a>
The Cedar policy definition within the policy definition structure. This contains the Cedar policy statement that defines the authorization logic using Cedar's human-readable, analyzable policy language. Cedar policies specify principals (who can access), actions (what operations are allowed), resources (what can be accessed), and optional conditions for fine-grained control. Cedar provides a formal policy language designed for authorization with deterministic evaluation, making policies testable, reviewable, and auditable. All Cedar policies follow a default-deny model where actions are denied unless explicitly permitted, and forbid policies always override permit policies.  
Type: [CedarPolicy](API_CedarPolicy.md) object  
Required: No

 ** policy **   <a name="bedrockagentcorecontrol-Type-PolicyDefinition-policy"></a>
An AgentCore policy statement that defines the access control rules. The statement can be a Cedar policy or a guardrails definition.  
Type: [PolicyStatement](API_PolicyStatement.md) object  
Required: No

 ** policyGeneration **   <a name="bedrockagentcorecontrol-Type-PolicyDefinition-policyGeneration"></a>
The generated policy asset information within the policy definition structure. This contains information identifying a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Cedar policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.  
Type: [PolicyGenerationDetails](API_PolicyGenerationDetails.md) object  
Required: No

## See Also
<a name="API_PolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyDefinition) 