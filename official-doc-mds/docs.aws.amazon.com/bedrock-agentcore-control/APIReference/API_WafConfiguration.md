

# WafConfiguration
<a name="API_WafConfiguration"></a>

The AWS WAF configuration for the gateway. This configuration controls how the gateway behaves when the associated web ACL cannot be evaluated.

## Contents
<a name="API_WafConfiguration_Contents"></a>

 ** failureMode **   <a name="bedrockagentcorecontrol-Type-WafConfiguration-failureMode"></a>
The failure mode that determines how the gateway handles requests when AWS WAF is unreachable or times out. Valid values include:  
+  `FAIL_CLOSE` - The gateway blocks requests when AWS WAF cannot be evaluated.
+  `FAIL_OPEN` - The gateway allows requests when AWS WAF cannot be evaluated.
Type: String  
Valid Values: `FAIL_CLOSE | FAIL_OPEN`   
Required: No

## See Also
<a name="API_WafConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/WafConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/WafConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/WafConfiguration) 