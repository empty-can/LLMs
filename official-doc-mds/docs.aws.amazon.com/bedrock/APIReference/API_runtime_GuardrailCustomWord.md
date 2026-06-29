

# GuardrailCustomWord
<a name="API_runtime_GuardrailCustomWord"></a>

A custom word configured in a guardrail.

## Contents
<a name="API_runtime_GuardrailCustomWord_Contents"></a>

 ** action **   <a name="bedrock-Type-runtime_GuardrailCustomWord-action"></a>
The action for the custom word.  
Type: String  
Valid Values: `BLOCKED | NONE`   
Required: Yes

 ** match **   <a name="bedrock-Type-runtime_GuardrailCustomWord-match"></a>
The match for the custom word.  
Type: String  
Required: Yes

 ** detected **   <a name="bedrock-Type-runtime_GuardrailCustomWord-detected"></a>
Indicates whether custom word content that breaches the guardrail configuration is detected.  
Type: Boolean  
Required: No

## See Also
<a name="API_runtime_GuardrailCustomWord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailCustomWord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailCustomWord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailCustomWord) 