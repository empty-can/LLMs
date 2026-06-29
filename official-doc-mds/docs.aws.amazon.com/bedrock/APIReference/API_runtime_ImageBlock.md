

# ImageBlock
<a name="API_runtime_ImageBlock"></a>

Image content for a message.

## Contents
<a name="API_runtime_ImageBlock_Contents"></a>

 ** format **   <a name="bedrock-Type-runtime_ImageBlock-format"></a>
The format of the image.  
Type: String  
Valid Values: `png | jpeg | gif | webp`   
Required: Yes

 ** source **   <a name="bedrock-Type-runtime_ImageBlock-source"></a>
The source for the image.  
Type: [ImageSource](API_runtime_ImageSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** error **   <a name="bedrock-Type-runtime_ImageBlock-error"></a>
Error information if the image block could not be processed or contains invalid data.  
Type: [ErrorBlock](API_runtime_ErrorBlock.md) object  
Required: No

## See Also
<a name="API_runtime_ImageBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ImageBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ImageBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ImageBlock) 