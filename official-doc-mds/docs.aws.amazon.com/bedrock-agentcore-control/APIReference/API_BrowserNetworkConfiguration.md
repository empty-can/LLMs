

# BrowserNetworkConfiguration
<a name="API_BrowserNetworkConfiguration"></a>

The network configuration for a browser. This structure defines how the browser connects to the network.

## Contents
<a name="API_BrowserNetworkConfiguration_Contents"></a>

 ** networkMode **   <a name="bedrockagentcorecontrol-Type-BrowserNetworkConfiguration-networkMode"></a>
The network mode for the browser. This field specifies how the browser connects to the network.  
Type: String  
Valid Values: `PUBLIC | VPC`   
Required: Yes

 ** vpcConfig **   <a name="bedrockagentcorecontrol-Type-BrowserNetworkConfiguration-vpcConfig"></a>
The VPC configuration for the browser. This configuration is required when the network mode is set to `VPC`.  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## See Also
<a name="API_BrowserNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BrowserNetworkConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BrowserNetworkConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BrowserNetworkConfiguration) 