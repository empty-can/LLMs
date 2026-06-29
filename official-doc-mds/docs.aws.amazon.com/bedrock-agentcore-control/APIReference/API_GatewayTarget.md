

# GatewayTarget
<a name="API_GatewayTarget"></a>

The gateway target.

## Contents
<a name="API_GatewayTarget_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-createdAt"></a>
The date and time at which the target was created.  
Type: Timestamp  
Required: Yes

 ** credentialProviderConfigurations **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-credentialProviderConfigurations"></a>
The provider configurations.  
Type: Array of [CredentialProviderConfiguration](API_CredentialProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** gatewayArn **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway target.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-name"></a>
The name of the gateway target.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-status"></a>
The status of the gateway target.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED | SYNCHRONIZING | SYNCHRONIZE_UNSUCCESSFUL | CREATE_PENDING_AUTH | UPDATE_PENDING_AUTH | SYNCHRONIZE_PENDING_AUTH`   
Required: Yes

 ** targetConfiguration **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-targetConfiguration"></a>
The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.  
Type: [TargetConfiguration](API_TargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** targetId **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-targetId"></a>
The target ID.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-updatedAt"></a>
The date and time at which the target was updated.  
Type: Timestamp  
Required: Yes

 ** authorizationData **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-authorizationData"></a>
OAuth2 authorization data for the gateway target. This data is returned when a target is configured with a credential provider with authorization code grant type and requires user federation.  
Type: [AuthorizationData](API_AuthorizationData.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-description"></a>
The description for the gateway target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** lastSynchronizedAt **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-lastSynchronizedAt"></a>
The last synchronization time.  
Type: Timestamp  
Required: No

 ** metadataConfiguration **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-metadataConfiguration"></a>
The metadata configuration for HTTP header and query parameter propagation to and from this gateway target.  
Type: [MetadataConfiguration](API_MetadataConfiguration.md) object  
Required: No

 ** privateEndpoint **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-privateEndpoint"></a>
The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** privateEndpointManagedResources **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-privateEndpointManagedResources"></a>
A list of managed resources created by the gateway for private endpoint connectivity. These resources are created in your account when you use a managed VPC Lattice resource configuration.  
Type: Array of [ManagedResourceDetails](API_ManagedResourceDetails.md) objects  
Required: No

 ** protocolType **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-protocolType"></a>
The protocol type of the gateway target.  
Type: String  
Valid Values: `MCP | HTTP`   
Required: No

 ** statusReasons **   <a name="bedrockagentcorecontrol-Type-GatewayTarget-statusReasons"></a>
The status reasons for the target status.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

## See Also
<a name="API_GatewayTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GatewayTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GatewayTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GatewayTarget) 