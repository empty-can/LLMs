

# FlowOutputField
<a name="API_agent-runtime_FlowOutputField"></a>

Represents an output field produced by a flow during a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowOutputField_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowOutputField-content"></a>
The content of the output field, which can contain text or structured data.  
Type: [FlowExecutionContent](API_agent-runtime_FlowExecutionContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrock-Type-agent-runtime_FlowOutputField-name"></a>
The name of the output field as defined in the flow's output schema.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

## See Also
<a name="API_agent-runtime_FlowOutputField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowOutputField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowOutputField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowOutputField) 