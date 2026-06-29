

# GuardrailConverseTextBlock
<a name="API_runtime_GuardrailConverseTextBlock"></a>

A text block that contains text that you want to assess with a guardrail. For more information, see [GuardrailConverseContentBlock](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailConverseContentBlock.html).

## Contents
<a name="API_runtime_GuardrailConverseTextBlock_Contents"></a>

 ** text **   <a name="bedrock-Type-runtime_GuardrailConverseTextBlock-text"></a>
The text that you want to guard.  
Type: String  
Required: Yes

 ** qualifiers **   <a name="bedrock-Type-runtime_GuardrailConverseTextBlock-qualifiers"></a>
The qualifier details for the guardrails contextual grounding filter.  
Type: Array of strings  
Valid Values: `grounding_source | query | guard_content`   
Required: No

## See Also
<a name="API_runtime_GuardrailConverseTextBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailConverseTextBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailConverseTextBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailConverseTextBlock) 