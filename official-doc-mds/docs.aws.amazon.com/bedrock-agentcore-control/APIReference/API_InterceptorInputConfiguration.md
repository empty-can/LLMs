

# InterceptorInputConfiguration
<a name="API_InterceptorInputConfiguration"></a>

The input configuration of the interceptor.

## Contents
<a name="API_InterceptorInputConfiguration_Contents"></a>

 ** passRequestHeaders **   <a name="bedrockagentcorecontrol-Type-InterceptorInputConfiguration-passRequestHeaders"></a>
Indicates whether to pass request headers as input into the interceptor. When set to true, request headers will be passed.  
Type: Boolean  
Required: Yes

 ** payloadFilter **   <a name="bedrockagentcorecontrol-Type-InterceptorInputConfiguration-payloadFilter"></a>
The filter that determines which parts of the request or response payload are passed as input to the interceptor.  
Type: [InterceptorPayloadFilter](API_InterceptorPayloadFilter.md) object  
Required: No

## See Also
<a name="API_InterceptorInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InterceptorInputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InterceptorInputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InterceptorInputConfiguration) 