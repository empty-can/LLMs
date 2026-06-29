

# CustomContent
<a name="API_agent_CustomContent"></a>

Contains information about the content to ingest into a knowledge base connected to a custom data source. Choose a `sourceType` and include the field that corresponds to it.

## Contents
<a name="API_agent_CustomContent_Contents"></a>

 ** customDocumentIdentifier **   <a name="bedrock-Type-agent_CustomContent-customDocumentIdentifier"></a>
A unique identifier for the document.  
Type: [CustomDocumentIdentifier](API_agent_CustomDocumentIdentifier.md) object  
Required: Yes

 ** sourceType **   <a name="bedrock-Type-agent_CustomContent-sourceType"></a>
The source of the data to ingest.  
Type: String  
Valid Values: `IN_LINE | S3_LOCATION`   
Required: Yes

 ** inlineContent **   <a name="bedrock-Type-agent_CustomContent-inlineContent"></a>
Contains information about content defined inline to ingest into a knowledge base.  
Type: [InlineContent](API_agent_InlineContent.md) object  
Required: No

 ** s3Location **   <a name="bedrock-Type-agent_CustomContent-s3Location"></a>
Contains information about the Amazon S3 location of the file from which to ingest data.  
Type: [CustomS3Location](API_agent_CustomS3Location.md) object  
Required: No

## See Also
<a name="API_agent_CustomContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CustomContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CustomContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CustomContent) 