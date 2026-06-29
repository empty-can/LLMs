

# GuardrailPiiEntityConfig
<a name="API_GuardrailPiiEntityConfig"></a>

The PII entity to configure for the guardrail.

## Contents
<a name="API_GuardrailPiiEntityConfig_Contents"></a>

 ** action **   <a name="bedrock-Type-GuardrailPiiEntityConfig-action"></a>
Configure guardrail action when the PII entity is detected.  
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: Yes

 ** type **   <a name="bedrock-Type-GuardrailPiiEntityConfig-type"></a>
Configure guardrail type when the PII entity is detected.  
The following PIIs are used to block or mask sensitive information:  
+  **General** 
  +  **ADDRESS** 

    A physical address, such as "100 Main Street, Anytown, USA" or "Suite \#12, Building 123". An address can include information such as the street, building, location, city, state, country, county, zip code, precinct, and neighborhood. 
  +  **AGE** 

    An individual's age, including the quantity and unit of time. For example, in the phrase "I am 40 years old," Guardrails recognizes "40 years" as an age. 
  +  **NAME** 

    An individual's name. This entity type does not include titles, such as Dr., Mr., Mrs., or Miss. guardrails doesn't apply this entity type to names that are part of organizations or addresses. For example, guardrails recognizes the "John Doe Organization" as an organization, and it recognizes "Jane Doe Street" as an address. 
  +  **EMAIL** 

    An email address, such as *marymajor@email.com*.
  +  **PHONE** 

    A phone number. This entity type also includes fax and pager numbers. 
  +  **USERNAME** 

    A user name that identifies an account, such as a login name, screen name, nick name, or handle. 
  +  **PASSWORD** 

    An alphanumeric string that is used as a password, such as "\**very20special\#pass\**". 
  +  **DRIVER\_ID** 

    The number assigned to a driver's license, which is an official document permitting an individual to operate one or more motorized vehicles on a public road. A driver's license number consists of alphanumeric characters. 
  +  **LICENSE\_PLATE** 

    A license plate for a vehicle is issued by the state or country where the vehicle is registered. The format for passenger vehicles is typically five to eight digits, consisting of upper-case letters and numbers. The format varies depending on the location of the issuing state or country. 
  +  **VEHICLE\_IDENTIFICATION\_NUMBER** 

    A Vehicle Identification Number (VIN) uniquely identifies a vehicle. VIN content and format are defined in the *ISO 3779* specification. Each country has specific codes and formats for VINs. 
