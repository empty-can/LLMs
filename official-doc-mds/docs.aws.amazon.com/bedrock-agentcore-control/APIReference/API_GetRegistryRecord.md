

# GetRegistryRecord
<a name="API_GetRegistryRecord"></a>

Retrieves information about a specific registry record.

## Request Syntax
<a name="API_GetRegistryRecord_RequestSyntax"></a>

```
GET /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_GetRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-request-uri-recordId"></a>
The identifier of the registry record to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the record.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_GetRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-request-uri-registryId"></a>
The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_GetRegistryRecord_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "descriptors": { 
      "a2a": { 
         "agentCard": { 
            "inlineContent": "string",
            "schemaVersion": "string"
         }
      },
      "agentSkills": { 
         "skillDefinition": { 
            "inlineContent": "string",
            "schemaVersion": "string"
         },
         "skillMd": { 
            "inlineContent": "string"
         }
      },
      "custom": { 
         "inlineContent": "string"
      },
      "mcp": { 
         "server": { 
            "inlineContent": "string",
            "schemaVersion": "string"
         },
         "tools": { 
            "inlineContent": "string",
            "protocolVersion": "string"
         }
      }
   },
   "descriptorType": "string",
   "name": "string",
   "recordArn": "string",
   "recordId": "string",
   "recordVersion": "string",
   "registryArn": "string",
   "status": "string",
   "statusReason": "string",
   "synchronizationConfiguration": { 
      "fromUrl": { 
         "credentialProviderConfigurations": [ 
            { 
               "credentialProvider": { ... },
               "credentialProviderType": "string"
            }
         ],
         "url": "string"
      }
   },
   "synchronizationType": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp

 ** [description](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-description"></a>
The description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [descriptors](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-descriptors"></a>
The descriptor-type-specific configuration containing the resource schema and metadata. For details, see the `Descriptors` data type.  
Type: [Descriptors](API_Descriptors.md) object

 ** [descriptorType](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-descriptorType"></a>
The descriptor type of the registry record. Possible values are `MCP`, `A2A`, `CUSTOM`, and `AGENT_SKILLS`.  
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS` 

 ** [name](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-name"></a>
The name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [recordArn](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [recordVersion](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-recordVersion"></a>
The version of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+` 

 ** [registryArn](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-registryArn"></a>
The Amazon Resource Name (ARN) of the registry that contains the record.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-status"></a>
The current status of the registry record. Possible values include `CREATING`, `DRAFT`, `APPROVED`, `PENDING_APPROVAL`, `REJECTED`, `DEPRECATED`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED`. A record transitions from `CREATING` to `DRAFT`, then to `PENDING_APPROVAL` (via `SubmitRegistryRecordForApproval`), and finally to `APPROVED` upon approval.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [statusReason](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-statusReason"></a>
The reason for the current status, typically set when the status is a failure state.  
Type: String

 ** [synchronizationConfiguration](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-synchronizationConfiguration"></a>
The configuration for synchronizing registry record metadata from an external source.  
Type: [SynchronizationConfiguration](API_SynchronizationConfiguration.md) object

 ** [synchronizationType](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-synchronizationType"></a>
The type of synchronization used for this record.  
Type: String  
Valid Values: `URL` 

 ** [updatedAt](#API_GetRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistryRecord-response-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp

## Errors
<a name="API_GetRegistryRecord_Errors"></a>

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

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetRegistryRecord) 