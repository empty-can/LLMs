

# ByteContentDoc
<a name="API_ByteContentDoc"></a>

Contains the document contained in the wrapper object, along with its attributes/fields.

## Contents
<a name="API_ByteContentDoc_Contents"></a>

 ** contentType **   <a name="bedrock-Type-ByteContentDoc-contentType"></a>
The MIME type of the document contained in the wrapper object.  
Type: String  
Pattern: `.*[a-z]{1,20}/.{1,20}.*`   
Required: Yes

 ** data **   <a name="bedrock-Type-ByteContentDoc-data"></a>
The byte value of the file to upload, encoded as a Base-64 string.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 10485760.  
Required: Yes

 ** identifier **   <a name="bedrock-Type-ByteContentDoc-identifier"></a>
The file name of the document contained in the wrapper object.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

## See Also
<a name="API_ByteContentDoc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ByteContentDoc) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ByteContentDoc) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ByteContentDoc) 