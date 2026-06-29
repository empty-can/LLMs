

# InferenceTargetConfiguration
<a name="API_InferenceTargetConfiguration"></a>

The configuration for an inference target. An inference target routes requests to a large language model (LLM) provider, either through a built-in connector or an explicitly configured provider.

## Contents
<a name="API_InferenceTargetConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** connector **   <a name="bedrockagentcorecontrol-Type-InferenceTargetConfiguration-connector"></a>
The connector-based inference configuration. Use this option to route requests to an LLM provider through a built-in connector that includes predefined provider rules.  
Type: [InferenceConnectorTargetConfiguration](API_InferenceConnectorTargetConfiguration.md) object  
Required: No

 ** provider **   <a name="bedrockagentcorecontrol-Type-InferenceTargetConfiguration-provider"></a>
The provider-based inference configuration. Use this option to explicitly configure the endpoint, model mapping, and operations for an LLM provider.  
Type: [InferenceProviderTargetConfiguration](API_InferenceProviderTargetConfiguration.md) object  
Required: No

## See Also
<a name="API_InferenceTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InferenceTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InferenceTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InferenceTargetConfiguration) 