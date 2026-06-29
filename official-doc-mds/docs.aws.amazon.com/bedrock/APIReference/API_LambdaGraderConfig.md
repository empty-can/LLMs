

# LambdaGraderConfig
<a name="API_LambdaGraderConfig"></a>

 Configuration for using an AWS Lambda function to grade model responses during reinforcement fine-tuning training. 

## Contents
<a name="API_LambdaGraderConfig_Contents"></a>

 ** lambdaArn **   <a name="bedrock-Type-LambdaGraderConfig-lambdaArn"></a>
 ARN of the AWS Lambda function that will evaluate model responses and return reward scores for RFT training.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: Yes

## See Also
<a name="API_LambdaGraderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/LambdaGraderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/LambdaGraderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/LambdaGraderConfig) 