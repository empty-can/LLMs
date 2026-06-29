

# RerankDocument
<a name="API_agent-runtime_RerankDocument"></a>

Contains information about a document to rerank. Choose the `type` to define and include the field that corresponds to the type.

## Contents
<a name="API_agent-runtime_RerankDocument_Contents"></a>

 ** type **   <a name="bedrock-Type-agent-runtime_RerankDocument-type"></a>
The type of document to rerank.  
Type: String  
Valid Values: `TEXT | JSON`   
Required: Yes

 ** jsonDocument **   <a name="bedrock-Type-agent-runtime_RerankDocument-jsonDocument"></a>
Contains a JSON document to rerank.  
Type: JSON value  
Required: No

 ** textDocument **   <a name="bedrock-Type-agent-runtime_RerankDocument-textDocument"></a>
Contains information about a text document to rerank.  
Type: [RerankTextDocument](API_agent-runtime_RerankTextDocument.md) object  
Required: No

## See Also
<a name="API_agent-runtime_RerankDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RerankDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RerankDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RerankDocument) 