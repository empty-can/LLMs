

# PromptOverrideConfiguration
<a name="API_agent_PromptOverrideConfiguration"></a>

Contains configurations to override prompts in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).

## Contents
<a name="API_agent_PromptOverrideConfiguration_Contents"></a>

 ** promptConfigurations **   <a name="bedrock-Type-agent_PromptOverrideConfiguration-promptConfigurations"></a>
Contains configurations to override a prompt template in one part of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).  
Type: Array of [PromptConfiguration](API_agent_PromptConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: Yes

 ** overrideLambda **   <a name="bedrock-Type-agent_PromptOverrideConfiguration-overrideLambda"></a>
The ARN of the Lambda function to use when parsing the raw foundation model output in parts of the agent sequence. If you specify this field, at least one of the `promptConfigurations` must contain a `parserMode` value that is set to `OVERRIDDEN`. For more information, see [Parser Lambda function in Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/lambda-parser.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`   
Required: No

## See Also
<a name="API_agent_PromptOverrideConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptOverrideConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptOverrideConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptOverrideConfiguration) 