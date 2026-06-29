

# HarnessMemoryConfiguration
<a name="API_HarnessMemoryConfiguration"></a>

The memory configuration for a harness.

## Contents
<a name="API_HarnessMemoryConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentCoreMemoryConfiguration **   <a name="bedrockagentcorecontrol-Type-HarnessMemoryConfiguration-agentCoreMemoryConfiguration"></a>
The AgentCore Memory configuration.  
Type: [HarnessAgentCoreMemoryConfiguration](API_HarnessAgentCoreMemoryConfiguration.md) object  
Required: No

 ** disabled **   <a name="bedrockagentcorecontrol-Type-HarnessMemoryConfiguration-disabled"></a>
Explicitly opt out of memory.  
Type: [HarnessDisabledMemoryConfiguration](API_HarnessDisabledMemoryConfiguration.md) object  
Required: No

 ** managedMemoryConfiguration **   <a name="bedrockagentcorecontrol-Type-HarnessMemoryConfiguration-managedMemoryConfiguration"></a>
Harness creates and manages a memory resource in the customer's account.  
Type: [HarnessManagedMemoryConfiguration](API_HarnessManagedMemoryConfiguration.md) object  
Required: No

## See Also
<a name="API_HarnessMemoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessMemoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessMemoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessMemoryConfiguration) 