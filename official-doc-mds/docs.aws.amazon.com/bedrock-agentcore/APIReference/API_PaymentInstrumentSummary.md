

# PaymentInstrumentSummary
<a name="API_PaymentInstrumentSummary"></a>

Summary of a payment instrument for list operations.

## Contents
<a name="API_PaymentInstrumentSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-createdAt"></a>
The timestamp when this payment instrument was created.  
Type: Timestamp  
Required: Yes

 ** paymentConnectorId **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentConnectorId"></a>
The ID of the payment connector associated with this instrument.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** paymentInstrumentId **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentInstrumentId"></a>
The unique identifier for this payment instrument.  
Type: String  
Length Constraints: Fixed length of 34.  
Pattern: `payment-instrument-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** paymentInstrumentType **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentInstrumentType"></a>
The type of payment instrument (e.g., EMBEDDED\_CRYPTO\_WALLET).  
Type: String  
Valid Values: `EMBEDDED_CRYPTO_WALLET`   
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-paymentManagerArn"></a>
The ARN of the payment manager that owns this payment instrument.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-status"></a>
The current status of this payment instrument.  
Type: String  
Valid Values: `INITIATED | ACTIVE | FAILED | DELETED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-updatedAt"></a>
The timestamp when this payment instrument was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentInstrumentSummary-userId"></a>
The user ID associated with this payment instrument.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

## See Also
<a name="API_PaymentInstrumentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentInstrumentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentInstrumentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentInstrumentSummary) 