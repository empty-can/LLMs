

# GuardrailContentPolicy
<a name="API_GuardrailContentPolicy"></a>

Contains details about how to handle harmful content.

This data type is used in the following API operations:
+  [GetGuardrail response body](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetGuardrail.html#API_GetGuardrail_ResponseSyntax) 

## Contents
<a name="API_GuardrailContentPolicy_Contents"></a>

 ** filters **   <a name="bedrock-Type-GuardrailContentPolicy-filters"></a>
Contains the type of the content filter and how strongly it should apply to prompts and model responses.  
Type: Array of [GuardrailContentFilter](API_GuardrailContentFilter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 6 items.  
Required: No

 ** tier **   <a name="bedrock-Type-GuardrailContentPolicy-tier"></a>
The tier that your guardrail uses for content filters.  
Type: [GuardrailContentFiltersTier](API_GuardrailContentFiltersTier.md) object  
Required: No

## See Also
<a name="API_GuardrailContentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContentPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContentPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContentPolicy) 