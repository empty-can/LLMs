

# FlowConnection
<a name="API_agent_FlowConnection"></a>

Contains information about a connection between two nodes in the flow.

## Contents
<a name="API_agent_FlowConnection_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_FlowConnection-name"></a>
A name for the connection that you can reference.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,100}`   
Required: Yes

 ** source **   <a name="bedrock-Type-agent_FlowConnection-source"></a>
The node that the connection starts at.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** target **   <a name="bedrock-Type-agent_FlowConnection-target"></a>
The node that the connection ends at.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent_FlowConnection-type"></a>
Whether the source node that the connection begins from is a condition node (`Conditional`) or not (`Data`).  
Type: String  
Valid Values: `Data | Conditional`   
Required: Yes

 ** configuration **   <a name="bedrock-Type-agent_FlowConnection-configuration"></a>
The configuration of the connection.  
Type: [FlowConnectionConfiguration](API_agent_FlowConnectionConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_agent_FlowConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowConnection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowConnection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowConnection) 