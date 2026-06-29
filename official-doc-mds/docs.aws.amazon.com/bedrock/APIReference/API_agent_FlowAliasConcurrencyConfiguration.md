

# FlowAliasConcurrencyConfiguration
<a name="API_agent_FlowAliasConcurrencyConfiguration"></a>

Determines how multiple nodes in a flow can run in parallel. Running nodes concurrently can improve your flow's performance.

## Contents
<a name="API_agent_FlowAliasConcurrencyConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_FlowAliasConcurrencyConfiguration-type"></a>
The type of concurrency to use for parallel node execution. Specify one of the following options:  
+  `Automatic` - Amazon Bedrock determines which nodes can be executed in parallel based on the flow definition and its dependencies.
+  `Manual` - You specify which nodes can be executed in parallel.
Type: String  
Valid Values: `Automatic | Manual`   
Required: Yes

 ** maxConcurrency **   <a name="bedrock-Type-agent_FlowAliasConcurrencyConfiguration-maxConcurrency"></a>
The maximum number of nodes that can be executed concurrently in the flow.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_agent_FlowAliasConcurrencyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowAliasConcurrencyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowAliasConcurrencyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowAliasConcurrencyConfiguration) 