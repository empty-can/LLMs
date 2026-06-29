

# VpcConfig
<a name="API_VpcConfig"></a>

VpcConfig for the Agent.

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** securityGroups **   <a name="bedrockagentcorecontrol-Type-VpcConfig-securityGroups"></a>
The security groups associated with the VPC configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Pattern: `sg-[0-9a-zA-Z]{8,17}`   
Required: Yes

 ** subnets **   <a name="bedrockagentcorecontrol-Type-VpcConfig-subnets"></a>
The subnets associated with the VPC configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Pattern: `subnet-[0-9a-zA-Z]{8,17}`   
Required: Yes

 ** requireServiceS3Endpoint **   <a name="bedrockagentcorecontrol-Type-VpcConfig-requireServiceS3Endpoint"></a>
This field applies only to Agent Runtimes. It is not applicable to Browsers or Code Interpreters.
Controls whether a service-managed Amazon S3 gateway endpoint is provisioned in the VPC network topology for the agent runtime. This gateway is used by Amazon Bedrock AgentCore Runtime to download code and container images during agent startup.  
Starting May 5, 2026, Amazon Bedrock AgentCore Runtime is gradually rolling out a change to how network isolation is configured for VPC mode agents. Agent runtimes created on or after this rollout will no longer include the service-managed Amazon S3 gateway. Instead, all network access, including to Amazon S3, is governed exclusively by your VPC configuration. This field cannot be set on agent runtimes created after the rollout. Passing this field in an `UpdateAgentRuntime` request for these agent runtimes returns a `ValidationException`.  
Agent runtimes created before the rollout are not affected and continue to operate with the service-managed Amazon S3 gateway. To enforce full VPC network isolation on these existing agent runtimes, set this field to `false` via the `UpdateAgentRuntime` API. Before opting out, ensure your VPC provides the Amazon S3 access required for agent startup. If this field is not specified or is set to `true`, the service-managed Amazon S3 gateway remains provisioned.  
This field is only supported in the `UpdateAgentRuntime` API for pre-rollout agent runtimes. Passing this field in a `CreateAgentRuntime` request returns a `ValidationException`.  
Type: Boolean  
Required: No

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/VpcConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/VpcConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/VpcConfig) 