

# FlowInputField
<a name="API_agent-runtime_FlowInputField"></a>

Represents an input field provided to a flow during a flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Contents
<a name="API_agent-runtime_FlowInputField_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowInputField-content"></a>
The content of the input field, which can contain text or structured data.  
Type: [FlowExecutionContent](API_agent-runtime_FlowExecutionContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** name **   <a name="bedrock-Type-agent-runtime_FlowInputField-name"></a>
The name of the input field as defined in the flow's input schema.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`   
Required: Yes

## See Also
<a name="API_agent-runtime_FlowInputField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowInputField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowInputField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowInputField) 