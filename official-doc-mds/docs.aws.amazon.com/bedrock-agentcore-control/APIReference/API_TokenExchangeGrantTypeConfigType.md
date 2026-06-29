

# TokenExchangeGrantTypeConfigType
<a name="API_TokenExchangeGrantTypeConfigType"></a>

Configuration for RFC 8693 token exchange.

## Contents
<a name="API_TokenExchangeGrantTypeConfigType_Contents"></a>

 ** actorTokenContent **   <a name="bedrockagentcorecontrol-Type-TokenExchangeGrantTypeConfigType-actorTokenContent"></a>
The content type for the actor token in the token exchange.  
Type: String  
Valid Values: `NONE | M2M | AWS_IAM_ID_TOKEN_JWT`   
Required: Yes

 ** actorTokenScopes **   <a name="bedrockagentcorecontrol-Type-TokenExchangeGrantTypeConfigType-actorTokenScopes"></a>
The scopes for the actor token. Only valid when actorTokenContent is M2M.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

## See Also
<a name="API_TokenExchangeGrantTypeConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TokenExchangeGrantTypeConfigType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TokenExchangeGrantTypeConfigType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TokenExchangeGrantTypeConfigType) 