

# PaymentManagerSummary
<a name="API_PaymentManagerSummary"></a>

Contains summary information about a payment manager.

## Contents
<a name="API_PaymentManagerSummary_Contents"></a>

 ** authorizerType **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-authorizerType"></a>
The type of authorizer used by the payment manager.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: Yes

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-lastUpdatedAt"></a>
The timestamp when the payment manager was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-name"></a>
The name of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9]{0,47}`   
Required: Yes

 ** paymentManagerArn **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-paymentManagerArn"></a>
The Amazon Resource Name (ARN) of the payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** paymentManagerId **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-paymentManagerId"></a>
The unique identifier of the payment manager.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** roleArn **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-status"></a>
The current status of the payment manager. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-createdAt"></a>
The timestamp when the payment manager was created.  
Type: Timestamp  
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-PaymentManagerSummary-description"></a>
The description of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[a-zA-Z0-9\s]+`   
Required: No

## See Also
<a name="API_PaymentManagerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PaymentManagerSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PaymentManagerSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PaymentManagerSummary) 