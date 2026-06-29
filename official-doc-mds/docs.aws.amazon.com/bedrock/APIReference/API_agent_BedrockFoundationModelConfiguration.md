

# BedrockFoundationModelConfiguration
<a name="API_agent_BedrockFoundationModelConfiguration"></a>

Settings for a foundation model used to parse documents for a data source.

## Contents
<a name="API_agent_BedrockFoundationModelConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-agent_BedrockFoundationModelConfiguration-modelArn"></a>
The ARN of the foundation model to use for parsing.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]{1,12})?:(bedrock):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

 ** parsingModality **   <a name="bedrock-Type-agent_BedrockFoundationModelConfiguration-parsingModality"></a>
Specifies whether to enable parsing of multimodal data, including both text and/or images.  
Type: String  
Valid Values: `MULTIMODAL`   
Required: No

 ** parsingPrompt **   <a name="bedrock-Type-agent_BedrockFoundationModelConfiguration-parsingPrompt"></a>
Instructions for interpreting the contents of a document.  
Type: [ParsingPrompt](API_agent_ParsingPrompt.md) object  
Required: No

## See Also
<a name="API_agent_BedrockFoundationModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/BedrockFoundationModelConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/BedrockFoundationModelConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/BedrockFoundationModelConfiguration) 