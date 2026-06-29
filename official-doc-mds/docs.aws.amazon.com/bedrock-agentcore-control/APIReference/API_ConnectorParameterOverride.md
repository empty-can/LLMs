

# ConnectorParameterOverride
<a name="API_ConnectorParameterOverride"></a>

Specifies a parameter override for a connector tool, allowing you to control parameter visibility and descriptions.

## Contents
<a name="API_ConnectorParameterOverride_Contents"></a>

 ** path **   <a name="bedrockagentcorecontrol-Type-ConnectorParameterOverride-path"></a>
A JSON Pointer path identifying the parameter (for example, `/numberOfResults` or `/filter`).  
Type: String  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-ConnectorParameterOverride-description"></a>
An agent-facing description override for this parameter.  
Type: String  
Required: No

 ** visible **   <a name="bedrockagentcorecontrol-Type-ConnectorParameterOverride-visible"></a>
Whether this parameter is visible to the agent. If not specified, uses the service default.  
Type: Boolean  
Required: No

## See Also
<a name="API_ConnectorParameterOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConnectorParameterOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConnectorParameterOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConnectorParameterOverride) 