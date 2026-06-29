

# LexFlowNodeConfiguration
<a name="API_agent_LexFlowNodeConfiguration"></a>

Contains configurations for a Lex node in the flow. You specify a Amazon Lex bot to invoke. This node takes an utterance as the input and returns as the output the intent identified by the Amazon Lex bot. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_agent_LexFlowNodeConfiguration_Contents"></a>

 ** botAliasArn **   <a name="bedrock-Type-agent_LexFlowNodeConfiguration-botAliasArn"></a>
The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 78.  
Pattern: `$|^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:lex:([a-z]{2,}-){2,}\d:\d{12}:bot-alias/[0-9a-zA-Z]+/[0-9a-zA-Z]+`   
Required: Yes

 ** localeId **   <a name="bedrock-Type-agent_LexFlowNodeConfiguration-localeId"></a>
The Region to invoke the Amazon Lex bot in.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Required: Yes

## See Also
<a name="API_agent_LexFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/LexFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/LexFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/LexFlowNodeConfiguration) 