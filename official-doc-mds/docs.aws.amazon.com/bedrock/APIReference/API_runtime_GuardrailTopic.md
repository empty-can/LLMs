

# GuardrailTopic
<a name="API_runtime_GuardrailTopic"></a>

Information about a topic guardrail.

## Contents
<a name="API_runtime_GuardrailTopic_Contents"></a>

 ** action **   <a name="bedrock-Type-runtime_GuardrailTopic-action"></a>
The action the guardrail should take when it intervenes on a topic.  
Type: String  
Valid Values: `BLOCKED | NONE`   
Required: Yes

 ** name **   <a name="bedrock-Type-runtime_GuardrailTopic-name"></a>
The name for the guardrail.  
Type: String  
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_GuardrailTopic-type"></a>
The type behavior that the guardrail should perform when the model detects the topic.  
Type: String  
Valid Values: `DENY`   
Required: Yes

 ** detected **   <a name="bedrock-Type-runtime_GuardrailTopic-detected"></a>
Indicates whether topic content that breaches the guardrail configuration is detected.  
Type: Boolean  
Required: No

## See Also
<a name="API_runtime_GuardrailTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailTopic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailTopic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailTopic) 