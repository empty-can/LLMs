

# RerankResult
<a name="API_agent-runtime_RerankResult"></a>

Contains information about a document that was reranked.

## Contents
<a name="API_agent-runtime_RerankResult_Contents"></a>

 ** index **   <a name="bedrock-Type-agent-runtime_RerankResult-index"></a>
The original index of the document from the input sources array.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000.  
Required: Yes

 ** relevanceScore **   <a name="bedrock-Type-agent-runtime_RerankResult-relevanceScore"></a>
The relevance score of the document.  
Type: Float  
Required: Yes

 ** document **   <a name="bedrock-Type-agent-runtime_RerankResult-document"></a>
Contains information about the document.  
Type: [RerankDocument](API_agent-runtime_RerankDocument.md) object  
Required: No

## See Also
<a name="API_agent-runtime_RerankResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RerankResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RerankResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RerankResult) 