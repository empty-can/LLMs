

# ProxyConfiguration
<a name="API_ProxyConfiguration"></a>

Configuration for routing browser traffic through customer-managed proxy servers. Supports 1-5 proxy servers for domain-based routing and proxy bypass rules.

## Contents
<a name="API_ProxyConfiguration_Contents"></a>

 ** proxies **   <a name="BedrockAgentCore-Type-ProxyConfiguration-proxies"></a>
An array of 1-5 proxy server configurations for domain-based routing. Each proxy can specify which domains it handles via `domainPatterns`, enabling flexible routing of different traffic through different proxies based on destination domain.  
Type: Array of [Proxy](API_Proxy.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** bypass **   <a name="BedrockAgentCore-Type-ProxyConfiguration-bypass"></a>
Optional configuration for domains that should bypass all proxies and connect directly to their destination, like the internet. Takes precedence over all proxy routing rules.  
Type: [ProxyBypass](API_ProxyBypass.md) object  
Required: No

## See Also
<a name="API_ProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProxyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProxyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProxyConfiguration) 