+  **Finance** 
  +  **CREDIT\_DEBIT\_CARD\_CVV** 

    A three-digit card verification code (CVV) that is present on VISA, MasterCard, and Discover credit and debit cards. For American Express credit or debit cards, the CVV is a four-digit numeric code. 
  +  **CREDIT\_DEBIT\_CARD\_EXPIRY** 

    The expiration date for a credit or debit card. This number is usually four digits long and is often formatted as *month/year* or *MM/YY*. Guardrails recognizes expiration dates such as *01/21*, *01/2021*, and *Jan 2021*. 
  +  **CREDIT\_DEBIT\_CARD\_NUMBER** 

    The number for a credit or debit card. These numbers can vary from 13 to 16 digits in length. However, Amazon Comprehend also recognizes credit or debit card numbers when only the last four digits are present. 
  +  **PIN** 

    A four-digit personal identification number (PIN) with which you can access your bank account. 
  +  **INTERNATIONAL\_BANK\_ACCOUNT\_NUMBER** 

    An International Bank Account Number has specific formats in each country. For more information, see [www.iban.com/structure](https://www.iban.com/structure).
  +  **SWIFT\_CODE** 

    A SWIFT code is a standard format of Bank Identifier Code (BIC) used to specify a particular bank or branch. Banks use these codes for money transfers such as international wire transfers.

    SWIFT codes consist of eight or 11 characters. The 11-digit codes refer to specific branches, while eight-digit codes (or 11-digit codes ending in 'XXX') refer to the head or primary office.
+  **IT** 
  +  **IP\_ADDRESS** 

    An IPv4 address, such as *198.51.100.0*. 
  +  **MAC\_ADDRESS** 

    A *media access control* (MAC) address is a unique identifier assigned to a network interface controller (NIC). 
  +  **URL** 

    A web address, such as *www.example.com*. 
  +  **AWS\_ACCESS\_KEY** 

    A unique identifier that's associated with a secret access key; you use the access key ID and secret access key to sign programmatic AWS requests cryptographically. 
  +  **AWS\_SECRET\_KEY** 

    A unique identifier that's associated with an access key. You use the access key ID and secret access key to sign programmatic AWS requests cryptographically. 
+  **USA specific** 
  +  **US\_BANK\_ACCOUNT\_NUMBER** 

    A US bank account number, which is typically 10 to 12 digits long. 
  +  **US\_BANK\_ROUTING\_NUMBER** 

    A US bank account routing number. These are typically nine digits long, 
  +  **US\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER** 

    A US Individual Taxpayer Identification Number (ITIN) is a nine-digit number that starts with a "9" and contain a "7" or "8" as the fourth digit. An ITIN can be formatted with a space or a dash after the third and forth digits. 
  +  **US\_PASSPORT\_NUMBER** 

    A US passport number. Passport numbers range from six to nine alphanumeric characters. 
  +  **US\_SOCIAL\_SECURITY\_NUMBER** 

    A US Social Security Number (SSN) is a nine-digit number that is issued to US citizens, permanent residents, and temporary working residents. 
+  **Canada specific** 
  +  **CA\_HEALTH\_NUMBER** 

    A Canadian Health Service Number is a 10-digit unique identifier, required for individuals to access healthcare benefits. 
  +  **CA\_SOCIAL\_INSURANCE\_NUMBER** 

    A Canadian Social Insurance Number (SIN) is a nine-digit unique identifier, required for individuals to access government programs and benefits.

    The SIN is formatted as three groups of three digits, such as *123-456-789*. A SIN can be validated through a simple check-digit process called the [Luhn algorithm](https://www.wikipedia.org/wiki/Luhn_algorithm).
+  **UK Specific** 
  +  **UK\_NATIONAL\_HEALTH\_SERVICE\_NUMBER** 

    A UK National Health Service Number is a 10-17 digit number, such as *485 777 3456*. The current system formats the 10-digit number with spaces after the third and sixth digits. The final digit is an error-detecting checksum.
  +  **UK\_NATIONAL\_INSURANCE\_NUMBER** 

    A UK National Insurance Number (NINO) provides individuals with access to National Insurance (social security) benefits. It is also used for some purposes in the UK tax system.

    The number is nine digits long and starts with two letters, followed by six numbers and one letter. A NINO can be formatted with a space or a dash after the two letters and after the second, forth, and sixth digits.
  +  **UK\_UNIQUE\_TAXPAYER\_REFERENCE\_NUMBER** 

    A UK Unique Taxpayer Reference (UTR) is a 10-digit number that identifies a taxpayer or a business. 
+  **Custom** 
  +  **Regex filter** - You can use a regular expressions to define patterns for a guardrail to recognize and act upon such as serial number, booking ID etc..
Type: String  
Valid Values: `ADDRESS | AGE | AWS_ACCESS_KEY | AWS_SECRET_KEY | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | DRIVER_ID | EMAIL | INTERNATIONAL_BANK_ACCOUNT_NUMBER | IP_ADDRESS | LICENSE_PLATE | MAC_ADDRESS | NAME | PASSWORD | PHONE | PIN | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | URL | USERNAME | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | VEHICLE_IDENTIFICATION_NUMBER`   
Required: Yes

 ** inputAction **   <a name="bedrock-Type-GuardrailPiiEntityConfig-inputAction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `ANONYMIZE` – Mask the content and replace it with identifier tags.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** inputEnabled **   <a name="bedrock-Type-GuardrailPiiEntityConfig-inputEnabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

 ** outputAction **   <a name="bedrock-Type-GuardrailPiiEntityConfig-outputAction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:  
+  `BLOCK` – Block the content and replace it with blocked messaging.
+  `ANONYMIZE` – Mask the content and replace it with identifier tags.
+  `NONE` – Take no action but return detection information in the trace response.
Type: String  
Valid Values: `BLOCK | ANONYMIZE | NONE`   
Required: No

 ** outputEnabled **   <a name="bedrock-Type-GuardrailPiiEntityConfig-outputEnabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.  
Type: Boolean  
Required: No

## See Also
<a name="API_GuardrailPiiEntityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailPiiEntityConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailPiiEntityConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailPiiEntityConfig) 