

# GraderConfig
<a name="API_GraderConfig"></a>

 Configuration for the grader used in reinforcement fine-tuning to evaluate model responses and provide reward signals. 

## Contents
<a name="API_GraderConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** lambdaGrader **   <a name="bedrock-Type-GraderConfig-lambdaGrader"></a>
 Configuration for using an AWS Lambda function as the grader for evaluating model responses and provide reward signals in reinforcement fine-tuning.   
Type: [LambdaGraderConfig](API_LambdaGraderConfig.md) object  
Required: No

## See Also
<a name="API_GraderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GraderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GraderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GraderConfig) 