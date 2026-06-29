

# PaymentSessionSummary
<a name="API_PaymentSessionSummary"></a>

Summary information about a payment session.

## Contents
<a name="API_PaymentSessionSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-createdAt"></a>
The timestamp when the session was created.  
Type: Timestamp  
Required: Yes

 ** expiryTimeInMinutes **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-expiryTimeInMinutes"></a>
The session expiry time in minutes.  
Type: Integer  
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** paymentSessionId **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-paymentSessionId"></a>
The unique identifier of the payment session.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-updatedAt"></a>
The timestamp when the session was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentSessionSummary-userId"></a>
The user ID associated with this session.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

## See Also
<a name="API_PaymentSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentSessionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentSessionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentSessionSummary) 