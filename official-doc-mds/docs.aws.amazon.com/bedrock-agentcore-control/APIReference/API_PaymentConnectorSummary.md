

# PaymentConnectorSummary
<a name="API_PaymentConnectorSummary"></a>

Contains summary information about a payment connector.

## Contents
<a name="API_PaymentConnectorSummary_Contents"></a>

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-PaymentConnectorSummary-lastUpdatedAt"></a>
The timestamp when the payment connector was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PaymentConnectorSummary-name"></a>
The name of the payment connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** paymentConnectorId **   <a name="bedrockagentcorecontrol-Type-PaymentConnectorSummary-paymentConnectorId"></a>
The unique identifier of the payment connector.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PaymentConnectorSummary-status"></a>
The current status of the payment connector. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** type **   <a name="bedrockagentcorecontrol-Type-PaymentConnectorSummary-type"></a>
The type of the payment connector, which determines the payment provider integration.  
Type: String  
Valid Values: `CoinbaseCDP | StripePrivy`   
Required: Yes

## See Also
<a name="API_PaymentConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PaymentConnectorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PaymentConnectorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PaymentConnectorSummary) 