

# CustomJWTAuthorizerConfiguration
<a name="API_CustomJWTAuthorizerConfiguration"></a>

Configuration for inbound JWT-based authorization, specifying how incoming requests should be authenticated.

## Contents
<a name="API_CustomJWTAuthorizerConfiguration_Contents"></a>

 ** discoveryUrl **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-discoveryUrl"></a>
This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.  
Type: String  
Pattern: `.+/\.well-known/openid-configuration`   
Required: Yes

 ** allowedAudience **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-allowedAudience"></a>
Represents individual audience values that are validated in the incoming JWT token validation process.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Required: No

 ** allowedClients **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-allowedClients"></a>
Represents individual client IDs that are validated in the incoming JWT token validation process.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Required: No

 ** allowedScopes **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-allowedScopes"></a>
An array of scopes that are allowed to access the token.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`   
Required: No

 ** allowedWorkloadConfiguration **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-allowedWorkloadConfiguration"></a>
The configuration that restricts which workloads in the request's identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.  
Type: [AllowedWorkloadConfiguration](API_AllowedWorkloadConfiguration.md) object  
Required: No

 ** customClaims **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-customClaims"></a>
An array of objects that define a custom claim validation name, value, and operation   
Type: Array of [CustomClaimValidationType](API_CustomClaimValidationType.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** privateEndpoint **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-privateEndpoint"></a>
The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** privateEndpointOverrides **   <a name="bedrockagentcorecontrol-Type-CustomJWTAuthorizerConfiguration-privateEndpointOverrides"></a>
The private endpoint overrides for the custom JWT authorizer configuration.  
Type: Array of [PrivateEndpointOverride](API_PrivateEndpointOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_CustomJWTAuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomJWTAuthorizerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomJWTAuthorizerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomJWTAuthorizerConfiguration) 