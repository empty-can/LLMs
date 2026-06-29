

# RuntimeTargetConfiguration
<a name="API_RuntimeTargetConfiguration"></a>

Configuration for an AgentCore Runtime target. Specifies the agent runtime to route requests to via HTTP.

## Contents
<a name="API_RuntimeTargetConfiguration_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-RuntimeTargetConfiguration-arn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime to route requests to.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:runtime/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** qualifier **   <a name="bedrockagentcorecontrol-Type-RuntimeTargetConfiguration-qualifier"></a>
The qualifier for the agent runtime, used to target a specific endpoint version. If not specified, the default endpoint is used.  
Type: String  
Pattern: `.*([1-9][0-9]{0,4})|([a-zA-Z][a-zA-Z0-9_]{0,47}).*`   
Required: No

 ** schema **   <a name="bedrockagentcorecontrol-Type-RuntimeTargetConfiguration-schema"></a>
The API schema configuration that defines the structure of the runtime target's API.  
Type: [HttpApiSchemaConfiguration](API_HttpApiSchemaConfiguration.md) object  
Required: No

## See Also
<a name="API_RuntimeTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RuntimeTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RuntimeTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RuntimeTargetConfiguration) 