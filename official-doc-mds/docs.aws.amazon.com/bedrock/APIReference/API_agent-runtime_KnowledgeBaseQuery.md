

# KnowledgeBaseQuery
<a name="API_agent-runtime_KnowledgeBaseQuery"></a>

Contains the query made to the knowledge base.

This data type is used in the following API operations:
+  [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) – in the `retrievalQuery` field

## Contents
<a name="API_agent-runtime_KnowledgeBaseQuery_Contents"></a>

 ** image **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseQuery-image"></a>
An image to include in the knowledge base query for multimodal retrieval.  
Type: [InputImage](API_agent-runtime_InputImage.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseQuery-text"></a>
The text of the query made to the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 20000.  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseQuery-type"></a>
The type of query being performed.  
Type: String  
Valid Values: `TEXT | IMAGE`   
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseQuery) 