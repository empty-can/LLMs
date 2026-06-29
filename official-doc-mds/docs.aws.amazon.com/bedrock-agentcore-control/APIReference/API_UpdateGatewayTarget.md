

# UpdateGatewayTarget
<a name="API_UpdateGatewayTarget"></a>

Updates an existing gateway target.

You cannot update a target that is in a pending authorization state (`CREATE_PENDING_AUTH`, `UPDATE_PENDING_AUTH`, or `SYNCHRONIZE_PENDING_AUTH`). Wait for the authorization to complete or fail before updating the target.

## Request Syntax
<a name="API_UpdateGatewayTarget_RequestSyntax"></a>

```
PUT /gateways/{{gatewayIdentifier}}/targets/{{targetId}}/ HTTP/1.1
Content-type: application/json

{
   "credentialProviderConfigurations": [ 
      { 
         "credentialProvider": { ... },
         "credentialProviderType": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "metadataConfiguration": { 
      "allowedQueryParameters": [ "{{string}}" ],
      "allowedRequestHeaders": [ "{{string}}" ],
      "allowedResponseHeaders": [ "{{string}}" ]
   },
   "name": "{{string}}",
   "privateEndpoint": { ... },
   "targetConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateGatewayTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-uri-gatewayIdentifier"></a>
The unique identifier of the gateway associated with the target.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [targetId](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-uri-targetId"></a>
The unique identifier of the gateway target to update.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateGatewayTarget_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [credentialProviderConfigurations](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-credentialProviderConfigurations"></a>
The updated credential provider configurations for the gateway target.  
Type: Array of [CredentialProviderConfiguration](API_CredentialProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** [description](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-description"></a>
The updated description for the gateway target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [metadataConfiguration](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-metadataConfiguration"></a>
Configuration for HTTP header and query parameter propagation to the gateway target.  
Type: [MetadataConfiguration](API_MetadataConfiguration.md) object  
Required: No

 ** [name](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-name"></a>
The updated name for the gateway target.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}`   
Required: No

 ** [privateEndpoint](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-privateEndpoint"></a>
The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [targetConfiguration](#API_UpdateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-request-targetConfiguration"></a>
The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.  
Type: [TargetConfiguration](API_TargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_UpdateGatewayTarget_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "authorizationData": { ... },
   "createdAt": "string",
   "credentialProviderConfigurations": [ 
      { 
         "credentialProvider": { ... },
         "credentialProviderType": "string"
      }
   ],
   "description": "string",
   "gatewayArn": "string",
   "lastSynchronizedAt": "string",
   "metadataConfiguration": { 
      "allowedQueryParameters": [ "string" ],
      "allowedRequestHeaders": [ "string" ],
      "allowedResponseHeaders": [ "string" ]
   },
   "name": "string",
   "privateEndpoint": { ... },
   "privateEndpointManagedResources": [ 
      { 
         "domain": "string",
         "resourceAssociationArn": "string",
         "resourceGatewayArn": "string"
      }
   ],
   "protocolType": "string",
   "status": "string",
   "statusReasons": [ "string" ],
   "targetConfiguration": { ... },
   "targetId": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateGatewayTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authorizationData](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-authorizationData"></a>
OAuth2 authorization data for the updated gateway target. This data is returned when a target is configured with a credential provider with authorization code grant type and requires user federation.  
Type: [AuthorizationData](API_AuthorizationData.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-createdAt"></a>
The timestamp when the gateway target was created.  
Type: Timestamp

 ** [credentialProviderConfigurations](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-credentialProviderConfigurations"></a>
The updated credential provider configurations for the gateway target.  
Type: Array of [CredentialProviderConfiguration](API_CredentialProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.

 ** [description](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-description"></a>
The updated description of the gateway target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [gatewayArn](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [lastSynchronizedAt](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-lastSynchronizedAt"></a>
The date and time at which the targets were last synchronized.  
Type: Timestamp

 ** [metadataConfiguration](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-metadataConfiguration"></a>
The metadata configuration that was applied to the gateway target.  
Type: [MetadataConfiguration](API_MetadataConfiguration.md) object

 ** [name](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-name"></a>
The updated name of the gateway target.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}` 

 ** [privateEndpoint](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-privateEndpoint"></a>
The private endpoint configuration for the gateway target.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [privateEndpointManagedResources](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-privateEndpointManagedResources"></a>
The managed resources created by the gateway for private endpoint connectivity.  
Type: Array of [ManagedResourceDetails](API_ManagedResourceDetails.md) objects

 ** [protocolType](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-protocolType"></a>
The protocol type of the updated gateway target.  
Type: String  
Valid Values: `MCP | HTTP` 

 ** [status](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-status"></a>
The current status of the updated gateway target.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED | SYNCHRONIZING | SYNCHRONIZE_UNSUCCESSFUL | CREATE_PENDING_AUTH | UPDATE_PENDING_AUTH | SYNCHRONIZE_PENDING_AUTH` 

 ** [statusReasons](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-statusReasons"></a>
The reasons for the current status of the updated gateway target.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [targetConfiguration](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-targetConfiguration"></a>
The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.  
Type: [TargetConfiguration](API_TargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [targetId](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-targetId"></a>
The unique identifier of the updated gateway target.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [updatedAt](#API_UpdateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGatewayTarget-response-updatedAt"></a>
The timestamp when the gateway target was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdateGatewayTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateGatewayTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateGatewayTarget) 