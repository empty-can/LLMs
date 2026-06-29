

# ImageInput
<a name="API_agent-runtime_ImageInput"></a>

Details about an image in the result from a function in the action group invocation. You can specify images only when the function is a computer use action. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html).

## Contents
<a name="API_agent-runtime_ImageInput_Contents"></a>

 ** format **   <a name="bedrock-Type-agent-runtime_ImageInput-format"></a>
The type of image in the result.  
Type: String  
Valid Values: `png | jpeg | gif | webp`   
Required: Yes

 ** source **   <a name="bedrock-Type-agent-runtime_ImageInput-source"></a>
The source of the image in the result.  
Type: [ImageInputSource](API_agent-runtime_ImageInputSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_agent-runtime_ImageInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ImageInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ImageInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ImageInput) 