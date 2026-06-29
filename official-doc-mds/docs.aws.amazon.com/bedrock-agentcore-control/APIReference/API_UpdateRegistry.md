

# UpdateRegistry
<a name="API_UpdateRegistry"></a>

Updates an existing registry. This operation uses PATCH semantics, so you only need to specify the fields you want to change.

## Request Syntax
<a name="API_UpdateRegistry_RequestSyntax"></a>

```
PATCH /registries/{{registryId}} HTTP/1.1
Content-type: application/json

{
   "approvalConfiguration": { 
      "optionalValue": { 
         "autoApproval": {{boolean}}
      }
   },
   "authorizerConfiguration": { 
      "optionalValue": { ... }
   },
   "description": { 
      "optionalValue": "{{string}}"
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_UpdateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-request-uri-registryId"></a>
The identifier of the registry to update. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_UpdateRegistry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-request-approvalConfiguration"></a>
The updated approval configuration for registry records. The updated configuration only affects new records that move to `PENDING_APPROVAL` status after the change. Existing records already in `PENDING_APPROVAL` status are not affected.  
Type: [UpdatedApprovalConfiguration](API_UpdatedApprovalConfiguration.md) object  
Required: No

 ** [authorizerConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-request-authorizerConfiguration"></a>
The updated authorizer configuration for the registry. Changing the authorizer configuration can break existing consumers of the registry who are using the authorization type prior to the update.  
Type: [UpdatedAuthorizerConfiguration](API_UpdatedAuthorizerConfiguration.md) object  
Required: No

 ** [description](#API_UpdateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-request-description"></a>
The updated description of the registry. To clear the description, include the `UpdatedDescription` wrapper with `optionalValue` not specified.  
Type: [UpdatedDescription](API_UpdatedDescription.md) object  
Required: No

 ** [name](#API_UpdateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-request-name"></a>
The updated name of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: No

## Response Syntax
<a name="API_UpdateRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "approvalConfiguration": { 
      "autoApproval": boolean
   },
   "authorizerConfiguration": { ... },
   "authorizerType": "string",
   "createdAt": "string",
   "description": "string",
   "name": "string",
   "registryArn": "string",
   "registryId": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [approvalConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-approvalConfiguration"></a>
The approval configuration for the updated registry. For details, see the `ApprovalConfiguration` data type.  
Type: [ApprovalConfiguration](API_ApprovalConfiguration.md) object

 ** [authorizerConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-authorizerConfiguration"></a>
The authorizer configuration for the updated registry. For details, see the `AuthorizerConfiguration` data type.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [authorizerType](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-authorizerType"></a>
The type of authorizer used by the updated registry. This controls the authorization method for the Search and Invoke APIs used by consumers.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM` 

 ** [createdAt](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-createdAt"></a>
The timestamp when the registry was created.  
Type: Timestamp

 ** [description](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-description"></a>
The description of the updated registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [name](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-name"></a>
The name of the updated registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [registryArn](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-registryArn"></a>
The Amazon Resource Name (ARN) of the updated registry.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [registryId](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-registryId"></a>
The unique identifier of the updated registry.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}` 

 ** [status](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-status"></a>
The current status of the updated registry. Possible values include `CREATING`, `READY`, `UPDATING`, `CREATE_FAILED`, `UPDATE_FAILED`, `DELETING`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

 ** [statusReason](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-statusReason"></a>
The reason for the current status of the updated registry.  
Type: String

 ** [updatedAt](#API_UpdateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistry-response-updatedAt"></a>
The timestamp when the registry was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdateRegistry_Errors"></a>

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
<a name="API_UpdateRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateRegistry) 