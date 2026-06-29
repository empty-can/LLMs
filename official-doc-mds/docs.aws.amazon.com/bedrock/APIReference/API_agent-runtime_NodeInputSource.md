

# NodeInputSource
<a name="API_agent-runtime_NodeInputSource"></a>

Represents the source of input data for a node field.

## Contents
<a name="API_agent-runtime_NodeInputSource_Contents"></a>

 ** expression **   <a name="bedrock-Type-agent-runtime_NodeInputSource-expression"></a>
The expression used to extract data from the source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_NodeInputSource-nodeName"></a>
The name of the source node that provides the input data.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** outputFieldName **   <a name="bedrock-Type-agent-runtime_NodeInputSource-outputFieldName"></a>
The name of the output field from the source node.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

## See Also
<a name="API_agent-runtime_NodeInputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/NodeInputSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/NodeInputSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/NodeInputSource) 