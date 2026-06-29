

# PerVariantOnlineEvaluationConfig
<a name="API_PerVariantOnlineEvaluationConfig"></a>

An online evaluation configuration associated with a specific A/B test variant.

## Contents
<a name="API_PerVariantOnlineEvaluationConfig_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-PerVariantOnlineEvaluationConfig-name"></a>
The name of the variant this evaluation configuration applies to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2.  
Pattern: `(C|T1)`   
Required: Yes

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-PerVariantOnlineEvaluationConfig-onlineEvaluationConfigArn"></a>
The Amazon Resource Name (ARN) of the online evaluation configuration for this variant.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## See Also
<a name="API_PerVariantOnlineEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PerVariantOnlineEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PerVariantOnlineEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PerVariantOnlineEvaluationConfig) 