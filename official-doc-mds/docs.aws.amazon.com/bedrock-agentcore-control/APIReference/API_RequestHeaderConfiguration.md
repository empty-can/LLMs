

# RequestHeaderConfiguration
<a name="API_RequestHeaderConfiguration"></a>

Configuration for HTTP request headers that will be passed through to the runtime.

## Contents
<a name="API_RequestHeaderConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** requestHeaderAllowlist **   <a name="bedrockagentcorecontrol-Type-RequestHeaderConfiguration-requestHeaderAllowlist"></a>
A list of HTTP request headers that are allowed to be passed through to the runtime.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[A-Za-z][A-Za-z0-9_-]{0,255}`   
Required: No

## See Also
<a name="API_RequestHeaderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RequestHeaderConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RequestHeaderConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RequestHeaderConfiguration) 