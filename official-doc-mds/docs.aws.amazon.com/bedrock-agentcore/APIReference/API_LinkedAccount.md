

# LinkedAccount
<a name="API_LinkedAccount"></a>

Represents different linked accounts that can be linked to an embedded wallet. Supports email, SMS, JWT, and OAuth2 approaches.

## Contents
<a name="API_LinkedAccount_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** developerJwt **   <a name="BedrockAgentCore-Type-LinkedAccount-developerJwt"></a>
Developer JWT linked account with key ID and subject.  
Type: [LinkedAccountDeveloperJwt](API_LinkedAccountDeveloperJwt.md) object  
Required: No

 ** email **   <a name="BedrockAgentCore-Type-LinkedAccount-email"></a>
Email-based linked account.  
Type: [LinkedAccountEmail](API_LinkedAccountEmail.md) object  
Required: No

 ** oAuth2 **   <a name="BedrockAgentCore-Type-LinkedAccount-oAuth2"></a>
OAuth2 provider linked account (Google, Apple, X, Telegram, GitHub).  
Type: [LinkedAccountOAuth2](API_LinkedAccountOAuth2.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** sms **   <a name="BedrockAgentCore-Type-LinkedAccount-sms"></a>
SMS-based linked account using phone number.  
Type: [LinkedAccountSms](API_LinkedAccountSms.md) object  
Required: No

## See Also
<a name="API_LinkedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LinkedAccount) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LinkedAccount) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LinkedAccount) 