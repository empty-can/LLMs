

# InferenceOperationConfiguration
<a name="API_InferenceOperationConfiguration"></a>

The configuration for a specific inference operation, including its request path and the models that the operation supports.

## Contents
<a name="API_InferenceOperationConfiguration_Contents"></a>

 ** path **   <a name="bedrockagentcorecontrol-Type-InferenceOperationConfiguration-path"></a>
The request path for this operation (for example, `/v1/messages` or `/v1/responses`).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `/[a-zA-Z0-9\-\._/]+`   
Required: Yes

 ** models **   <a name="bedrockagentcorecontrol-Type-InferenceOperationConfiguration-models"></a>
The list of models supported for this operation.  
Type: Array of [ModelEntry](API_ModelEntry.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** providerPath **   <a name="bedrockagentcorecontrol-Type-InferenceOperationConfiguration-providerPath"></a>
The provider path to forward requests to, if it differs from the request path. For example, `/anthropic/v1/messages` when the provider expects a different path than the client-facing `/v1/messages`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `/[a-zA-Z0-9\-\._/]+`   
Required: No

## See Also
<a name="API_InferenceOperationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InferenceOperationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InferenceOperationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InferenceOperationConfiguration) 