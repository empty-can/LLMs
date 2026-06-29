

# GuardrailPiiEntityFilter
<a name="API_agent-runtime_GuardrailPiiEntityFilter"></a>

The Guardrail filter to identify and remove personally identifiable information (PII).

## Contents
<a name="API_agent-runtime_GuardrailPiiEntityFilter_Contents"></a>

 ** action **   <a name="bedrock-Type-agent-runtime_GuardrailPiiEntityFilter-action"></a>
The action of the Guardrail filter to identify and remove PII.  
Type: String  
Valid Values: `BLOCKED | ANONYMIZED`   
Required: No

 ** match **   <a name="bedrock-Type-agent-runtime_GuardrailPiiEntityFilter-match"></a>
The match to settings in the Guardrail filter to identify and remove PII.  
Type: String  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_GuardrailPiiEntityFilter-type"></a>
The type of PII the Guardrail filter has identified and removed.  
Type: String  
Valid Values: `ADDRESS | AGE | AWS_ACCESS_KEY | AWS_SECRET_KEY | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | DRIVER_ID | EMAIL | INTERNATIONAL_BANK_ACCOUNT_NUMBER | IP_ADDRESS | LICENSE_PLATE | MAC_ADDRESS | NAME | PASSWORD | PHONE | PIN | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | URL | USERNAME | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | VEHICLE_IDENTIFICATION_NUMBER`   
Required: No

## See Also
<a name="API_agent-runtime_GuardrailPiiEntityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GuardrailPiiEntityFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GuardrailPiiEntityFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GuardrailPiiEntityFilter) 