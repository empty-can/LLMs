

# GuardrailConverseContentBlock
<a name="API_runtime_GuardrailConverseContentBlock"></a>



A content block for selective guarding with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations. 

## Contents
<a name="API_runtime_GuardrailConverseContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** image **   <a name="bedrock-Type-runtime_GuardrailConverseContentBlock-image"></a>
Image within converse content block to be evaluated by the guardrail.  
Type: [GuardrailConverseImageBlock](API_runtime_GuardrailConverseImageBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-runtime_GuardrailConverseContentBlock-text"></a>
The text to guard.  
Type: [GuardrailConverseTextBlock](API_runtime_GuardrailConverseTextBlock.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailConverseContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailConverseContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailConverseContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailConverseContentBlock) 