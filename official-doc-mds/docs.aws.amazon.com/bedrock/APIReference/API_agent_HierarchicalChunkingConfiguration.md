

# HierarchicalChunkingConfiguration
<a name="API_agent_HierarchicalChunkingConfiguration"></a>

Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

You configure the number of tokens to overlap, or repeat across adjacent chunks. For example, if you set overlap tokens to 60, the last 60 tokens in the first chunk are also included at the beginning of the second chunk. For each layer, you must also configure the maximum number of tokens in a chunk.

## Contents
<a name="API_agent_HierarchicalChunkingConfiguration_Contents"></a>

 ** levelConfigurations **   <a name="bedrock-Type-agent_HierarchicalChunkingConfiguration-levelConfigurations"></a>
Token settings for each layer.  
Type: Array of [HierarchicalChunkingLevelConfiguration](API_agent_HierarchicalChunkingLevelConfiguration.md) objects  
Array Members: Fixed number of 2 items.  
Required: Yes

 ** overlapTokens **   <a name="bedrock-Type-agent_HierarchicalChunkingConfiguration-overlapTokens"></a>
The number of tokens to repeat across chunks in the same layer.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: Yes

## See Also
<a name="API_agent_HierarchicalChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/HierarchicalChunkingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/HierarchicalChunkingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/HierarchicalChunkingConfiguration) 