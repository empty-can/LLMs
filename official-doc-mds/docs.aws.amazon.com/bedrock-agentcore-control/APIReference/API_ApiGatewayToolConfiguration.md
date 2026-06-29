

# ApiGatewayToolConfiguration
<a name="API_ApiGatewayToolConfiguration"></a>

The configuration for defining REST API tool filters and overrides for the gateway target.

## Contents
<a name="API_ApiGatewayToolConfiguration_Contents"></a>

 ** toolFilters **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolConfiguration-toolFilters"></a>
A list of path and method patterns to expose as tools using metadata from the REST API's OpenAPI specification.  
Type: Array of [ApiGatewayToolFilter](API_ApiGatewayToolFilter.md) objects  
Required: Yes

 ** toolOverrides **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolConfiguration-toolOverrides"></a>
A list of explicit tool definitions with optional custom names and descriptions.  
Type: Array of [ApiGatewayToolOverride](API_ApiGatewayToolOverride.md) objects  
Required: No

## See Also
<a name="API_ApiGatewayToolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ApiGatewayToolConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ApiGatewayToolConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ApiGatewayToolConfiguration) 