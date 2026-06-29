

# PaymentSession
<a name="API_PaymentSession"></a>

A payment session for managing payment transactions.

## Contents
<a name="API_PaymentSession_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-PaymentSession-createdAt"></a>
The timestamp when the session was created.  
Type: Timestamp  
Required: Yes

 ** expiryTimeInMinutes **   <a name="BedrockAgentCore-Type-PaymentSession-expiryTimeInMinutes"></a>
The session expiry time in minutes.  
Type: Integer  
Required: Yes

 ** paymentManagerArn **   <a name="BedrockAgentCore-Type-PaymentSession-paymentManagerArn"></a>
The ARN of the payment manager that owns this session.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`   
Required: Yes

 ** paymentSessionId **   <a name="BedrockAgentCore-Type-PaymentSession-paymentSessionId"></a>
The unique identifier of the payment session.  
Type: String  
Length Constraints: Fixed length of 31.  
Pattern: `payment-session-[0-9a-zA-Z-]{15}`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-PaymentSession-updatedAt"></a>
The timestamp when the session was last updated.  
Type: Timestamp  
Required: Yes

 ** userId **   <a name="BedrockAgentCore-Type-PaymentSession-userId"></a>
The user ID associated with this session.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 120.  
Required: Yes

 ** availableLimits **   <a name="BedrockAgentCore-Type-PaymentSession-availableLimits"></a>
The current available spending limits.  
Type: [AvailableLimits](API_AvailableLimits.md) object  
Required: No

 ** limits **   <a name="BedrockAgentCore-Type-PaymentSession-limits"></a>
The spending limits for the payment session.  
Type: [SessionLimits](API_SessionLimits.md) object  
Required: No

## See Also
<a name="API_PaymentSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentSession) 