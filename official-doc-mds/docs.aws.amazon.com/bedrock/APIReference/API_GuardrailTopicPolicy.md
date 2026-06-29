

# GuardrailTopicPolicy
<a name="API_GuardrailTopicPolicy"></a>

Contains details about topics that the guardrail should identify and deny.

This data type is used in the following API operations:
+  [GetGuardrail response body](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetGuardrail.html#API_GetGuardrail_ResponseSyntax) 

## Contents
<a name="API_GuardrailTopicPolicy_Contents"></a>

 ** topics **   <a name="bedrock-Type-GuardrailTopicPolicy-topics"></a>
A list of policies related to topics that the guardrail should deny.  
Type: Array of [GuardrailTopic](API_GuardrailTopic.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 30 items.  
Required: Yes

 ** tier **   <a name="bedrock-Type-GuardrailTopicPolicy-tier"></a>
The tier that your guardrail uses for denied topic filters.  
Type: [GuardrailTopicsTier](API_GuardrailTopicsTier.md) object  
Required: No

## See Also
<a name="API_GuardrailTopicPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailTopicPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailTopicPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailTopicPolicy) 