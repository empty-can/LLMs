

# ApiGatewayToolFilter
<a name="API_ApiGatewayToolFilter"></a>

Specifies which operations from an API Gateway REST API are exposed as tools. Tool names and descriptions are derived from the operationId and description fields in the API's exported OpenAPI specification.

## Contents
<a name="API_ApiGatewayToolFilter_Contents"></a>

 ** filterPath **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolFilter-filterPath"></a>
Resource path to match in the REST API. Supports exact paths (for example, `/pets`) or wildcard paths (for example, `/pets/*` to match all paths under `/pets`). Must match existing paths in the REST API.  
Type: String  
Required: Yes

 ** methods **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolFilter-methods"></a>
The methods to filter for.  
Type: Array of strings  
Valid Values: `GET | DELETE | HEAD | OPTIONS | PATCH | PUT | POST`   
Required: Yes

## See Also
<a name="API_ApiGatewayToolFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ApiGatewayToolFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ApiGatewayToolFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ApiGatewayToolFilter) 