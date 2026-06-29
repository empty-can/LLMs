

# StickinessConfiguration
<a name="API_StickinessConfiguration"></a>

The configuration for session-sticky routing to a target. Session stickiness routes requests that share a session identifier to the same target.

## Contents
<a name="API_StickinessConfiguration_Contents"></a>

 ** identifier **   <a name="bedrockagentcorecontrol-Type-StickinessConfiguration-identifier"></a>
The expression that identifies where to extract the session identifier from the request (for example, `$context.header.x-session-id`).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** timeout **   <a name="bedrockagentcorecontrol-Type-StickinessConfiguration-timeout"></a>
The session stickiness timeout, in seconds. After this duration of inactivity, the session affinity expires. Valid values range from 1 to 86400.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 86400.  
Required: No

## See Also
<a name="API_StickinessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/StickinessConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/StickinessConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/StickinessConfiguration) 