

# ActionGroupExecutor
<a name="API_agent_ActionGroupExecutor"></a>

Contains details about the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.

## Contents
<a name="API_agent_ActionGroupExecutor_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customControl **   <a name="bedrock-Type-agent_ActionGroupExecutor-customControl"></a>
To return the action group invocation results directly in the `InvokeAgent` response, specify `RETURN_CONTROL`.  
Type: String  
Valid Values: `RETURN_CONTROL`   
Required: No

 ** lambda **   <a name="bedrock-Type-agent_ActionGroupExecutor-lambda"></a>
The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: No

## See Also
<a name="API_agent_ActionGroupExecutor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ActionGroupExecutor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ActionGroupExecutor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ActionGroupExecutor) 