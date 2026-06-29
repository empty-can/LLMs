

# GetGatewayTarget
<a name="API_GetGatewayTarget"></a>

Retrieves information about a specific gateway target.

## Request Syntax
<a name="API_GetGatewayTarget_RequestSyntax"></a>

```
GET /gateways/{{gatewayIdentifier}}/targets/{{targetId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGatewayTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_GetGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-request-uri-gatewayIdentifier"></a>
The identifier of the gateway that contains the target.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [targetId](#API_GetGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-request-uri-targetId"></a>
The unique identifier of the target to retrieve.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_GetGatewayTarget_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGatewayTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetGatewayTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizationData](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-authorizationData"></a>
OAuth2 authorization data for the gateway target. This data is returned when a target is configured with a credential provider with authorization code grant type and requires user federation.  
Type: [AuthorizationData](API_AuthorizationData.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-createdAt"></a>
The timestamp when the gateway target was created.  
Type: Timestamp

 ** [credentialProviderConfigurations](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-credentialProviderConfigurations"></a>
The credential provider configurations for the gateway target.  
Type: Array of [CredentialProviderConfiguration](API_CredentialProviderConfiguration.md) objects  
Array Members: Fixed number of 1 item.

 ** [description](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-description"></a>
The description of the gateway target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [gatewayArn](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [lastSynchronizedAt](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-lastSynchronizedAt"></a>
The last synchronization of the target.  
Type: Timestamp

 ** [metadataConfiguration](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-metadataConfiguration"></a>
The metadata configuration for HTTP header and query parameter propagation for the retrieved gateway target.  
Type: [MetadataConfiguration](API_MetadataConfiguration.md) object

 ** [name](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-name"></a>
The name of the gateway target.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,100}` 

 ** [privateEndpoint](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-privateEndpoint"></a>
The private endpoint configuration for the gateway target.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [privateEndpointManagedResources](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-privateEndpointManagedResources"></a>
The managed resources created by the gateway for private endpoint connectivity.  
Type: Array of [ManagedResourceDetails](API_ManagedResourceDetails.md) objects

 ** [protocolType](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-protocolType"></a>
The protocol type of the gateway target.  
Type: String  
Valid Values: `MCP | HTTP` 

 ** [status](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-status"></a>
The current status of the gateway target.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED | SYNCHRONIZING | SYNCHRONIZE_UNSUCCESSFUL | CREATE_PENDING_AUTH | UPDATE_PENDING_AUTH | SYNCHRONIZE_PENDING_AUTH` 

 ** [statusReasons](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-statusReasons"></a>
The reasons for the current status of the gateway target.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [targetConfiguration](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-targetConfiguration"></a>
The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.  
Type: [TargetConfiguration](API_TargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [targetId](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-targetId"></a>
The unique identifier of the gateway target.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [updatedAt](#API_GetGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetGatewayTarget-response-updatedAt"></a>
The timestamp when the gateway target was last updated.  
Type: Timestamp

## Errors
<a name="API_GetGatewayTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetGatewayTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetGatewayTarget) 