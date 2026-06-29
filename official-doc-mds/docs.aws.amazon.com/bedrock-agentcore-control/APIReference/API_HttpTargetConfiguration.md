

# HttpTargetConfiguration
<a name="API_HttpTargetConfiguration"></a>

The HTTP target configuration for a gateway target. Contains the configuration for HTTP-based target endpoints.

## Contents
<a name="API_HttpTargetConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentcoreRuntime **   <a name="bedrockagentcorecontrol-Type-HttpTargetConfiguration-agentcoreRuntime"></a>
The AgentCore Runtime target configuration for HTTP-based communication with an agent runtime.  
Type: [RuntimeTargetConfiguration](API_RuntimeTargetConfiguration.md) object  
Required: No

 ** passthrough **   <a name="bedrockagentcorecontrol-Type-HttpTargetConfiguration-passthrough"></a>
The passthrough configuration for the HTTP target. A passthrough target forwards requests directly to an external HTTP endpoint.  
Type: [PassthroughTargetConfiguration](API_PassthroughTargetConfiguration.md) object  
Required: No

## See Also
<a name="API_HttpTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HttpTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HttpTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HttpTargetConfiguration) 