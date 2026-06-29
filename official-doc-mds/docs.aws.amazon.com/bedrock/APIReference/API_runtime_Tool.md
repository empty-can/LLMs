

# Tool
<a name="API_runtime_Tool"></a>

Information about a tool that you can use with the Converse API. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_Tool_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cachePoint **   <a name="bedrock-Type-runtime_Tool-cachePoint"></a>
CachePoint to include in the tool configuration.  
Type: [CachePointBlock](API_runtime_CachePointBlock.md) object  
Required: No

 ** systemTool **   <a name="bedrock-Type-runtime_Tool-systemTool"></a>
Specifies the system-defined tool that you want use.  
Type: [SystemTool](API_runtime_SystemTool.md) object  
Required: No

 ** toolSpec **   <a name="bedrock-Type-runtime_Tool-toolSpec"></a>
The specfication for the tool.   
Type: [ToolSpecification](API_runtime_ToolSpecification.md) object  
Required: No

## See Also
<a name="API_runtime_Tool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/Tool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/Tool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/Tool) 