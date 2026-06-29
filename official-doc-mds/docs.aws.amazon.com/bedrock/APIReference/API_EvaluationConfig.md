

# EvaluationConfig
<a name="API_EvaluationConfig"></a>

The configuration details of either an automated or human-based evaluation job.

## Contents
<a name="API_EvaluationConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** automated **   <a name="bedrock-Type-EvaluationConfig-automated"></a>
Contains the configuration details of an automated evaluation job that computes metrics.  
Type: [AutomatedEvaluationConfig](API_AutomatedEvaluationConfig.md) object  
Required: No

 ** human **   <a name="bedrock-Type-EvaluationConfig-human"></a>
Contains the configuration details of an evaluation job that uses human workers.  
Type: [HumanEvaluationConfig](API_HumanEvaluationConfig.md) object  
Required: No

## See Also
<a name="API_EvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationConfig) 