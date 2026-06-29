

# AgenticRetrieveResultItem
<a name="API_agent-runtime_AgenticRetrieveResultItem"></a>

A single item from the agentic retrieval results.

## Contents
<a name="API_agent-runtime_AgenticRetrieveResultItem_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveResultItem-content"></a>
The retrieved content.  
Type: [RetrievalContent](API_agent-runtime_RetrievalContent.md) object  
Required: Yes

 ** sourceRetriever **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveResultItem-sourceRetriever"></a>
The source retriever that produced this result.  
Type: [AgenticRetrieveSourceRetriever](API_agent-runtime_AgenticRetrieveSourceRetriever.md) object  
Required: Yes

 ** metadata **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveResultItem-metadata"></a>
Metadata associated with the retrieved item.  
Type: String to JSON value map  
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveResultItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveResultItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveResultItem) 