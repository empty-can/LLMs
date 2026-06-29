

# InlineContent
<a name="API_agent_InlineContent"></a>

Contains information about content defined inline to ingest into a data source. Choose a `type` and include the field that corresponds to it.

## Contents
<a name="API_agent_InlineContent_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_InlineContent-type"></a>
The type of inline content to define.  
Type: String  
Valid Values: `BYTE | TEXT`   
Required: Yes

 ** byteContent **   <a name="bedrock-Type-agent_InlineContent-byteContent"></a>
Contains information about content defined inline in bytes.  
Type: [ByteContentDoc](API_agent_ByteContentDoc.md) object  
Required: No

 ** textContent **   <a name="bedrock-Type-agent_InlineContent-textContent"></a>
Contains information about content defined inline in text.  
Type: [TextContentDoc](API_agent_TextContentDoc.md) object  
Required: No

## See Also
<a name="API_agent_InlineContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/InlineContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/InlineContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/InlineContent) 