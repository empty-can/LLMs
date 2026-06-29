

# GatewayPolicyEngineConfiguration
<a name="API_GatewayPolicyEngineConfiguration"></a>

The configuration for a policy engine associated with a gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.

## Contents
<a name="API_GatewayPolicyEngineConfiguration_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-GatewayPolicyEngineConfiguration-arn"></a>
The ARN of the policy engine. The policy engine contains Cedar policies that define fine-grained authorization rules specifying who can perform what actions on which resources as agents interact through the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 170.  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:policy-engine\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9_]{10}`   
Required: Yes

 ** mode **   <a name="bedrockagentcorecontrol-Type-GatewayPolicyEngineConfiguration-mode"></a>
The enforcement mode for the policy engine. Valid values include:  
+  `LOG_ONLY` - The policy engine evaluates each action against your policies and adds traces on whether tool calls would be allowed or denied, but does not enforce the decision. Use this mode to test and validate policies before enabling enforcement.
+  `ENFORCE` - The policy engine evaluates actions against your policies and enforces decisions by allowing or denying agent operations. Test and validate policies in `LOG_ONLY` mode before enabling enforcement to avoid unintended denials or adversely affecting production traffic.
Type: String  
Valid Values: `LOG_ONLY | ENFORCE`   
Required: Yes

## See Also
<a name="API_GatewayPolicyEngineConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GatewayPolicyEngineConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GatewayPolicyEngineConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GatewayPolicyEngineConfiguration) 