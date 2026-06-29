

# GuardrailContentFiltersTier
<a name="API_GuardrailContentFiltersTier"></a>

The tier that your guardrail uses for content filters.

## Contents
<a name="API_GuardrailContentFiltersTier_Contents"></a>

 ** tierName **   <a name="bedrock-Type-GuardrailContentFiltersTier-tierName"></a>
The tier that your guardrail uses for content filters. Valid values include:  
+  `CLASSIC` tier – Provides established guardrails functionality supporting English, French, and Spanish languages.
+  `STANDARD` tier – Provides a more robust solution than the `CLASSIC` tier and has more comprehensive language support. This tier requires that your guardrail use [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).
Type: String  
Valid Values: `CLASSIC | STANDARD`   
Required: Yes

## See Also
<a name="API_GuardrailContentFiltersTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContentFiltersTier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContentFiltersTier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContentFiltersTier) 