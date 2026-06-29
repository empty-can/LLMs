

# LambdaTransformConfiguration
<a name="API_LambdaTransformConfiguration"></a>

The Lambda configuration for custom transformations. This structure defines the Lambda function that the gateway invokes to transform data.

## Contents
<a name="API_LambdaTransformConfiguration_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-LambdaTransformConfiguration-arn"></a>
The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to transform data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 170.  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: No

## See Also
<a name="API_LambdaTransformConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LambdaTransformConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LambdaTransformConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LambdaTransformConfiguration) 