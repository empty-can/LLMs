

# ParsingConfiguration
<a name="API_agent_ParsingConfiguration"></a>

Settings for parsing document contents. If you exclude this field, the default parser converts the contents of each document into text before splitting it into chunks. Specify the parsing strategy to use in the `parsingStrategy` field and include the relevant configuration, or omit it to use the Amazon Bedrock default parser. For more information, see [Parsing options for your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html).

**Note**  
If you specify `BEDROCK_DATA_AUTOMATION` or `BEDROCK_FOUNDATION_MODEL` and it fails to parse a file, the Amazon Bedrock default parser will be used instead.

## Contents
<a name="API_agent_ParsingConfiguration_Contents"></a>

 ** parsingStrategy **   <a name="bedrock-Type-agent_ParsingConfiguration-parsingStrategy"></a>
The parsing strategy for the data source. Only `SMART_PARSING` can be selected for managed knowledge bases. For more information, see [Customize ingestion for managed knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-customize-ingestion.html).  
Type: String  
Valid Values: `BEDROCK_FOUNDATION_MODEL | BEDROCK_DATA_AUTOMATION | SMART_PARSING`   
Required: Yes

 ** bedrockDataAutomationConfiguration **   <a name="bedrock-Type-agent_ParsingConfiguration-bedrockDataAutomationConfiguration"></a>
If you specify `BEDROCK_DATA_AUTOMATION` as the parsing strategy for ingesting your data source, use this object to modify configurations for using the Amazon Bedrock Data Automation parser.  
Type: [BedrockDataAutomationConfiguration](API_agent_BedrockDataAutomationConfiguration.md) object  
Required: No

 ** bedrockFoundationModelConfiguration **   <a name="bedrock-Type-agent_ParsingConfiguration-bedrockFoundationModelConfiguration"></a>
If you specify `BEDROCK_FOUNDATION_MODEL` as the parsing strategy for ingesting your data source, use this object to modify configurations for using a foundation model to parse documents.  
Type: [BedrockFoundationModelConfiguration](API_agent_BedrockFoundationModelConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_ParsingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ParsingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ParsingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ParsingConfiguration) 