

# CodeInterpreterNetworkConfiguration
<a name="API_CodeInterpreterNetworkConfiguration"></a>

The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.

## Contents
<a name="API_CodeInterpreterNetworkConfiguration_Contents"></a>

 ** networkMode **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterNetworkConfiguration-networkMode"></a>
The network mode for the code interpreter. This field specifies how the code interpreter connects to the network.  
Type: String  
Valid Values: `PUBLIC | SANDBOX | VPC`   
Required: Yes

 ** vpcConfig **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterNetworkConfiguration-vpcConfig"></a>
The VPC configuration for the code interpreter. This configuration is required when the network mode is set to `VPC`.  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## See Also
<a name="API_CodeInterpreterNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CodeInterpreterNetworkConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CodeInterpreterNetworkConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CodeInterpreterNetworkConfiguration) 