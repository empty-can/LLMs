

# ManagedVpcResource
<a name="API_ManagedVpcResource"></a>

Configuration for a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resource gateway and resource configuration on your behalf using a service-linked role.

## Contents
<a name="API_ManagedVpcResource_Contents"></a>

 ** endpointIpAddressType **   <a name="bedrockagentcorecontrol-Type-ManagedVpcResource-endpointIpAddressType"></a>
The IP address type for the resource configuration endpoint.  
Type: String  
Valid Values: `IPV4 | IPV6`   
Required: Yes

 ** subnetIds **   <a name="bedrockagentcorecontrol-Type-ManagedVpcResource-subnetIds"></a>
The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.  
Type: Array of strings  
Pattern: `subnet-[0-9a-zA-Z]{8,17}`   
Required: Yes

 ** vpcIdentifier **   <a name="bedrockagentcorecontrol-Type-ManagedVpcResource-vpcIdentifier"></a>
The ID of the VPC that contains your private resource.  
Type: String  
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`   
Required: Yes

 ** routingDomain **   <a name="bedrockagentcorecontrol-Type-ManagedVpcResource-routingDomain"></a>
An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain[Route traffic through an intermediate domain].  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Required: No

 ** securityGroupIds **   <a name="bedrockagentcorecontrol-Type-ManagedVpcResource-securityGroupIds"></a>
The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`   
Required: No

 ** tags **   <a name="bedrockagentcorecontrol-Type-ManagedVpcResource-tags"></a>
Tags to apply to the managed VPC Lattice resource gateway.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## See Also
<a name="API_ManagedVpcResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ManagedVpcResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ManagedVpcResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ManagedVpcResource) 