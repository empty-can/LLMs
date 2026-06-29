

# WebCrawlerConfiguration
<a name="API_agent_WebCrawlerConfiguration"></a>

The configuration of web URLs that you want to crawl. You should be authorized to crawl the URLs.

## Contents
<a name="API_agent_WebCrawlerConfiguration_Contents"></a>

 ** crawlerLimits **   <a name="bedrock-Type-agent_WebCrawlerConfiguration-crawlerLimits"></a>
The configuration of crawl limits for the web URLs.  
Type: [WebCrawlerLimits](API_agent_WebCrawlerLimits.md) object  
Required: No

 ** exclusionFilters **   <a name="bedrock-Type-agent_WebCrawlerConfiguration-exclusionFilters"></a>
A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** inclusionFilters **   <a name="bedrock-Type-agent_WebCrawlerConfiguration-inclusionFilters"></a>
A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** scope **   <a name="bedrock-Type-agent_WebCrawlerConfiguration-scope"></a>
The scope of what is crawled for your URLs.  
You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL "https://docs.aws.amazon.com/bedrock/latest/userguide/" and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain "aws.amazon.com" can also include sub domain "docs.aws.amazon.com".  
Type: String  
Valid Values: `HOST_ONLY | SUBDOMAINS`   
Required: No

 ** userAgent **   <a name="bedrock-Type-agent_WebCrawlerConfiguration-userAgent"></a>
Returns the user agent suffix for your web crawler.  
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 40.  
Required: No

 ** userAgentHeader **   <a name="bedrock-Type-agent_WebCrawlerConfiguration-userAgentHeader"></a>
A string used for identifying the crawler or bot when it accesses a web server. The user agent header value consists of the `bedrockbot`, UUID, and a user agent suffix for your crawler (if one is provided). By default, it is set to `bedrockbot_UUID`. You can optionally append a custom suffix to `bedrockbot_UUID` to allowlist a specific user agent permitted to access your source URLs.   
Type: String  
Length Constraints: Minimum length of 61. Maximum length of 86.  
Required: No

## See Also
<a name="API_agent_WebCrawlerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/WebCrawlerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/WebCrawlerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/WebCrawlerConfiguration) 