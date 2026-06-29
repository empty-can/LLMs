

# ToolChoice
<a name="API_runtime_ToolChoice"></a>

Determines which tools the model should request in a call to `Converse` or `ConverseStream`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolChoice_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** any **   <a name="bedrock-Type-runtime_ToolChoice-any"></a>
The model must request at least one tool (no text is generated).  
Type: [AnyToolChoice](API_runtime_AnyToolChoice.md) object  
Required: No

 ** auto **   <a name="bedrock-Type-runtime_ToolChoice-auto"></a>
(Default). The Model automatically decides if a tool should be called or whether to generate text instead.   
Type: [AutoToolChoice](API_runtime_AutoToolChoice.md) object  
Required: No

 ** tool **   <a name="bedrock-Type-runtime_ToolChoice-tool"></a>
The Model must request the specified tool. Only supported by Anthropic Claude 3 and Amazon Nova models.   
Type: [SpecificToolChoice](API_runtime_SpecificToolChoice.md) object  
Required: No

## See Also
<a name="API_runtime_ToolChoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolChoice) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolChoice) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolChoice) 