

# ManagedResourceDetails
<a name="API_ManagedResourceDetails"></a>

Details of a resource created and managed by the gateway for private endpoint connectivity.

## Contents
<a name="API_ManagedResourceDetails_Contents"></a>

 ** domain **   <a name="bedrockagentcorecontrol-Type-ManagedResourceDetails-domain"></a>
The domain associated with this managed resource.  
Type: String  
Required: No

 ** resourceAssociationArn **   <a name="bedrockagentcorecontrol-Type-ManagedResourceDetails-resourceAssociationArn"></a>
The ARN of the service network resource association.  
Type: String  
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}`   
Required: No

 ** resourceGatewayArn **   <a name="bedrockagentcorecontrol-Type-ManagedResourceDetails-resourceGatewayArn"></a>
The ARN of the VPC Lattice resource gateway created in your account.  
Type: String  
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`   
Required: No

## See Also
<a name="API_ManagedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ManagedResourceDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ManagedResourceDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ManagedResourceDetails) 