

# GuardrailPiiEntity
<a name="API_GuardrailPiiEntity"></a>

The PII entity configured for the guardrail.

## Contents
<a name="API_GuardrailPiiEntity_Contents"></a>

 ** action **   <a name="bedrock-Type-GuardrailPiiEntity-action"></a>
The configured guardrail action when PII entity is detected.  
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: Yes

 ** type **   <a name="bedrock-Type-GuardrailPiiEntity-type"></a>
The type of PII entity. For example, Social Security Number.  
Type: String  
Valid Values: `ADDRESS | AGE | AWS_ACCESS_KEY | AWS_SECRET_KEY | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | DRIVER_ID | EMAIL | INTERNATIONAL_BANK_ACCOUNT_NUMBER | IP_ADDRESS | LICENSE_PLATE | MAC_ADDRESS | NAME | PASSWORD | PHONE | PIN | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | URL | USERNAME | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | VEHICLE_IDENTIFICATION_NUMBER`   
Required: Yes

 ** inputAction **   <a name="bedrock-Type-GuardrailPiiEntity-inputAction"></a>
The action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `ANONYMIZE` – Mask the content and replace it with identifier tags.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailPiiEntity-inputEnabled"></a>
Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailPiiEntity-outputAction"></a>
The action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `ANONYMIZE` – Mask the content and replace it with identifier tags.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailPiiEntity-outputEnabled"></a>
Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailPiiEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailPiiEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailPiiEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailPiiEntity) 