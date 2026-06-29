

# GuardrailContentBlock
<a name="API_runtime_GuardrailContentBlock"></a>

The content block to be evaluated by the guardrail.

## Contents
<a name="API_runtime_GuardrailContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** image **   <a name="bedrock-Type-runtime_GuardrailContentBlock-image"></a>
Image within guardrail content block to be evaluated by the guardrail.  
Type: [GuardrailImageBlock](API_runtime_GuardrailImageBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-runtime_GuardrailContentBlock-text"></a>
Text within content block to be evaluated by the guardrail.  
Type: [GuardrailTextBlock](API_runtime_GuardrailTextBlock.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailContentBlock) 