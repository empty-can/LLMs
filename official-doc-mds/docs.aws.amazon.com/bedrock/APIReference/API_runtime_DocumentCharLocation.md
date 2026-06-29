

# DocumentCharLocation
<a name="API_runtime_DocumentCharLocation"></a>

Specifies a character-level location within a document, providing precise positioning information for cited content using start and end character indices.

## Contents
<a name="API_runtime_DocumentCharLocation_Contents"></a>

 ** documentIndex **   <a name="bedrock-Type-runtime_DocumentCharLocation-documentIndex"></a>
The index of the document within the array of documents provided in the request.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** end **   <a name="bedrock-Type-runtime_DocumentCharLocation-end"></a>
The ending character position of the cited content within the document.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** start **   <a name="bedrock-Type-runtime_DocumentCharLocation-start"></a>
The starting character position of the cited content within the document.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_runtime_DocumentCharLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/DocumentCharLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/DocumentCharLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/DocumentCharLocation) 