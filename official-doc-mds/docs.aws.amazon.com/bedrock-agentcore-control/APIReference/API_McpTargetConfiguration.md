

# McpTargetConfiguration
<a name="API_McpTargetConfiguration"></a>

The Model Context Protocol (MCP) configuration for a target. This structure defines how the gateway uses MCP to communicate with the target.

## Contents
<a name="API_McpTargetConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiGateway **   <a name="bedrockagentcorecontrol-Type-McpTargetConfiguration-apiGateway"></a>
The configuration for an Amazon API Gateway target.  
Type: [ApiGatewayTargetConfiguration](API_ApiGatewayTargetConfiguration.md) object  
Required: No

 ** connector **   <a name="bedrockagentcorecontrol-Type-McpTargetConfiguration-connector"></a>
The connector integration configuration for the Model Context Protocol target. This configuration defines how the gateway uses a pre-built connector to communicate with the target.  
Type: [ConnectorTargetConfiguration](API_ConnectorTargetConfiguration.md) object  
Required: No

 ** lambda **   <a name="bedrockagentcorecontrol-Type-McpTargetConfiguration-lambda"></a>
The Lambda configuration for the Model Context Protocol target. This configuration defines how the gateway uses a Lambda function to communicate with the target.  
Type: [McpLambdaTargetConfiguration](API_McpLambdaTargetConfiguration.md) object  
Required: No

 ** mcpServer **   <a name="bedrockagentcorecontrol-Type-McpTargetConfiguration-mcpServer"></a>
The MCP server specified as the gateway target.  
Type: [McpServerTargetConfiguration](API_McpServerTargetConfiguration.md) object  
Required: No

 ** openApiSchema **   <a name="bedrockagentcorecontrol-Type-McpTargetConfiguration-openApiSchema"></a>
The OpenAPI schema for the Model Context Protocol target. This schema defines the API structure of the target.  
Type: [ApiSchemaConfiguration](API_ApiSchemaConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** smithyModel **   <a name="bedrockagentcorecontrol-Type-McpTargetConfiguration-smithyModel"></a>
The Smithy model for the Model Context Protocol target. This model defines the API structure of the target using the Smithy specification.  
Type: [ApiSchemaConfiguration](API_ApiSchemaConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_McpTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/McpTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/McpTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/McpTargetConfiguration) 