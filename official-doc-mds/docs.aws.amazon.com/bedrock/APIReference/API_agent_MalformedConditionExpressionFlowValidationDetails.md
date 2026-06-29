

# MalformedConditionExpressionFlowValidationDetails
<a name="API_agent_MalformedConditionExpressionFlowValidationDetails"></a>

Details about a malformed condition expression in a node.

## Contents
<a name="API_agent_MalformedConditionExpressionFlowValidationDetails_Contents"></a>

 ** cause **   <a name="bedrock-Type-agent_MalformedConditionExpressionFlowValidationDetails-cause"></a>
The error message describing why the condition expression is malformed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** condition **   <a name="bedrock-Type-agent_MalformedConditionExpressionFlowValidationDetails-condition"></a>
The name of the malformed condition.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** node **   <a name="bedrock-Type-agent_MalformedConditionExpressionFlowValidationDetails-node"></a>
The name of the node containing the malformed condition expression.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

## See Also
<a name="API_agent_MalformedConditionExpressionFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MalformedConditionExpressionFlowValidationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MalformedConditionExpressionFlowValidationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MalformedConditionExpressionFlowValidationDetails) 