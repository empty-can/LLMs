

# SemanticChunkingConfiguration
<a name="API_agent_SemanticChunkingConfiguration"></a>

Settings for semantic document chunking for a data source. Semantic chunking splits a document into into smaller documents based on groups of similar content derived from the text with natural language processing.

With semantic chunking, each sentence is compared to the next to determine how similar they are. You specify a threshold in the form of a percentile, where adjacent sentences that are less similar than that percentage of sentence pairs are divided into separate chunks. For example, if you set the threshold to 90, then the 10 percent of sentence pairs that are least similar are split. So if you have 101 sentences, 100 sentence pairs are compared, and the 10 with the least similarity are split, creating 11 chunks. These chunks are further split if they exceed the max token size.

You must also specify a buffer size, which determines whether sentences are compared in isolation, or within a moving context window that includes the previous and following sentence. For example, if you set the buffer size to `1`, the embedding for sentence 10 is derived from sentences 9, 10, and 11 combined.

## Contents
<a name="API_agent_SemanticChunkingConfiguration_Contents"></a>

 ** breakpointPercentileThreshold **   <a name="bedrock-Type-agent_SemanticChunkingConfiguration-breakpointPercentileThreshold"></a>
The dissimilarity threshold for splitting chunks.  
Type: Integer  
Valid Range: Minimum value of 50. Maximum value of 99.  
Required: Yes

 ** bufferSize **   <a name="bedrock-Type-agent_SemanticChunkingConfiguration-bufferSize"></a>
The buffer size.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: Yes

 ** maxTokens **   <a name="bedrock-Type-agent_SemanticChunkingConfiguration-maxTokens"></a>
The maximum number of tokens that a chunk can contain.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 8192.  
Required: Yes

## See Also
<a name="API_agent_SemanticChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SemanticChunkingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SemanticChunkingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SemanticChunkingConfiguration) 