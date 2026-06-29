

# ToolArguments
<a name="API_ToolArguments"></a>

The collection of arguments that specify the operation to perform and its parameters when invoking a tool in Amazon Bedrock AgentCore. Different tools require different arguments, and this structure provides a flexible way to pass the appropriate arguments to each tool type.

## Contents
<a name="API_ToolArguments_Contents"></a>

 ** clearContext **   <a name="BedrockAgentCore-Type-ToolArguments-clearContext"></a>
Whether to clear the context for the tool.  
Type: Boolean  
Required: No

 ** code **   <a name="BedrockAgentCore-Type-ToolArguments-code"></a>
The code to execute in a code interpreter session. This is the source code in the specified programming language that will be executed by the code interpreter.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** command **   <a name="BedrockAgentCore-Type-ToolArguments-command"></a>
The command to execute with the tool.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** content **   <a name="BedrockAgentCore-Type-ToolArguments-content"></a>
The content for the tool operation.  
Type: Array of [InputContentBlock](API_InputContentBlock.md) objects  
Required: No

 ** directoryPath **   <a name="BedrockAgentCore-Type-ToolArguments-directoryPath"></a>
The directory path for the tool operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** language **   <a name="BedrockAgentCore-Type-ToolArguments-language"></a>
The programming language of the code to execute. This tells the code interpreter which language runtime to use for execution.  
Type: String  
Valid Values: `python | javascript | typescript`   
Required: No

 ** path **   <a name="BedrockAgentCore-Type-ToolArguments-path"></a>
The path for the tool operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** paths **   <a name="BedrockAgentCore-Type-ToolArguments-paths"></a>
The paths for the tool operation.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

 ** runtime **   <a name="BedrockAgentCore-Type-ToolArguments-runtime"></a>
The runtime environment to use for code execution. If not specified, defaults to `deno` for JavaScript and TypeScript.  
Type: String  
Valid Values: `nodejs | deno | python`   
Required: No

 ** taskId **   <a name="BedrockAgentCore-Type-ToolArguments-taskId"></a>
The identifier of the task for the tool operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: No

## See Also
<a name="API_ToolArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolArguments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolArguments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolArguments) 