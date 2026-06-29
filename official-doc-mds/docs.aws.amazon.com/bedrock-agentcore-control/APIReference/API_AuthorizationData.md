

# AuthorizationData
<a name="API_AuthorizationData"></a>

Contains the authorization data that is returned when a gateway target is configured with a credential provider with authorization code grant type and requires user federation.

## Contents
<a name="API_AuthorizationData_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** oauth2 **   <a name="bedrockagentcorecontrol-Type-AuthorizationData-oauth2"></a>
OAuth2 authorization data for the gateway target.  
Type: [OAuth2AuthorizationData](API_OAuth2AuthorizationData.md) object  
Required: No

## See Also
<a name="API_AuthorizationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AuthorizationData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AuthorizationData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AuthorizationData) 