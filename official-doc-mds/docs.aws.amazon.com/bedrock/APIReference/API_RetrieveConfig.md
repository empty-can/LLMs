

# RetrieveConfig
<a name="API_RetrieveConfig"></a>

The configuration details for retrieving information from a knowledge base.

## Contents
<a name="API_RetrieveConfig_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-RetrieveConfig-knowledgeBaseId"></a>
The unique identifier of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** knowledgeBaseRetrievalConfiguration **   <a name="bedrock-Type-RetrieveConfig-knowledgeBaseRetrievalConfiguration"></a>
Contains configuration details for knowledge base retrieval.  
Type: [KnowledgeBaseRetrievalConfiguration](API_KnowledgeBaseRetrievalConfiguration.md) object  
Required: Yes

## See Also
<a name="API_RetrieveConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RetrieveConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RetrieveConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RetrieveConfig) 