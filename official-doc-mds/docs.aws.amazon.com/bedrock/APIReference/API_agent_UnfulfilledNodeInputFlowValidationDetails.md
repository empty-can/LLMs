

# UnfulfilledNodeInputFlowValidationDetails
<a name="API_agent_UnfulfilledNodeInputFlowValidationDetails"></a>

Details about an unfulfilled node input with no valid connections.

## Contents
<a name="API_agent_UnfulfilledNodeInputFlowValidationDetails_Contents"></a>

 ** input **   <a name="bedrock-Type-agent_UnfulfilledNodeInputFlowValidationDetails-input"></a>
The name of the unfulfilled input. An input is unfulfilled if there are no data connections to it.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** node **   <a name="bedrock-Type-agent_UnfulfilledNodeInputFlowValidationDetails-node"></a>
The name of the node containing the unfulfilled input.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

## See Also
<a name="API_agent_UnfulfilledNodeInputFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UnfulfilledNodeInputFlowValidationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UnfulfilledNodeInputFlowValidationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UnfulfilledNodeInputFlowValidationDetails) 