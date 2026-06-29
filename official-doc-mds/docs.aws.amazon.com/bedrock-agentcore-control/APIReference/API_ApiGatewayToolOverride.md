

# ApiGatewayToolOverride
<a name="API_ApiGatewayToolOverride"></a>

Settings to override configurations for a tool.

## Contents
<a name="API_ApiGatewayToolOverride_Contents"></a>

 ** method **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolOverride-method"></a>
The HTTP method to expose for the specified path.  
Type: String  
Valid Values: `GET | DELETE | HEAD | OPTIONS | PATCH | PUT | POST`   
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolOverride-name"></a>
The name of tool. Identifies the tool in the Model Context Protocol.  
Type: String  
Required: Yes

 ** path **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolOverride-path"></a>
Resource path in the REST API (e.g., `/pets`). Must explicitly match an existing path in the REST API.  
Type: String  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-ApiGatewayToolOverride-description"></a>
The description of the tool. Provides information about the purpose and usage of the tool. If not provided, uses the description from the API's OpenAPI specification.  
Type: String  
Required: No

## See Also
<a name="API_ApiGatewayToolOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ApiGatewayToolOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ApiGatewayToolOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ApiGatewayToolOverride) 