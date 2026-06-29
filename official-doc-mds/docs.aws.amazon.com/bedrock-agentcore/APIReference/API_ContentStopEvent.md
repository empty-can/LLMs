

# ContentStopEvent
<a name="API_ContentStopEvent"></a>

An event that signals the completion of a command execution. This event contains the final status and exit code of the executed command.

## Contents
<a name="API_ContentStopEvent_Contents"></a>

 ** exitCode **   <a name="BedrockAgentCore-Type-ContentStopEvent-exitCode"></a>
The exit code returned by the executed command. An exit code of 0 indicates successful execution, -1 indicates a platform error, and values greater than 0 indicate command-specific errors.  
Type: Integer  
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-ContentStopEvent-status"></a>
The final status of the command execution. Valid values are `COMPLETED` for successful completion or `TIMED_OUT` if the command exceeded the specified timeout.  
Type: String  
Valid Values: `COMPLETED | TIMED_OUT`   
Required: Yes

## See Also
<a name="API_ContentStopEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentStopEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentStopEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentStopEvent) 