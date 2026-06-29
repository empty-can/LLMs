

# DocumentContent
<a name="API_agent_DocumentContent"></a>

Contains information about the content of a document. Choose a `dataSourceType` and include the field that corresponds to it.

## Contents
<a name="API_agent_DocumentContent_Contents"></a>

 ** dataSourceType **   <a name="bedrock-Type-agent_DocumentContent-dataSourceType"></a>
The type of data source that is connected to the knowledge base to which to ingest this document.  
Type: String  
Valid Values: `CUSTOM | S3`   
Required: Yes

 ** custom **   <a name="bedrock-Type-agent_DocumentContent-custom"></a>
Contains information about the content to ingest into a knowledge base connected to a custom data source.  
Type: [CustomContent](API_agent_CustomContent.md) object  
Required: No

 ** s3 **   <a name="bedrock-Type-agent_DocumentContent-s3"></a>
Contains information about the content to ingest into a knowledge base connected to an Amazon S3 data source  
Type: [S3Content](API_agent_S3Content.md) object  
Required: No

## See Also
<a name="API_agent_DocumentContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DocumentContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DocumentContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DocumentContent) 