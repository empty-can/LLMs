

# HarnessAgentCoreGatewayConfig
<a name="API_HarnessAgentCoreGatewayConfig"></a>

Configuration for AgentCore Gateway.

## Contents
<a name="API_HarnessAgentCoreGatewayConfig_Contents"></a>

 ** gatewayArn **   <a name="BedrockAgentCore-Type-HarnessAgentCoreGatewayConfig-gatewayArn"></a>
The ARN of the desired AgentCore Gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** outboundAuth **   <a name="BedrockAgentCore-Type-HarnessAgentCoreGatewayConfig-outboundAuth"></a>
How harness authenticates to this Gateway. Defaults to AWS\_IAM (SigV4) if omitted.  
Type: [HarnessGatewayOutboundAuth](API_HarnessGatewayOutboundAuth.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_HarnessAgentCoreGatewayConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessAgentCoreGatewayConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessAgentCoreGatewayConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessAgentCoreGatewayConfig) 