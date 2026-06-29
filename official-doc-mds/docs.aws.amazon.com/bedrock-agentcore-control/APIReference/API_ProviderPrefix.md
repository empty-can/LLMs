

# ProviderPrefix
<a name="API_ProviderPrefix"></a>

The configuration that controls how a provider prefix is applied to model IDs during translation.

## Contents
<a name="API_ProviderPrefix_Contents"></a>

 ** separator **   <a name="bedrockagentcorecontrol-Type-ProviderPrefix-separator"></a>
The single character that separates the provider prefix from the model name (for example, `.`). The default is `.`.  
Type: String  
Length Constraints: Fixed length of 1.  
Required: No

 ** strip **   <a name="bedrockagentcorecontrol-Type-ProviderPrefix-strip"></a>
Whether clients can omit the provider prefix from model IDs. If `true`, the gateway accepts model IDs without the prefix and restores the full prefixed form before forwarding to the provider. The default is `false`.  
Type: Boolean  
Required: No

## See Also
<a name="API_ProviderPrefix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ProviderPrefix) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ProviderPrefix) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ProviderPrefix) 