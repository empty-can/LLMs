

# InferenceProviderTargetConfiguration
<a name="API_InferenceProviderTargetConfiguration"></a>

The configuration for a provider-based inference target. This configuration explicitly defines the endpoint, model mapping, and operations used to route requests to a large language model (LLM) provider.

## Contents
<a name="API_InferenceProviderTargetConfiguration_Contents"></a>

 ** endpoint **   <a name="bedrockagentcorecontrol-Type-InferenceProviderTargetConfiguration-endpoint"></a>
The HTTPS endpoint of the inference provider that the gateway forwards requests to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://[a-zA-Z0-9\-\.]+(:[0-9]{1,5})?(/.*)?`   
Required: Yes

 ** modelMapping **   <a name="bedrockagentcorecontrol-Type-InferenceProviderTargetConfiguration-modelMapping"></a>
The configuration that translates client-facing model IDs to the model IDs expected by the provider.  
Type: [ModelMapping](API_ModelMapping.md) object  
Required: No

 ** operations **   <a name="bedrockagentcorecontrol-Type-InferenceProviderTargetConfiguration-operations"></a>
A list of per-operation configurations that map request paths to the models supported for each operation.  
Type: Array of [InferenceOperationConfiguration](API_InferenceOperationConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

## See Also
<a name="API_InferenceProviderTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InferenceProviderTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InferenceProviderTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InferenceProviderTargetConfiguration) 