

# Conversational
<a name="API_Conversational"></a>

Contains conversational content for an event payload.

## Contents
<a name="API_Conversational_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-Conversational-content"></a>
The content of the conversation message.  
Type: [Content](API_Content.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** role **   <a name="BedrockAgentCore-Type-Conversational-role"></a>
The role of the participant in the conversation (for example, "user" or "assistant").  
Type: String  
Valid Values: `ASSISTANT | USER | TOOL | OTHER`   
Required: Yes

## See Also
<a name="API_Conversational_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Conversational) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Conversational) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Conversational) 