

# HarnessToolConfiguration
<a name="API_HarnessToolConfiguration"></a>

Configuration union for different tool types.

## Contents
<a name="API_HarnessToolConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentCoreBrowser **   <a name="bedrockagentcorecontrol-Type-HarnessToolConfiguration-agentCoreBrowser"></a>
Configuration for AgentCore Browser.  
Type: [HarnessAgentCoreBrowserConfig](API_HarnessAgentCoreBrowserConfig.md) object  
Required: No

 ** agentCoreCodeInterpreter **   <a name="bedrockagentcorecontrol-Type-HarnessToolConfiguration-agentCoreCodeInterpreter"></a>
Configuration for AgentCore Code Interpreter.  
Type: [HarnessAgentCoreCodeInterpreterConfig](API_HarnessAgentCoreCodeInterpreterConfig.md) object  
Required: No

 ** agentCoreGateway **   <a name="bedrockagentcorecontrol-Type-HarnessToolConfiguration-agentCoreGateway"></a>
Configuration for AgentCore Gateway.  
Type: [HarnessAgentCoreGatewayConfig](API_HarnessAgentCoreGatewayConfig.md) object  
Required: No

 ** inlineFunction **   <a name="bedrockagentcorecontrol-Type-HarnessToolConfiguration-inlineFunction"></a>
Configuration for an inline function tool.  
Type: [HarnessInlineFunctionConfig](API_HarnessInlineFunctionConfig.md) object  
Required: No

 ** remoteMcp **   <a name="bedrockagentcorecontrol-Type-HarnessToolConfiguration-remoteMcp"></a>
Configuration for remote MCP server.  
Type: [HarnessRemoteMcpConfig](API_HarnessRemoteMcpConfig.md) object  
Required: No

## See Also
<a name="API_HarnessToolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessToolConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessToolConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessToolConfiguration) 