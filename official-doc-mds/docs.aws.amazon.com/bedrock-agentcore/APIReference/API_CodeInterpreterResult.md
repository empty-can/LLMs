

# CodeInterpreterResult
<a name="API_CodeInterpreterResult"></a>

The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore. This structure contains the results of code execution, including textual output, structured data, and error information. Agents use these results to generate responses that incorporate computation, data analysis, and visualization.

## Contents
<a name="API_CodeInterpreterResult_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-CodeInterpreterResult-content"></a>
The textual content of the execution result. This includes standard output from the code execution, such as print statements, console output, and text representations of results.  
Type: Array of [ContentBlock](API_ContentBlock.md) objects  
Required: Yes

 ** isError **   <a name="BedrockAgentCore-Type-CodeInterpreterResult-isError"></a>
Indicates whether the result represents an error. If true, the content contains error messages or exception information. If false, the content contains successful execution results.  
Type: Boolean  
Required: No

 ** structuredContent **   <a name="BedrockAgentCore-Type-CodeInterpreterResult-structuredContent"></a>
The structured content of the execution result. This includes additional metadata about the execution, such as execution time, memory usage, and structured representations of output data. The format depends on the specific code interpreter and execution context.  
Type: [ToolResultStructuredContent](API_ToolResultStructuredContent.md) object  
Required: No

## See Also
<a name="API_CodeInterpreterResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CodeInterpreterResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CodeInterpreterResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CodeInterpreterResult) 