

# LambdaEvaluatorConfig
<a name="API_LambdaEvaluatorConfig"></a>

 Configuration for a Lambda function used as a code-based evaluator. 

## Contents
<a name="API_LambdaEvaluatorConfig_Contents"></a>

 ** lambdaArn **   <a name="bedrockagentcorecontrol-Type-LambdaEvaluatorConfig-lambdaArn"></a>
 The Amazon Resource Name (ARN) of the Lambda function that implements the evaluation logic.   
Type: String  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: Yes

 ** lambdaTimeoutInSeconds **   <a name="bedrockagentcorecontrol-Type-LambdaEvaluatorConfig-lambdaTimeoutInSeconds"></a>
 The timeout in seconds for the Lambda function invocation. Defaults to 60. Must be between 1 and 300.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 300.  
Required: No

## See Also
<a name="API_LambdaEvaluatorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LambdaEvaluatorConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LambdaEvaluatorConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LambdaEvaluatorConfig) 