

# DocumentIdentifier
<a name="API_agent_DocumentIdentifier"></a>

Contains information that identifies the document.

## Contents
<a name="API_agent_DocumentIdentifier_Contents"></a>

 ** dataSourceType **   <a name="bedrock-Type-agent_DocumentIdentifier-dataSourceType"></a>
The type of data source connected to the knowledge base that contains the document.  
Type: String  
Valid Values: `CUSTOM | S3`   
Required: Yes

 ** custom **   <a name="bedrock-Type-agent_DocumentIdentifier-custom"></a>
Contains information that identifies the document in a custom data source.  
Type: [CustomDocumentIdentifier](API_agent_CustomDocumentIdentifier.md) object  
Required: No

 ** s3 **   <a name="bedrock-Type-agent_DocumentIdentifier-s3"></a>
Contains information that identifies the document in an S3 data source.  
Type: [S3Location](API_agent_S3Location.md) object  
Required: No

## See Also
<a name="API_agent_DocumentIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DocumentIdentifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DocumentIdentifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DocumentIdentifier) 