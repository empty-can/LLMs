

# CreateGatewayTarget
<a name="API_CreateGatewayTarget"></a>

Creates a target for a gateway. A target defines an endpoint that the gateway can connect to.

## Request Syntax
<a name="API_CreateGatewayTarget_RequestSyntax"></a>

```
POST /gateways/{{gatewayIdentifier}}/targets/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
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
<a name="API_CreateGatewayTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-uri-gatewayIdentifier"></a>
The identifier of the gateway to create a target for.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_CreateGatewayTarget_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [credentialProviderConfigurations](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-credentialProviderConfigurations"></a>
The credential provider configurations for the target. These configurations specify how the gateway authenticates with the target endpoint.  
Type: Array of [CredentialProviderConfiguration](API_CredentialProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** [description](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-description"></a>
The description of the gateway target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [metadataConfiguration](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-metadataConfiguration"></a>
Optional configuration for HTTP header and query parameter propagation to and from the gateway target.  
Type: [MetadataConfiguration](API_MetadataConfiguration.md) object  
Required: No

 ** [name](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-name"></a>
The name of the gateway target. The name must be unique within the gateway.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}`   
Required: No

 ** [privateEndpoint](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-privateEndpoint"></a>
The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [targetConfiguration](#API_CreateGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-request-targetConfiguration"></a>
The configuration settings for the target, including endpoint information and schema definitions.  
Type: [TargetConfiguration](API_TargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_CreateGatewayTarget_ResponseSyntax"></a>

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
<a name="API_CreateGatewayTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authorizationData](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-authorizationData"></a>
OAuth2 authorization data for the created gateway target. This data is returned when a target is configured with a credential provider with authorization code grant type and requires user federation.  
Type: [AuthorizationData](API_AuthorizationData.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-createdAt"></a>
The timestamp when the target was created.  
Type: Timestamp

 ** [credentialProviderConfigurations](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-credentialProviderConfigurations"></a>
The credential provider configurations for the target.  
Type: Array of [CredentialProviderConfiguration](API_CredentialProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.

 ** [description](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-description"></a>
The description of the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [gatewayArn](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [lastSynchronizedAt](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-lastSynchronizedAt"></a>
The last synchronization of the target.  
Type: Timestamp

 ** [metadataConfiguration](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-metadataConfiguration"></a>
The metadata configuration that was applied to the created gateway target.  
Type: [MetadataConfiguration](API_MetadataConfiguration.md) object

 ** [name](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-name"></a>
The name of the target.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}` 

 ** [privateEndpoint](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-privateEndpoint"></a>
The private endpoint configuration for the gateway target.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [privateEndpointManagedResources](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-privateEndpointManagedResources"></a>
The managed resources created by the gateway for private endpoint connectivity.  
Type: Array of [ManagedResourceDetails](API_ManagedResourceDetails.md) objects

 ** [protocolType](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-protocolType"></a>
The protocol type of the created gateway target.  
Type: String  
Valid Values: `MCP | HTTP` 

 ** [status](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-status"></a>
The current status of the target.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED | SYNCHRONIZING | SYNCHRONIZE_UNSUCCESSFUL | CREATE_PENDING_AUTH | UPDATE_PENDING_AUTH | SYNCHRONIZE_PENDING_AUTH` 

 ** [statusReasons](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-statusReasons"></a>
The reasons for the current status of the target.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [targetConfiguration](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-targetConfiguration"></a>
The configuration settings for the target.  
Type: [TargetConfiguration](API_TargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [targetId](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-targetId"></a>
The unique identifier of the created target.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [updatedAt](#API_CreateGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGatewayTarget-response-updatedAt"></a>
The timestamp when the target was last updated.  
Type: Timestamp

## Errors
<a name="API_CreateGatewayTarget_Errors"></a>

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
<a name="API_CreateGatewayTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateGatewayTarget) 