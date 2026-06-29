

# GuardrailContextualGroundingFilterConfig
<a name="API_GuardrailContextualGroundingFilterConfig"></a>

The filter configuration details for the guardrails contextual grounding filter.

## Contents
<a name="API_GuardrailContextualGroundingFilterConfig_Contents"></a>

 ** threshold **   <a name="bedrock-Type-GuardrailContextualGroundingFilterConfig-threshold"></a>
The threshold details for the guardrails contextual grounding filter.  
Type: Double  
Valid Range: Minimum value of 0.  
Required: Yes

 ** type **   <a name="bedrock-Type-GuardrailContextualGroundingFilterConfig-type"></a>
The filter details for the guardrails contextual grounding filter.  
Type: String  
Valid Values: `GROUNDING | RELEVANCE`   
Required: Yes

 ** action **   <a name="bedrock-Type-GuardrailContextualGroundingFilterConfig-action"></a>
Specifies the action to take when content fails the contextual grounding evaluation. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | NONE`   
Required: No

 ** enabled **   <a name="bedrock-Type-GuardrailContextualGroundingFilterConfig-enabled"></a>
Specifies whether to enable contextual grounding evaluation. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailContextualGroundingFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContextualGroundingFilterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContextualGroundingFilterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContextualGroundingFilterConfig) 