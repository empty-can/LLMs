

# McpLambdaTargetConfiguration
<a name="API_McpLambdaTargetConfiguration"></a>

The Lambda configuration for a Model Context Protocol target. This structure defines how the gateway uses a Lambda function to communicate with the target.

## Contents
<a name="API_McpLambdaTargetConfiguration_Contents"></a>

 ** lambdaArn **   <a name="bedrockagentcorecontrol-Type-McpLambdaTargetConfiguration-lambdaArn"></a>
The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to communicate with the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 170.  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: Yes

 ** toolSchema **   <a name="bedrockagentcorecontrol-Type-McpLambdaTargetConfiguration-toolSchema"></a>
The tool schema for the Lambda function. This schema defines the structure of the tools that the Lambda function provides.  
Type: [ToolSchema](API_ToolSchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_McpLambdaTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/McpLambdaTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/McpLambdaTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/McpLambdaTargetConfiguration) 