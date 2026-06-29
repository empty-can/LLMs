

# ConnectorConfiguration
<a name="API_ConnectorConfiguration"></a>

Configuration for a single tool within a connector.

## Contents
<a name="API_ConnectorConfiguration_Contents"></a>

 ** name **   <a name="bedrockagentcorecontrol-Type-ConnectorConfiguration-name"></a>
The tool or operation name (for example, `retrieve` or `webSearch`).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]*`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-ConnectorConfiguration-description"></a>
An agent-facing description override for this tool.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2000.  
Required: No

 ** parameterOverrides **   <a name="bedrockagentcorecontrol-Type-ConnectorConfiguration-parameterOverrides"></a>
Parameters to expose to the agent at runtime, with optional description overrides.  
Type: Array of [ConnectorParameterOverride](API_ConnectorParameterOverride.md) objects  
Required: No

 ** parameterValues **   <a name="bedrockagentcorecontrol-Type-ConnectorConfiguration-parameterValues"></a>
Parameters to set as fixed or default values when provisioning this tool.  
Type: JSON value  
Required: No

## See Also
<a name="API_ConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConnectorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConnectorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConnectorConfiguration) 