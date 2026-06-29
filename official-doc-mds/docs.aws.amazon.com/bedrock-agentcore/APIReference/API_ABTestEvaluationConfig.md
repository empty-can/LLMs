

# ABTestEvaluationConfig
<a name="API_ABTestEvaluationConfig"></a>

The evaluation configuration for an A/B test, specifying which online evaluation configurations to use for measuring variant performance.

## Contents
<a name="API_ABTestEvaluationConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-ABTestEvaluationConfig-onlineEvaluationConfigArn"></a>
The Amazon Resource Name (ARN) of a single online evaluation configuration to use for both variants.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: No

 ** perVariantOnlineEvaluationConfig **   <a name="BedrockAgentCore-Type-ABTestEvaluationConfig-perVariantOnlineEvaluationConfig"></a>
Per-variant online evaluation configurations, allowing different evaluation settings for each variant.  
Type: Array of [PerVariantOnlineEvaluationConfig](API_PerVariantOnlineEvaluationConfig.md) objects  
Array Members: Fixed number of 2 items.  
Required: No

## See Also
<a name="API_ABTestEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ABTestEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ABTestEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ABTestEvaluationConfig) 