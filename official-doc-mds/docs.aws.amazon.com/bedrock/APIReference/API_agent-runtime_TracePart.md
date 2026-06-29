

# TracePart
<a name="API_agent-runtime_TracePart"></a>

Contains information about the agent and session, alongside the agent's reasoning process and results from calling API actions and querying knowledge bases and metadata about the trace. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see [Trace enablement](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement).

## Contents
<a name="API_agent-runtime_TracePart_Contents"></a>

 ** agentAliasId **   <a name="bedrock-Type-agent-runtime_TracePart-agentAliasId"></a>
The unique identifier of the alias of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: No

 ** agentId **   <a name="bedrock-Type-agent-runtime_TracePart-agentId"></a>
The unique identifier of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: No

 ** agentVersion **   <a name="bedrock-Type-agent-runtime_TracePart-agentVersion"></a>
The version of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: No

 ** callerChain **   <a name="bedrock-Type-agent-runtime_TracePart-callerChain"></a>
The part's caller chain.  
Type: Array of [Caller](API_agent-runtime_Caller.md) objects  
Required: No

 ** collaboratorName **   <a name="bedrock-Type-agent-runtime_TracePart-collaboratorName"></a>
The part's collaborator name.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** eventTime **   <a name="bedrock-Type-agent-runtime_TracePart-eventTime"></a>
 The time of the trace.   
Type: Timestamp  
Required: No

 ** sessionId **   <a name="bedrock-Type-agent-runtime_TracePart-sessionId"></a>
The unique identifier of the session with the agent.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: No

 ** trace **   <a name="bedrock-Type-agent-runtime_TracePart-trace"></a>
Contains one part of the agent's reasoning process and results from calling API actions and querying knowledge bases. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see [Trace enablement](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement).  
Type: [Trace](API_agent-runtime_Trace.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_agent-runtime_TracePart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/TracePart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/TracePart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/TracePart) 