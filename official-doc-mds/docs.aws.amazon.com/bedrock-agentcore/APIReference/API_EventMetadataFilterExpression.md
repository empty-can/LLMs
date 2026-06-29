

# EventMetadataFilterExpression
<a name="API_EventMetadataFilterExpression"></a>

Filter expression for retrieving events based on metadata associated with an event.

## Contents
<a name="API_EventMetadataFilterExpression_Contents"></a>

 ** left **   <a name="BedrockAgentCore-Type-EventMetadataFilterExpression-left"></a>
Left operand of the event metadata filter expression.  
Type: [LeftExpression](API_LeftExpression.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** operator **   <a name="BedrockAgentCore-Type-EventMetadataFilterExpression-operator"></a>
Operator applied to the event metadata filter expression.  
Type: String  
Valid Values: `EQUALS_TO | EXISTS | NOT_EXISTS`   
Required: Yes

 ** right **   <a name="BedrockAgentCore-Type-EventMetadataFilterExpression-right"></a>
Right operand of the event metadata filter expression.  
Type: [RightExpression](API_RightExpression.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_EventMetadataFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EventMetadataFilterExpression) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EventMetadataFilterExpression) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EventMetadataFilterExpression) 