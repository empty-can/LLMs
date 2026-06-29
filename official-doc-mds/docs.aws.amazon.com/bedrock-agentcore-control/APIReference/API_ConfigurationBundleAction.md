

# ConfigurationBundleAction
<a name="API_ConfigurationBundleAction"></a>

An action that applies a configuration bundle override, either as a static override or a weighted split for A/B testing.

## Contents
<a name="API_ConfigurationBundleAction_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** staticOverride **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleAction-staticOverride"></a>
A static configuration bundle override that applies a single bundle version to all matching requests.  
Type: [StaticOverride](API_StaticOverride.md) object  
Required: No

 ** weightedOverride **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleAction-weightedOverride"></a>
A weighted configuration bundle override that splits traffic between multiple bundle versions based on configured weights.  
Type: [WeightedOverride](API_WeightedOverride.md) object  
Required: No

## See Also
<a name="API_ConfigurationBundleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConfigurationBundleAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConfigurationBundleAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConfigurationBundleAction) 