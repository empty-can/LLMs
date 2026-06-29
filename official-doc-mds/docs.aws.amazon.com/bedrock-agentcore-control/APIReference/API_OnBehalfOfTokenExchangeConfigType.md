

# OnBehalfOfTokenExchangeConfigType
<a name="API_OnBehalfOfTokenExchangeConfigType"></a>

Configuration for on-behalf-of token exchange.

## Contents
<a name="API_OnBehalfOfTokenExchangeConfigType_Contents"></a>

 ** grantType **   <a name="bedrockagentcorecontrol-Type-OnBehalfOfTokenExchangeConfigType-grantType"></a>
The grant type for the on-behalf-of token exchange.  
Type: String  
Valid Values: `TOKEN_EXCHANGE | JWT_AUTHORIZATION_GRANT`   
Required: Yes

 ** tokenExchangeGrantTypeConfig **   <a name="bedrockagentcorecontrol-Type-OnBehalfOfTokenExchangeConfigType-tokenExchangeGrantTypeConfig"></a>
Configuration specific to the TOKEN\_EXCHANGE grant type (RFC 8693).  
Type: [TokenExchangeGrantTypeConfigType](API_TokenExchangeGrantTypeConfigType.md) object  
Required: No

## See Also
<a name="API_OnBehalfOfTokenExchangeConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OnBehalfOfTokenExchangeConfigType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OnBehalfOfTokenExchangeConfigType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OnBehalfOfTokenExchangeConfigType) 