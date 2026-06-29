

# GatewayInterceptorConfiguration
<a name="API_GatewayInterceptorConfiguration"></a>

The configuration for an interceptor on a gateway. This structure defines settings for an interceptor that will be invoked during the invocation of the gateway.

## Contents
<a name="API_GatewayInterceptorConfiguration_Contents"></a>

 ** interceptionPoints **   <a name="bedrockagentcorecontrol-Type-GatewayInterceptorConfiguration-interceptionPoints"></a>
The supported points of interception. This field specifies which points during the gateway invocation to invoke the interceptor  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Valid Values: `REQUEST | RESPONSE`   
Required: Yes

 ** interceptor **   <a name="bedrockagentcorecontrol-Type-GatewayInterceptorConfiguration-interceptor"></a>
The infrastructure settings of an interceptor configuration. This structure defines how the interceptor can be invoked.  
Type: [InterceptorConfiguration](API_InterceptorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** inputConfiguration **   <a name="bedrockagentcorecontrol-Type-GatewayInterceptorConfiguration-inputConfiguration"></a>
The configuration for the input of the interceptor. This field specifies how the input to the interceptor is constructed  
Type: [InterceptorInputConfiguration](API_InterceptorInputConfiguration.md) object  
Required: No

## See Also
<a name="API_GatewayInterceptorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GatewayInterceptorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GatewayInterceptorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GatewayInterceptorConfiguration) 