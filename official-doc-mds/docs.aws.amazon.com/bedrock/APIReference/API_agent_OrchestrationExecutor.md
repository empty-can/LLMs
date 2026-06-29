

# OrchestrationExecutor
<a name="API_agent_OrchestrationExecutor"></a>

 Contains details about the Lambda function containing the orchestration logic carried out upon invoking the custom orchestration. 

## Contents
<a name="API_agent_OrchestrationExecutor_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** lambda **   <a name="bedrock-Type-agent_OrchestrationExecutor-lambda"></a>
 The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: No

## See Also
<a name="API_agent_OrchestrationExecutor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/OrchestrationExecutor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/OrchestrationExecutor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/OrchestrationExecutor) 