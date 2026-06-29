

# HarnessGatewayOutboundAuth
<a name="API_HarnessGatewayOutboundAuth"></a>

Authentication method for calling a Gateway.

## Contents
<a name="API_HarnessGatewayOutboundAuth_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsIam **   <a name="BedrockAgentCore-Type-HarnessGatewayOutboundAuth-awsIam"></a>
SigV4-sign requests using the agent's execution role.  
Type: Structure  
Required: No

 ** none **   <a name="BedrockAgentCore-Type-HarnessGatewayOutboundAuth-none"></a>
No authentication.  
Type: Structure  
Required: No

 ** oauth **   <a name="BedrockAgentCore-Type-HarnessGatewayOutboundAuth-oauth"></a>
OAuth 2.0 authentication via AgentCore Identity.  
Type: [OAuthCredentialProvider](API_OAuthCredentialProvider.md) object  
Required: No

## See Also
<a name="API_HarnessGatewayOutboundAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessGatewayOutboundAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessGatewayOutboundAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessGatewayOutboundAuth) 