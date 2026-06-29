

# FlowConnectionConfiguration
<a name="API_agent_FlowConnectionConfiguration"></a>

The configuration of the connection.

## Contents
<a name="API_agent_FlowConnectionConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conditional **   <a name="bedrock-Type-agent_FlowConnectionConfiguration-conditional"></a>
The configuration of a connection originating from a Condition node.  
Type: [FlowConditionalConnectionConfiguration](API_agent_FlowConditionalConnectionConfiguration.md) object  
Required: No

 ** data **   <a name="bedrock-Type-agent_FlowConnectionConfiguration-data"></a>
The configuration of a connection originating from a node that isn't a Condition node.  
Type: [FlowDataConnectionConfiguration](API_agent_FlowDataConnectionConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_FlowConnectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowConnectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowConnectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowConnectionConfiguration) 