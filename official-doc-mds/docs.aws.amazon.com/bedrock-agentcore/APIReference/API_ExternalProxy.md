

# ExternalProxy
<a name="API_ExternalProxy"></a>

Configuration for a customer-managed external proxy server. Includes server location, optional domain-based routing patterns, and authentication credentials.

## Contents
<a name="API_ExternalProxy_Contents"></a>

 ** port **   <a name="BedrockAgentCore-Type-ExternalProxy-port"></a>
The port number of the proxy server. Valid range: 1-65535.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: Yes

 ** server **   <a name="BedrockAgentCore-Type-ExternalProxy-server"></a>
The hostname of the proxy server. Must be a valid DNS hostname (maximum 253 characters).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`   
Required: Yes

 ** credentials **   <a name="BedrockAgentCore-Type-ExternalProxy-credentials"></a>
Optional authentication credentials for the proxy server. If omitted, the proxy is accessed without authentication (useful for IP-allowlisted proxies).  
Type: [ProxyCredentials](API_ProxyCredentials.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** domainPatterns **   <a name="BedrockAgentCore-Type-ExternalProxy-domainPatterns"></a>
Optional array of domain patterns that should route through this specific proxy. Supports `.example.com` for subdomain matching (matches any subdomain of example.com) or `example.com` for exact domain matching. If omitted, this proxy acts as a catch-all for domains not matched by other proxies. Maximum 100 patterns per proxy, each up to 253 characters.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\.)?[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`   
Required: No

## See Also
<a name="API_ExternalProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExternalProxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExternalProxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExternalProxy) 