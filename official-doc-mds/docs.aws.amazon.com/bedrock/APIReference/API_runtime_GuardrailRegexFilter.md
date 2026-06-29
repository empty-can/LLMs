

# GuardrailRegexFilter
<a name="API_runtime_GuardrailRegexFilter"></a>

A Regex filter configured in a guardrail.

## Contents
<a name="API_runtime_GuardrailRegexFilter_Contents"></a>

 ** action **   <a name="bedrock-Type-runtime_GuardrailRegexFilter-action"></a>
The region filter action.  
Type: String  
Valid Values: `ANONYMIZED | BLOCKED | NONE`   
Required: Yes

 ** detected **   <a name="bedrock-Type-runtime_GuardrailRegexFilter-detected"></a>
Indicates whether custom regex entities that breach the guardrail configuration are detected.  
Type: Boolean  
Required: No

 ** match **   <a name="bedrock-Type-runtime_GuardrailRegexFilter-match"></a>
The regesx filter match.  
Type: String  
Required: No

 ** name **   <a name="bedrock-Type-runtime_GuardrailRegexFilter-name"></a>
The regex filter name.  
Type: String  
Required: No

 ** regex **   <a name="bedrock-Type-runtime_GuardrailRegexFilter-regex"></a>
The regex query.  
Type: String  
Required: No

## See Also
<a name="API_runtime_GuardrailRegexFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailRegexFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailRegexFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailRegexFilter) 