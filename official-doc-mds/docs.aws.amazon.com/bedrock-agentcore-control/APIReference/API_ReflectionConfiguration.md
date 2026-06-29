

# ReflectionConfiguration
<a name="API_ReflectionConfiguration"></a>

Contains reflection configuration information for a memory strategy.

## Contents
<a name="API_ReflectionConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customReflectionConfiguration **   <a name="bedrockagentcorecontrol-Type-ReflectionConfiguration-customReflectionConfiguration"></a>
The configuration for a custom reflection strategy.  
Type: [CustomReflectionConfiguration](API_CustomReflectionConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** episodicReflectionConfiguration **   <a name="bedrockagentcorecontrol-Type-ReflectionConfiguration-episodicReflectionConfiguration"></a>
The configuration for the episodic reflection strategy.  
Type: [EpisodicReflectionConfiguration](API_EpisodicReflectionConfiguration.md) object  
Required: No

## See Also
<a name="API_ReflectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ReflectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ReflectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ReflectionConfiguration) 