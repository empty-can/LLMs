

# Oauth2Discovery
<a name="API_Oauth2Discovery"></a>

Contains the discovery information for an OAuth2 provider.

## Contents
<a name="API_Oauth2Discovery_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** authorizationServerMetadata **   <a name="bedrockagentcorecontrol-Type-Oauth2Discovery-authorizationServerMetadata"></a>
The authorization server metadata for the OAuth2 provider.  
Type: [Oauth2AuthorizationServerMetadata](API_Oauth2AuthorizationServerMetadata.md) object  
Required: No

 ** discoveryUrl **   <a name="bedrockagentcorecontrol-Type-Oauth2Discovery-discoveryUrl"></a>
The discovery URL for the OAuth2 provider.  
Type: String  
Pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`   
Required: No

## See Also
<a name="API_Oauth2Discovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Oauth2Discovery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Oauth2Discovery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Oauth2Discovery) 