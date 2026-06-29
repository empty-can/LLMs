

# Message
<a name="API_runtime_Message"></a>

A message input, or returned from, a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html).

## Contents
<a name="API_runtime_Message_Contents"></a>

 ** content **   <a name="bedrock-Type-runtime_Message-content"></a>
The message content. Note the following restrictions:  
+ You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.
+ You can include up to five documents. Each document's size must be no more than 4.5 MB.
+ If you include a `ContentBlock` with a `document` field in the array, you must also include a `ContentBlock` with a `text` field.
+ You can only include images and documents if the `role` is `user`.
Type: Array of [ContentBlock](API_runtime_ContentBlock.md) objects  
Required: Yes

 ** role **   <a name="bedrock-Type-runtime_Message-role"></a>
The role that the message plays in the message.  
Type: String  
Valid Values: `user | assistant`   
Required: Yes

## See Also
<a name="API_runtime_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/Message) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/Message) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/Message) 