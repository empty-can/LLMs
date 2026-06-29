

# CitationsContentBlock
<a name="API_runtime_CitationsContentBlock"></a>

A content block that contains both generated text and associated citation information. This block type is returned when document citations are enabled, providing traceability between the generated content and the source documents that informed the response.

## Contents
<a name="API_runtime_CitationsContentBlock_Contents"></a>

 ** citations **   <a name="bedrock-Type-runtime_CitationsContentBlock-citations"></a>
An array of citations that reference the source documents used to generate the associated content.  
Type: Array of [Citation](API_runtime_Citation.md) objects  
Required: No

 ** content **   <a name="bedrock-Type-runtime_CitationsContentBlock-content"></a>
The generated content that is supported by the associated citations.  
Type: Array of [CitationGeneratedContent](API_runtime_CitationGeneratedContent.md) objects  
Required: No

## See Also
<a name="API_runtime_CitationsContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CitationsContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CitationsContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CitationsContentBlock) 