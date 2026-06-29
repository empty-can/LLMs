

# ByteContentDoc
<a name="API_agent_ByteContentDoc"></a>

Contains information about content defined inline in bytes.

## Contents
<a name="API_agent_ByteContentDoc_Contents"></a>

 ** data **   <a name="bedrock-Type-agent_ByteContentDoc-data"></a>
The base64-encoded string of the content.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 5242880.  
Required: Yes

 ** mimeType **   <a name="bedrock-Type-agent_ByteContentDoc-mimeType"></a>
The MIME type of the content. For a list of MIME types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). The following MIME types are supported:  
+ text/plain
+ text/html
+ text/csv
+ text/vtt
+ message/rfc822
+ application/xhtml\+xml
+ application/pdf
+ application/msword
+ application/vnd.ms-word.document.macroenabled.12
+ application/vnd.ms-word.template.macroenabled.12
+ application/vnd.ms-excel
+ application/vnd.ms-excel.addin.macroenabled.12
+ application/vnd.ms-excel.sheet.macroenabled.12
+ application/vnd.ms-excel.template.macroenabled.12
+ application/vnd.ms-excel.sheet.binary.macroenabled.12
+ application/vnd.ms-spreadsheetml
+ application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
+ application/vnd.openxmlformats-officedocument.spreadsheetml.template
+ application/vnd.openxmlformats-officedocument.wordprocessingml.document
+ application/vnd.openxmlformats-officedocument.wordprocessingml.template
Type: String  
Pattern: `.*[a-z]{1,20}/.{1,20}.*`   
Required: Yes

## See Also
<a name="API_agent_ByteContentDoc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ByteContentDoc) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ByteContentDoc) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ByteContentDoc) 