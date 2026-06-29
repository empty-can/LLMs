

# GuardrailPiiEntityFilter
<a name="API_runtime_GuardrailPiiEntityFilter"></a>

A Personally Identifiable Information (PII) entity configured in a guardrail.

## Contents
<a name="API_runtime_GuardrailPiiEntityFilter_Contents"></a>

 ** action **   <a name="bedrock-Type-runtime_GuardrailPiiEntityFilter-action"></a>
The PII entity filter action.  
Type: String  
Valid Values: `ANONYMIZED | BLOCKED | NONE`   
Required: Yes

 ** match **   <a name="bedrock-Type-runtime_GuardrailPiiEntityFilter-match"></a>
The PII entity filter match.  
Type: String  
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_GuardrailPiiEntityFilter-type"></a>
The PII entity filter type.  
Type: String  
Valid Values: `ADDRESS | AGE | AWS_ACCESS_KEY | AWS_SECRET_KEY | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | DRIVER_ID | EMAIL | INTERNATIONAL_BANK_ACCOUNT_NUMBER | IP_ADDRESS | LICENSE_PLATE | MAC_ADDRESS | NAME | PASSWORD | PHONE | PIN | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | URL | USERNAME | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | VEHICLE_IDENTIFICATION_NUMBER`   
Required: Yes

 ** detected **   <a name="bedrock-Type-runtime_GuardrailPiiEntityFilter-detected"></a>
Indicates whether personally identifiable information (PII) that breaches the guardrail configuration is detected.  
Type: Boolean  
Required: No

## See Also
<a name="API_runtime_GuardrailPiiEntityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailPiiEntityFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailPiiEntityFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailPiiEntityFilter) 