

# ToolResultBlockDelta
<a name="API_runtime_ToolResultBlockDelta"></a>

Contains incremental updates to tool results information during streaming responses. This allows clients to build up tool results data progressively as the response is generated.

## Contents
<a name="API_runtime_ToolResultBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** json **   <a name="bedrock-Type-runtime_ToolResultBlockDelta-json"></a>
The JSON schema for the tool result content block. see [JSON Schema Reference](https://json-schema.org/understanding-json-schema/reference).  
Type: JSON value  
Required: No

 ** text **   <a name="bedrock-Type-runtime_ToolResultBlockDelta-text"></a>
The reasoning the model used to return the output.  
Type: String  
Required: No

## See Also
<a name="API_runtime_ToolResultBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolResultBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolResultBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolResultBlockDelta) 