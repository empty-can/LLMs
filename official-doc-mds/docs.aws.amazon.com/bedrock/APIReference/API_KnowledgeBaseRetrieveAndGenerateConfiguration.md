

# KnowledgeBaseRetrieveAndGenerateConfiguration
<a name="API_KnowledgeBaseRetrieveAndGenerateConfiguration"></a>

Contains configuration details for retrieving information from a knowledge base and generating responses.

## Contents
<a name="API_KnowledgeBaseRetrieveAndGenerateConfiguration_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-KnowledgeBaseRetrieveAndGenerateConfiguration-knowledgeBaseId"></a>
The unique identifier of the knowledge base.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** modelArn **   <a name="bedrock-Type-KnowledgeBaseRetrieveAndGenerateConfiguration-modelArn"></a>
The Amazon Resource Name (ARN) of the foundation model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) used to generate responses.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** generationConfiguration **   <a name="bedrock-Type-KnowledgeBaseRetrieveAndGenerateConfiguration-generationConfiguration"></a>
Contains configurations details for response generation based on retrieved text chunks.  
Type: [GenerationConfiguration](API_GenerationConfiguration.md) object  
Required: No

 ** orchestrationConfiguration **   <a name="bedrock-Type-KnowledgeBaseRetrieveAndGenerateConfiguration-orchestrationConfiguration"></a>
Contains configuration details for the model to process the prompt prior to retrieval and response generation.  
Type: [OrchestrationConfiguration](API_OrchestrationConfiguration.md) object  
Required: No

 ** retrievalConfiguration **   <a name="bedrock-Type-KnowledgeBaseRetrieveAndGenerateConfiguration-retrievalConfiguration"></a>
Contains configuration details for retrieving text chunks.  
Type: [KnowledgeBaseRetrievalConfiguration](API_KnowledgeBaseRetrievalConfiguration.md) object  
Required: No

## See Also
<a name="API_KnowledgeBaseRetrieveAndGenerateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/KnowledgeBaseRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/KnowledgeBaseRetrieveAndGenerateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/KnowledgeBaseRetrieveAndGenerateConfiguration) 