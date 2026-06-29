

# ToolConfiguration
<a name="API_runtime_ToolConfiguration"></a>

Configuration information for the tools that you pass to a model. For more information, see [Tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolConfiguration_Contents"></a>

 ** tools **   <a name="bedrock-Type-runtime_ToolConfiguration-tools"></a>
An array of tools that you want to pass to a model.   
Type: Array of [Tool](API_runtime_Tool.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

 ** toolChoice **   <a name="bedrock-Type-runtime_ToolConfiguration-toolChoice"></a>
If supported by model, forces the model to request a tool.   
Type: [ToolChoice](API_runtime_ToolChoice.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_runtime_ToolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolConfiguration) 