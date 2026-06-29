

# InvalidLoopBoundaryFlowValidationDetails
<a name="API_agent_InvalidLoopBoundaryFlowValidationDetails"></a>

Details about a flow that contains connections that violate loop boundary rules.

## Contents
<a name="API_agent_InvalidLoopBoundaryFlowValidationDetails_Contents"></a>

 ** connection **   <a name="bedrock-Type-agent_InvalidLoopBoundaryFlowValidationDetails-connection"></a>
The name of the connection that violates loop boundary rules.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,100}`   
Required: Yes

 ** source **   <a name="bedrock-Type-agent_InvalidLoopBoundaryFlowValidationDetails-source"></a>
The source node of the connection that violates DoWhile loop boundary rules.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** target **   <a name="bedrock-Type-agent_InvalidLoopBoundaryFlowValidationDetails-target"></a>
The target node of the connection that violates DoWhile loop boundary rules.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

## See Also
<a name="API_agent_InvalidLoopBoundaryFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/InvalidLoopBoundaryFlowValidationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/InvalidLoopBoundaryFlowValidationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/InvalidLoopBoundaryFlowValidationDetails) 