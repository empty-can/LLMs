

# ModifyReflectionConfiguration
<a name="API_ModifyReflectionConfiguration"></a>

Contains information for modifying a reflection configuration.

## Contents
<a name="API_ModifyReflectionConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customReflectionConfiguration **   <a name="bedrockagentcorecontrol-Type-ModifyReflectionConfiguration-customReflectionConfiguration"></a>
The updated custom reflection configuration.  
Type: [CustomReflectionConfigurationInput](API_CustomReflectionConfigurationInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** episodicReflectionConfiguration **   <a name="bedrockagentcorecontrol-Type-ModifyReflectionConfiguration-episodicReflectionConfiguration"></a>
The updated episodic reflection configuration.  
Type: [EpisodicReflectionConfigurationInput](API_EpisodicReflectionConfigurationInput.md) object  
Required: No

## See Also
<a name="API_ModifyReflectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ModifyReflectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ModifyReflectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ModifyReflectionConfiguration) 