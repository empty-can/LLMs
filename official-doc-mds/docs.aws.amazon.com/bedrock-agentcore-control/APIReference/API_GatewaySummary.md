

# GatewaySummary
<a name="API_GatewaySummary"></a>

Contains summary information about a gateway.

## Contents
<a name="API_GatewaySummary_Contents"></a>

 ** authorizerType **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-authorizerType"></a>
The type of authorizer used by the gateway.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM | NONE | AUTHENTICATE_ONLY`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-createdAt"></a>
The timestamp when the gateway was created.  
Type: Timestamp  
Required: Yes

 ** gatewayId **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-gatewayId"></a>
The unique identifier of the gateway.  
Type: String  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-name"></a>
The name of the gateway.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,48}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-status"></a>
The current status of the gateway.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-updatedAt"></a>
The timestamp when the gateway was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-description"></a>
The description of the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** protocolType **   <a name="bedrockagentcorecontrol-Type-GatewaySummary-protocolType"></a>
The protocol type used by the gateway.  
Type: String  
Valid Values: `MCP`   
Required: No

## See Also
<a name="API_GatewaySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GatewaySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GatewaySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GatewaySummary) 