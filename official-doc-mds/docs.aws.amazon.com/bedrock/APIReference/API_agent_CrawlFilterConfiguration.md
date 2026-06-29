

# CrawlFilterConfiguration
<a name="API_agent_CrawlFilterConfiguration"></a>

The configuration of filtering the data source content. For example, configuring regular expression patterns to include or exclude certain content.

## Contents
<a name="API_agent_CrawlFilterConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_CrawlFilterConfiguration-type"></a>
The type of filtering that you want to apply to certain objects or content of the data source. For example, the `PATTERN` type is regular expression patterns you can apply to filter your content.  
Type: String  
Valid Values: `PATTERN`   
Required: Yes

 ** patternObjectFilter **   <a name="bedrock-Type-agent_CrawlFilterConfiguration-patternObjectFilter"></a>
The configuration of filtering certain objects or content types of the data source.  
Type: [PatternObjectFilterConfiguration](API_agent_PatternObjectFilterConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_CrawlFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CrawlFilterConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CrawlFilterConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CrawlFilterConfiguration) 