

# UpdateRegistryRecord
<a name="API_UpdateRegistryRecord"></a>

Updates an existing registry record. This operation uses PATCH semantics, so you only need to specify the fields you want to change. The update is processed asynchronously and returns HTTP 202 Accepted.

## Request Syntax
<a name="API_UpdateRegistryRecord_RequestSyntax"></a>

```
PATCH /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
Content-type: application/json

{
   "description": { 
      "optionalValue": "{{string}}"
   },
   "descriptors": { 
      "optionalValue": { 
         "a2a": { 
            "optionalValue": { 
               "agentCard": { 
                  "inlineContent": "{{string}}",
                  "schemaVersion": "{{string}}"
               }
            }
         },
         "agentSkills": { 
            "optionalValue": { 
               "skillDefinition": { 
                  "optionalValue": { 
                     "inlineContent": "{{string}}",
                     "schemaVersion": "{{string}}"
                  }
               },
               "skillMd": { 
                  "optionalValue": { 
                     "inlineContent": "{{string}}"
                  }
               }
            }
         },
         "custom": { 
            "optionalValue": { 
               "inlineContent": "{{string}}"
            }
         },
         "mcp": { 
            "optionalValue": { 
               "server": { 
                  "optionalValue": { 
                     "inlineContent": "{{string}}",
                     "schemaVersion": "{{string}}"
                  }
               },
               "tools": { 
                  "optionalValue": { 
                     "inlineContent": "{{string}}",
                     "protocolVersion": "{{string}}"
                  }
               }
            }
         }
      }
   },
   "descriptorType": "{{string}}",
   "name": "{{string}}",
   "recordVersion": "{{string}}",
   "synchronizationConfiguration": { 
      "optionalValue": { 
         "fromUrl": { 
            "credentialProviderConfigurations": [ 
               { 
                  "credentialProvider": { ... },
                  "credentialProviderType": "{{string}}"
               }
            ],
            "url": "{{string}}"
         }
      }
   },
   "synchronizationType": { 
      "optionalValue": "{{string}}"
   },
   "triggerSynchronization": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-uri-recordId"></a>
The identifier of the registry record to update. You can specify either the Amazon Resource Name (ARN) or the ID of the record.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-uri-registryId"></a>
The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_UpdateRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-description"></a>
The updated description for the registry record. To clear the description, include the `UpdatedDescription` wrapper with `optionalValue` not specified.  
Type: [UpdatedDescription](API_UpdatedDescription.md) object  
Required: No

 ** [descriptors](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-descriptors"></a>
The updated descriptor-type-specific configuration containing the resource schema and metadata. Uses PATCH semantics where individual descriptor fields can be updated independently.  
Type: [UpdatedDescriptors](API_UpdatedDescriptors.md) object  
Required: No

 ** [descriptorType](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-descriptorType"></a>
The updated descriptor type for the registry record. Changing the descriptor type may require updating the `descriptors` field to match the new type's schema requirements.  
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS`   
Required: No

 ** [name](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-name"></a>
The updated name for the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: No

 ** [recordVersion](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-recordVersion"></a>
The version of the registry record for optimistic locking. If provided, it must match the current version of the record. The service automatically increments the version after a successful update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: No

 ** [synchronizationConfiguration](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-synchronizationConfiguration"></a>
The updated synchronization configuration for the registry record.  
Type: [UpdatedSynchronizationConfiguration](API_UpdatedSynchronizationConfiguration.md) object  
Required: No

 ** [synchronizationType](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-synchronizationType"></a>
The updated synchronization type for the registry record.  
Type: [UpdatedSynchronizationType](API_UpdatedSynchronizationType.md) object  
Required: No

 ** [triggerSynchronization](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-request-triggerSynchronization"></a>
Whether to trigger synchronization using the stored or provided configuration. When set to `true`, the service will synchronize the record metadata from the configured external source.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_UpdateRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_UpdateRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp

 ** [description](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-description"></a>
The description of the updated registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [descriptors](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-descriptors"></a>
The descriptor-type-specific configuration of the updated registry record. For details, see the `Descriptors` data type.  
Type: [Descriptors](API_Descriptors.md) object

 ** [descriptorType](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-descriptorType"></a>
The descriptor type of the updated registry record. Possible values are `MCP`, `A2A`, `CUSTOM`, and `AGENT_SKILLS`.  
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS` 

 ** [name](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-name"></a>
The name of the updated registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [recordArn](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-recordArn"></a>
The Amazon Resource Name (ARN) of the updated registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-recordId"></a>
The unique identifier of the updated registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [recordVersion](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-recordVersion"></a>
The version of the updated registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+` 

 ** [registryArn](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-registryArn"></a>
The Amazon Resource Name (ARN) of the registry that contains the updated record.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-status"></a>
The current status of the updated registry record. Possible values include `CREATING`, `DRAFT`, `APPROVED`, `PENDING_APPROVAL`, `REJECTED`, `DEPRECATED`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED`.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [statusReason](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-statusReason"></a>
The reason for the current status of the updated registry record.  
Type: String

 ** [synchronizationConfiguration](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-synchronizationConfiguration"></a>
The synchronization configuration of the updated registry record.  
Type: [SynchronizationConfiguration](API_SynchronizationConfiguration.md) object

 ** [synchronizationType](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-synchronizationType"></a>
The synchronization type of the updated registry record.  
Type: String  
Valid Values: `URL` 

 ** [updatedAt](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecord-response-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdateRegistryRecord_Errors"></a>

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
<a name="API_UpdateRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecord) 