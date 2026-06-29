

# MismatchedNodeOutputTypeFlowValidationDetails
<a name="API_agent_MismatchedNodeOutputTypeFlowValidationDetails"></a>

Details about mismatched output data types in a node.

## Contents
<a name="API_agent_MismatchedNodeOutputTypeFlowValidationDetails_Contents"></a>

 ** expectedType **   <a name="bedrock-Type-agent_MismatchedNodeOutputTypeFlowValidationDetails-expectedType"></a>
The expected data type for the node output.  
Type: String  
Valid Values: `String | Number | Boolean | Object | Array`   
Required: Yes

 ** node **   <a name="bedrock-Type-agent_MismatchedNodeOutputTypeFlowValidationDetails-node"></a>
The name of the node containing the output with the mismatched data type.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** output **   <a name="bedrock-Type-agent_MismatchedNodeOutputTypeFlowValidationDetails-output"></a>
The name of the output with the mismatched data type.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

## See Also
<a name="API_agent_MismatchedNodeOutputTypeFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MismatchedNodeOutputTypeFlowValidationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MismatchedNodeOutputTypeFlowValidationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MismatchedNodeOutputTypeFlowValidationDetails) 