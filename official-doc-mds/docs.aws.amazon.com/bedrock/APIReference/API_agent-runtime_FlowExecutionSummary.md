

# FlowExecutionSummary
<a name="API_agent-runtime_FlowExecutionSummary"></a>

Contains summary information about a flow execution, including its status, timestamps, and identifiers.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowExecutionSummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-createdAt"></a>
The timestamp when the flow execution was created.  
Type: Timestamp  
Required: Yes

 ** executionArn **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-executionArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the flow execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})`   
Required: Yes

 ** flowAliasIdentifier **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** flowIdentifier **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-flowIdentifier"></a>
The unique identifier of the flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

 ** flowVersion **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-flowVersion"></a>
The version of the flow used for the execution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-status"></a>
The current status of the flow execution.  
Flow executions time out after 24 hours.  
Type: String  
Valid Values: `Running | Succeeded | Failed | TimedOut | Aborted`   
Required: Yes

 ** endedAt **   <a name="bedrock-Type-agent-runtime_FlowExecutionSummary-endedAt"></a>
The timestamp when the flow execution ended. This field is only populated when the execution has completed, failed, timed out, or been aborted.  
Type: Timestamp  
Required: No

## See Also
<a name="API_agent-runtime_FlowExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowExecutionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowExecutionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowExecutionSummary) 