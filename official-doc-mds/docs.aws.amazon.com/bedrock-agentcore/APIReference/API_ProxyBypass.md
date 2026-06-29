

# ProxyBypass
<a name="API_ProxyBypass"></a>

Configuration for domains that should bypass all proxies and connect directly to the internet. These bypass rules take precedence over all proxy routing rules.

## Contents
<a name="API_ProxyBypass_Contents"></a>

 ** domainPatterns **   <a name="BedrockAgentCore-Type-ProxyBypass-domainPatterns"></a>
Array of domain patterns that should bypass the proxy. Supports `.amazonaws.com` for subdomain matching or `amazonaws.com` for exact domain matching. Requests to these domains connect directly without using any proxy. Maximum 253 characters per pattern.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\.)?[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`   
Required: No

## See Also
<a name="API_ProxyBypass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProxyBypass) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProxyBypass) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProxyBypass) 