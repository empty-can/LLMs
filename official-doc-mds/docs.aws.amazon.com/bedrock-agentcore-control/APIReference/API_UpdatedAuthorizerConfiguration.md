

# UpdatedAuthorizerConfiguration
<a name="API_UpdatedAuthorizerConfiguration"></a>

Wrapper for updating an optional AuthorizerConfiguration field with PATCH semantics. When present in an update request, the authorizer configuration is replaced with optionalValue. When absent, the authorizer configuration is left unchanged. To unset, include the wrapper with optionalValue not specified.

## Contents
<a name="API_UpdatedAuthorizerConfiguration_Contents"></a>

 ** optionalValue **   <a name="bedrockagentcorecontrol-Type-UpdatedAuthorizerConfiguration-optionalValue"></a>
The updated authorizer configuration value. If not specified, it will clear the current authorizer configuration of the resource.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_UpdatedAuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatedAuthorizerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatedAuthorizerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatedAuthorizerConfiguration) 