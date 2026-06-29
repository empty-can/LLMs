

# LambdaFunctionFlowNodeConfiguration
<a name="API_agent_LambdaFunctionFlowNodeConfiguration"></a>

Contains configurations for a Lambda function node in the flow. You specify the Lambda function to invoke and the inputs into the function. The output is the response that is defined in the Lambda function. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_LambdaFunctionFlowNodeConfiguration_Contents"></a>

 ** lambdaArn **   <a name="bedrock-Type-agent_LambdaFunctionFlowNodeConfiguration-lambdaArn"></a>
The Amazon Resource Name (ARN) of the Lambda function to invoke.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `$|^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:lambda:([a-z]{2,}-){2,}\d:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: Yes

## See Also
<a name="API_agent_LambdaFunctionFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/LambdaFunctionFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/LambdaFunctionFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/LambdaFunctionFlowNodeConfiguration) 