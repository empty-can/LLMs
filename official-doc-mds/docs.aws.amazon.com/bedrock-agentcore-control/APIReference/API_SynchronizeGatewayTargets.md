

# SynchronizeGatewayTargets
<a name="API_SynchronizeGatewayTargets"></a>

Synchronizes the gateway targets by fetching the latest tool definitions from the target endpoints.

You cannot synchronize a target that is in a pending authorization state (`CREATE_PENDING_AUTH`, `UPDATE_PENDING_AUTH`, or `SYNCHRONIZE_PENDING_AUTH`). Wait for the authorization to complete or fail before synchronizing.

You cannot synchronize a target that has a static tool schema (`mcpToolSchema`) configured. Remove the static schema through an `UpdateGatewayTarget` call to enable dynamic tool synchronization.

## Request Syntax
<a name="API_SynchronizeGatewayTargets_RequestSyntax"></a>

```
PUT /gateways/{{gatewayIdentifier}}/synchronizeTargets HTTP/1.1
Content-type: application/json

{
   "targetIdList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_SynchronizeGatewayTargets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_SynchronizeGatewayTargets_RequestSyntax) **   <a name="bedrockagentcorecontrol-SynchronizeGatewayTargets-request-uri-gatewayIdentifier"></a>
The gateway Identifier.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_SynchronizeGatewayTargets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetIdList](#API_SynchronizeGatewayTargets_RequestSyntax) **   <a name="bedrockagentcorecontrol-SynchronizeGatewayTargets-request-targetIdList"></a>
The target ID list.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Response Syntax
<a name="API_SynchronizeGatewayTargets_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "targets": [ 
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
   ]
}
```

## Response Elements
<a name="API_SynchronizeGatewayTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [targets](#API_SynchronizeGatewayTargets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SynchronizeGatewayTargets-response-targets"></a>
The gateway targets for synchronization.  
Type: Array of [GatewayTarget](API_GatewayTarget.md) objects

## Errors
<a name="API_SynchronizeGatewayTargets_Errors"></a>

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
<a name="API_SynchronizeGatewayTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SynchronizeGatewayTargets) 