

# PIIEntitiesConfiguration
<a name="API_data-automation_PIIEntitiesConfiguration"></a>

Configuration for detecting and redacting Personally Identifiable Information (PII) entities. Specify which PII entity types to detect and the redaction mask mode. If not provided, defaults to ALL entity types with ENTITY\_TYPE redaction mask mode.

## Contents
<a name="API_data-automation_PIIEntitiesConfiguration_Contents"></a>

 ** piiEntityTypes **   <a name="bedrock-Type-data-automation_PIIEntitiesConfiguration-piiEntityTypes"></a>
List of PII entity types to detect/redact in the output. Choose from specific entity types (such as ADDRESS, NAME, EMAIL, PHONE, US\_SOCIAL\_SECURITY\_NUMBER) or specify ALL to detect all supported PII types. If not specified, defaults to ALL.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 32 items.  
Valid Values: `ALL | ADDRESS | AGE | NAME | EMAIL | PHONE | USERNAME | PASSWORD | DRIVER_ID | LICENSE_PLATE | VEHICLE_IDENTIFICATION_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | PIN | INTERNATIONAL_BANK_ACCOUNT_NUMBER | SWIFT_CODE | IP_ADDRESS | MAC_ADDRESS | URL | AWS_ACCESS_KEY | AWS_SECRET_KEY | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`   
Required: No

 ** redactionMaskMode **   <a name="bedrock-Type-data-automation_PIIEntitiesConfiguration-redactionMaskMode"></a>
Defines how detected PII entities are masked in redacted output files. Set to PII to replace all detected entities with a generic [PII] marker regardless of entity type. Set to ENTITY\_TYPE to replace each detected entity with its specific type marker (for example, [NAME], [EMAIL], [ADDRESS]). This setting only applies when detectionMode is set to DETECTION\_AND\_REDACTION. If not specified, defaults to ENTITY\_TYPE.  
Type: String  
Valid Values: `PII | ENTITY_TYPE`   
Required: No

## See Also
<a name="API_data-automation_PIIEntitiesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/PIIEntitiesConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/PIIEntitiesConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/PIIEntitiesConfiguration) 