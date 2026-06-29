

# ToolSpecification
<a name="API_runtime_ToolSpecification"></a>

The specification for the tool. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolSpecification_Contents"></a>

 ** inputSchema **   <a name="bedrock-Type-runtime_ToolSpecification-inputSchema"></a>
The input schema for the tool in JSON format.  
Type: [ToolInputSchema](API_runtime_ToolInputSchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrock-Type-runtime_ToolSpecification-name"></a>
The name for the tool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** description **   <a name="bedrock-Type-runtime_ToolSpecification-description"></a>
The description for the tool.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** strict **   <a name="bedrock-Type-runtime_ToolSpecification-strict"></a>
Flag to enable structured output enforcement on a tool usage response.  
Type: Boolean  
Required: No

## See Also
<a name="API_runtime_ToolSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolSpecification) 