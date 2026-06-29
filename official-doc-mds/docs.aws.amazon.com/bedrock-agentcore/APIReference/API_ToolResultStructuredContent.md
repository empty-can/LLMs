

# ToolResultStructuredContent
<a name="API_ToolResultStructuredContent"></a>

Contains structured content from a tool result.

## Contents
<a name="API_ToolResultStructuredContent_Contents"></a>

 ** executionTime **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-executionTime"></a>
The execution time of the tool operation in milliseconds.  
Type: Double  
Required: No

 ** exitCode **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-exitCode"></a>
The exit code from the tool execution.  
Type: Integer  
Required: No

 ** stderr **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-stderr"></a>
The standard error output from the tool execution.  
Type: String  
Required: No

 ** stdout **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-stdout"></a>
The standard output from the tool execution.  
Type: String  
Required: No

 ** taskId **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-taskId"></a>
The identifier of the task that produced the result.  
Type: String  
Required: No

 ** taskStatus **   <a name="BedrockAgentCore-Type-ToolResultStructuredContent-taskStatus"></a>
The status of the task that produced the result.  
Type: String  
Valid Values: `submitted | working | completed | canceled | failed`   
Required: No

## See Also
<a name="API_ToolResultStructuredContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolResultStructuredContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolResultStructuredContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolResultStructuredContent) 