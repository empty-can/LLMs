

# PrivateEndpoint
<a name="API_PrivateEndpoint"></a>

The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.

## Contents
<a name="API_PrivateEndpoint_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** managedVpcResource **   <a name="bedrockagentcorecontrol-Type-PrivateEndpoint-managedVpcResource"></a>
Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.  
Type: [ManagedVpcResource](API_ManagedVpcResource.md) object  
Required: No

 ** selfManagedLatticeResource **   <a name="bedrockagentcorecontrol-Type-PrivateEndpoint-selfManagedLatticeResource"></a>
Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.  
Type: [SelfManagedLatticeResource](API_SelfManagedLatticeResource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_PrivateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PrivateEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PrivateEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PrivateEndpoint) 