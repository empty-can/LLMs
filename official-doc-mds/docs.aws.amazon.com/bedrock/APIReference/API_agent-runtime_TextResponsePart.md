

# TextResponsePart
<a name="API_agent-runtime_TextResponsePart"></a>

Contains the part of the generated text that contains a citation, alongside where it begins and ends.

This data type is used in the following API operations:
+  [RetrieveAndGenerate response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax) – in the `textResponsePart` field
+  [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) – in the `textResponsePart` field

## Contents
<a name="API_agent-runtime_TextResponsePart_Contents"></a>

 ** span **   <a name="bedrock-Type-agent-runtime_TextResponsePart-span"></a>
Contains information about where the text with a citation begins and ends in the generated output.  
Type: [Span](API_agent-runtime_Span.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_TextResponsePart-text"></a>
The part of the generated text that contains a citation.  
Type: String  
Required: No

## See Also
<a name="API_agent-runtime_TextResponsePart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/TextResponsePart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/TextResponsePart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/TextResponsePart) 