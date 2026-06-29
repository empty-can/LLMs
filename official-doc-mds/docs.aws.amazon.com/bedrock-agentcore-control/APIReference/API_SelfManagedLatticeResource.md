

# SelfManagedLatticeResource
<a name="API_SelfManagedLatticeResource"></a>

Configuration for a self-managed VPC Lattice resource. You create and manage the VPC Lattice resource gateway and resource configuration, then provide the resource configuration identifier.

## Contents
<a name="API_SelfManagedLatticeResource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** resourceConfigurationIdentifier **   <a name="bedrockagentcorecontrol-Type-SelfManagedLatticeResource-resourceConfigurationIdentifier"></a>
The ARN or ID of the VPC Lattice resource configuration.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`   
Required: No

## See Also
<a name="API_SelfManagedLatticeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SelfManagedLatticeResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SelfManagedLatticeResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SelfManagedLatticeResource) 