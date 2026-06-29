

# GuardrailTopicConfig
<a name="API_GuardrailTopicConfig"></a>

Details about topics for the guardrail to identify and deny.

## Contents
<a name="API_GuardrailTopicConfig_Contents"></a>

 ** definition **   <a name="bedrock-Type-GuardrailTopicConfig-definition"></a>
A definition of the topic to deny.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: Yes

 ** name **   <a name="bedrock-Type-GuardrailTopicConfig-name"></a>
The name of the topic to deny.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9a-zA-Z-_ !?.]+`   
Required: Yes

 ** type **   <a name="bedrock-Type-GuardrailTopicConfig-type"></a>
Specifies to deny the topic.  
Type: String  
Valid Values: `DENY`   
Required: Yes

 ** examples **   <a name="bedrock-Type-GuardrailTopicConfig-examples"></a>
A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** inputAction **   <a name="bedrock-Type-GuardrailTopicConfig-inputAction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailTopicConfig-inputEnabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailTopicConfig-outputAction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailTopicConfig-outputEnabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailTopicConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailTopicConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailTopicConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailTopicConfig) 