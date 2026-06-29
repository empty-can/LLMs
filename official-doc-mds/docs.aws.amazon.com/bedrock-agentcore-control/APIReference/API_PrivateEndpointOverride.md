

# PrivateEndpointOverride
<a name="API_PrivateEndpointOverride"></a>

A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.

## Contents
<a name="API_PrivateEndpointOverride_Contents"></a>

 ** domain **   <a name="bedrockagentcorecontrol-Type-PrivateEndpointOverride-domain"></a>
The domain to override with a private endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Required: Yes

 ** privateEndpoint **   <a name="bedrockagentcorecontrol-Type-PrivateEndpointOverride-privateEndpoint"></a>
The private endpoint configuration for the specified domain.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_PrivateEndpointOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PrivateEndpointOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PrivateEndpointOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PrivateEndpointOverride) 