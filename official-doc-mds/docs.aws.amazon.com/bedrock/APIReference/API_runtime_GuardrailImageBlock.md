

# GuardrailImageBlock
<a name="API_runtime_GuardrailImageBlock"></a>

Contain an image which user wants guarded. This block is accepted by the guardrails independent API.

## Contents
<a name="API_runtime_GuardrailImageBlock_Contents"></a>

 ** format **   <a name="bedrock-Type-runtime_GuardrailImageBlock-format"></a>
The format details for the file type of the image blocked by the guardrail.  
Type: String  
Valid Values: `png | jpeg`   
Required: Yes

 ** source **   <a name="bedrock-Type-runtime_GuardrailImageBlock-source"></a>
The image source (image bytes) details of the image blocked by the guardrail.  
Type: [GuardrailImageSource](API_runtime_GuardrailImageSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_runtime_GuardrailImageBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailImageBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailImageBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailImageBlock) 