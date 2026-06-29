

# VariantResult
<a name="API_VariantResult"></a>

Statistical results for a treatment variant compared against the control.

## Contents
<a name="API_VariantResult_Contents"></a>

 ** isSignificant **   <a name="BedrockAgentCore-Type-VariantResult-isSignificant"></a>
Whether the observed difference is statistically significant.  
Type: Boolean  
Required: Yes

 ** mean **   <a name="BedrockAgentCore-Type-VariantResult-mean"></a>
The mean evaluation score for this variant.  
Type: Double  
Required: Yes

 ** sampleSize **   <a name="BedrockAgentCore-Type-VariantResult-sampleSize"></a>
The number of sessions evaluated for this variant.  
Type: Integer  
Required: Yes

 ** variantName **   <a name="BedrockAgentCore-Type-VariantResult-variantName"></a>
The name of the treatment variant.  
Type: String  
Required: Yes

 ** absoluteChange **   <a name="BedrockAgentCore-Type-VariantResult-absoluteChange"></a>
The absolute change in mean score compared to the control variant.  
Type: Double  
Required: No

 ** confidenceInterval **   <a name="BedrockAgentCore-Type-VariantResult-confidenceInterval"></a>
The confidence interval for the observed difference.  
Type: [ConfidenceInterval](API_ConfidenceInterval.md) object  
Required: No

 ** percentChange **   <a name="BedrockAgentCore-Type-VariantResult-percentChange"></a>
The percentage change in mean score compared to the control variant.  
Type: Double  
Required: No

 ** pValue **   <a name="BedrockAgentCore-Type-VariantResult-pValue"></a>
The p-value indicating the statistical significance of the observed difference.  
Type: Double  
Required: No

## See Also
<a name="API_VariantResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/VariantResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/VariantResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/VariantResult) 