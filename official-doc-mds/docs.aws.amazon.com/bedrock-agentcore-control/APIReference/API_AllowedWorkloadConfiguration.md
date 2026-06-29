

# AllowedWorkloadConfiguration
<a name="API_AllowedWorkloadConfiguration"></a>

The configuration that restricts which workloads in the request's identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.

## Contents
<a name="API_AllowedWorkloadConfiguration_Contents"></a>

 ** hostingEnvironments **   <a name="bedrockagentcorecontrol-Type-AllowedWorkloadConfiguration-hostingEnvironments"></a>
The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.  
Type: Array of [HostingEnvironment](API_HostingEnvironment.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** workloadIdentities **   <a name="bedrockagentcorecontrol-Type-AllowedWorkloadConfiguration-workloadIdentities"></a>
The list of workload identities that are allowed to invoke the target.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: No

## See Also
<a name="API_AllowedWorkloadConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AllowedWorkloadConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AllowedWorkloadConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AllowedWorkloadConfiguration) 