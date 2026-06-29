

# FixedSizeChunkingConfiguration
<a name="API_agent_FixedSizeChunkingConfiguration"></a>

Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.

## Contents
<a name="API_agent_FixedSizeChunkingConfiguration_Contents"></a>

 ** maxTokens **   <a name="bedrock-Type-agent_FixedSizeChunkingConfiguration-maxTokens"></a>
The maximum number of tokens to include in a chunk.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 8192.  
Required: Yes

 ** overlapPercentage **   <a name="bedrock-Type-agent_FixedSizeChunkingConfiguration-overlapPercentage"></a>
The percentage of overlap between adjacent chunks of a data source.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 99.  
Required: Yes

## See Also
<a name="API_agent_FixedSizeChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FixedSizeChunkingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FixedSizeChunkingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FixedSizeChunkingConfiguration) 