

# CreateRegistryRecord
<a name="API_CreateRegistryRecord"></a>

Creates a new registry record within the specified registry. A registry record represents an individual AI resource's metadata in the registry. This could be an MCP server (and associated tools), A2A agent, agent skill, or a custom resource with a custom schema.

The record is processed asynchronously and returns HTTP 202 Accepted.

## Request Syntax
<a name="API_CreateRegistryRecord_RequestSyntax"></a>

```
POST /registries/{{registryId}}/records HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "descriptors": { 
      "a2a": { 
         "agentCard": { 
            "inlineContent": "{{string}}",
            "schemaVersion": "{{string}}"
         }
      },
      "agentSkills": { 
         "skillDefinition": { 
            "inlineContent": "{{string}}",
            "schemaVersion": "{{string}}"
         },
         "skillMd": { 
            "inlineContent": "{{string}}"
         }
      },
      "custom": { 
         "inlineContent": "{{string}}"
      },
      "mcp": { 
         "server": { 
            "inlineContent": "{{string}}",
            "schemaVersion": "{{string}}"
         },
         "tools": { 
            "inlineContent": "{{string}}",
            "protocolVersion": "{{string}}"
         }
      }
   },
   "descriptorType": "{{string}}",
   "name": "{{string}}",
   "recordVersion": "{{string}}",
   "synchronizationConfiguration": { 
      "fromUrl": { 
         "credentialProviderConfigurations": [ 
            { 
               "credentialProvider": { ... },
               "credentialProviderType": "{{string}}"
            }
         ],
         "url": "{{string}}"
      }
   },
   "synchronizationType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-uri-registryId"></a>
The identifier of the registry where the record will be created. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_CreateRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-description"></a>
A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [descriptors](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-descriptors"></a>
The descriptor-type-specific configuration containing the resource schema and metadata. The structure of this field depends on the `descriptorType` you specify.  
Type: [Descriptors](API_Descriptors.md) object  
Required: No

 ** [descriptorType](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-descriptorType"></a>
The descriptor type of the registry record.  
+  `MCP` - Model Context Protocol descriptor for MCP-compatible servers and tools.
+  `A2A` - Agent-to-Agent protocol descriptor.
+  `CUSTOM` - Custom descriptor type for resources such as APIs, Lambda functions, or servers not conforming to a standard protocol.
+  `AGENT_SKILLS` - Agent skills descriptor for defining agent skill definitions.
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS`   
Required: Yes

 ** [name](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-name"></a>
The name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** [recordVersion](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-recordVersion"></a>
The version of the registry record. Use this to track different versions of the record's content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: No

 ** [synchronizationConfiguration](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-synchronizationConfiguration"></a>
The configuration for synchronizing registry record metadata from an external source, such as a URL-based MCP server.  
Type: [SynchronizationConfiguration](API_SynchronizationConfiguration.md) object  
Required: No

 ** [synchronizationType](#API_CreateRegistryRecord_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-request-synchronizationType"></a>
The type of synchronization to use for keeping the record metadata up to date from an external source. Possible values include `FROM_URL` and `NONE`.  
Type: String  
Valid Values: `URL`   
Required: No

## Response Syntax
<a name="API_CreateRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recordArn](#API_CreateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-response-recordArn"></a>
The Amazon Resource Name (ARN) of the created registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [status](#API_CreateRegistryRecord_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistryRecord-response-status"></a>
The status of the registry record. Set to `CREATING` while the asynchronous workflow is in progress.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

## Errors
<a name="API_CreateRegistryRecord_Errors"></a>

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
<a name="API_CreateRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord) 