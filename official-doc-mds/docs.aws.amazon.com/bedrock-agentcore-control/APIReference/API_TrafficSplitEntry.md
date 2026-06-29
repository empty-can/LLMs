

# TrafficSplitEntry
<a name="API_TrafficSplitEntry"></a>

An entry in a traffic split configuration, defining a named variant with a weight and configuration bundle reference.

## Contents
<a name="API_TrafficSplitEntry_Contents"></a>

 ** configurationBundle **   <a name="bedrockagentcorecontrol-Type-TrafficSplitEntry-configurationBundle"></a>
The configuration bundle reference for this variant.  
Type: [ConfigurationBundleReference](API_ConfigurationBundleReference.md) object  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-TrafficSplitEntry-name"></a>
The name of this traffic split variant.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?`   
Required: Yes

 ** weight **   <a name="bedrockagentcorecontrol-Type-TrafficSplitEntry-weight"></a>
The percentage of traffic to route to this variant. Weights across all entries must sum to 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 99.  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-TrafficSplitEntry-description"></a>
The description of this traffic split variant.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** metadata **   <a name="bedrockagentcorecontrol-Type-TrafficSplitEntry-metadata"></a>
Key-value metadata associated with this traffic split variant.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 25 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

## See Also
<a name="API_TrafficSplitEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TrafficSplitEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TrafficSplitEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TrafficSplitEntry) 