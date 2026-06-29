

# Variant
<a name="API_Variant"></a>

A variant in an A/B test, representing either the control (C) or treatment (T1) configuration.

## Contents
<a name="API_Variant_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-Variant-name"></a>
The name of the variant. Must be `C` for control or `T1` for treatment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2.  
Pattern: `(C|T1)`   
Required: Yes

 ** variantConfiguration **   <a name="BedrockAgentCore-Type-Variant-variantConfiguration"></a>
The configuration for this variant, including the configuration bundle or target reference.  
Type: [VariantConfiguration](API_VariantConfiguration.md) object  
Required: Yes

 ** weight **   <a name="BedrockAgentCore-Type-Variant-weight"></a>
The percentage of traffic to route to this variant. Weights across all variants must sum to 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: Yes

## See Also
<a name="API_Variant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Variant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Variant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Variant) 