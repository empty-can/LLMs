

# HarnessTruncationStrategyConfiguration
<a name="API_HarnessTruncationStrategyConfiguration"></a>

Strategy-specific truncation configuration.

## Contents
<a name="API_HarnessTruncationStrategyConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** slidingWindow **   <a name="bedrockagentcorecontrol-Type-HarnessTruncationStrategyConfiguration-slidingWindow"></a>
Configuration for sliding window truncation.  
Type: [HarnessSlidingWindowConfiguration](API_HarnessSlidingWindowConfiguration.md) object  
Required: No

 ** summarization **   <a name="bedrockagentcorecontrol-Type-HarnessTruncationStrategyConfiguration-summarization"></a>
Configuration for summarization-based truncation.  
Type: [HarnessSummarizationConfiguration](API_HarnessSummarizationConfiguration.md) object  
Required: No

## See Also
<a name="API_HarnessTruncationStrategyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessTruncationStrategyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessTruncationStrategyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessTruncationStrategyConfiguration) 