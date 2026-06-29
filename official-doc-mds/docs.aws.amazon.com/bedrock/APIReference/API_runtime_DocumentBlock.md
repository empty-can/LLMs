

# DocumentBlock
<a name="API_runtime_DocumentBlock"></a>

A document to include in a message.

## Contents
<a name="API_runtime_DocumentBlock_Contents"></a>

 ** name **   <a name="bedrock-Type-runtime_DocumentBlock-name"></a>
A name for the document. The name can only contain the following characters:  
+ Alphanumeric characters
+ Whitespace characters (no more than one in a row)
+ Hyphens
+ Parentheses
+ Square brackets
This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: Yes

 ** source **   <a name="bedrock-Type-runtime_DocumentBlock-source"></a>
Contains the content of the document.  
Type: [DocumentSource](API_runtime_DocumentSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** citations **   <a name="bedrock-Type-runtime_DocumentBlock-citations"></a>
Configuration settings that control how citations should be generated for this specific document.  
Type: [CitationsConfig](API_runtime_CitationsConfig.md) object  
Required: No

 ** context **   <a name="bedrock-Type-runtime_DocumentBlock-context"></a>
Contextual information about how the document should be processed or interpreted by the model when generating citations.  
Type: String  
Required: No

 ** format **   <a name="bedrock-Type-runtime_DocumentBlock-format"></a>
The format of a document, or its extension.  
Type: String  
Valid Values: `pdf | csv | doc | docx | xls | xlsx | html | txt | md`   
Required: No

## See Also
<a name="API_runtime_DocumentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/DocumentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/DocumentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/DocumentBlock) 