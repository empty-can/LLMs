

# MetadataConfiguration
<a name="API_MetadataConfiguration"></a>

Configuration for HTTP header and query parameter propagation between the gateway and target servers.

## Contents
<a name="API_MetadataConfiguration_Contents"></a>

 ** allowedQueryParameters **   <a name="bedrockagentcorecontrol-Type-MetadataConfiguration-allowedQueryParameters"></a>
A list of URL query parameters that are allowed to be propagated from incoming gateway URL to the target.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 40.  
Required: No

 ** allowedRequestHeaders **   <a name="bedrockagentcorecontrol-Type-MetadataConfiguration-allowedRequestHeaders"></a>
A list of HTTP headers that are allowed to be propagated from incoming client requests to the target.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** allowedResponseHeaders **   <a name="bedrockagentcorecontrol-Type-MetadataConfiguration-allowedResponseHeaders"></a>
A list of HTTP headers that are allowed to be propagated from the target response back to the client.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_MetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MetadataConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MetadataConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MetadataConfiguration) 