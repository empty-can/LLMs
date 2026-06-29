

# NodeOutputField
<a name="API_agent-runtime_NodeOutputField"></a>

Represents an output field produced by a node during a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_NodeOutputField_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_NodeOutputField-content"></a>
The content of the output field, which can contain text or structured data.  
Type: [NodeExecutionContent](API_agent-runtime_NodeExecutionContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrock-Type-agent-runtime_NodeOutputField-name"></a>
The name of the output field as defined in the node's output schema.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

 ** next **   <a name="bedrock-Type-agent-runtime_NodeOutputField-next"></a>
The next node that receives output data from this field.  
Type: Array of [NodeOutputNext](API_agent-runtime_NodeOutputNext.md) objects  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_NodeOutputField-type"></a>
The data type of the output field for compatibility validation.  
Type: String  
Valid Values: `String | Number | Boolean | Object | Array`   
Required: No

## See Also
<a name="API_agent-runtime_NodeOutputField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/NodeOutputField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/NodeOutputField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/NodeOutputField) 