

# ContentDeltaEvent
<a name="API_ContentDeltaEvent"></a>

An event that contains incremental output from a command execution. This event streams standard output and standard error content as it becomes available during command execution.

## Contents
<a name="API_ContentDeltaEvent_Contents"></a>

 ** stderr **   <a name="BedrockAgentCore-Type-ContentDeltaEvent-stderr"></a>
The standard error content from the command execution. This field contains the incremental output written to stderr by the executing command.  
Type: String  
Required: No

 ** stdout **   <a name="BedrockAgentCore-Type-ContentDeltaEvent-stdout"></a>
The standard output content from the command execution. This field contains the incremental output written to stdout by the executing command.  
Type: String  
Required: No

## See Also
<a name="API_ContentDeltaEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentDeltaEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentDeltaEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentDeltaEvent) 