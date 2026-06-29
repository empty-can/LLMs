

# GetRegistry
<a name="API_GetRegistry"></a>

Retrieves information about a specific registry.

## Request Syntax
<a name="API_GetRegistry_RequestSyntax"></a>

```
GET /registries/{{registryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_GetRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-request-uri-registryId"></a>
The identifier of the registry to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_GetRegistry_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRegistry_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-approvalConfiguration"></a>
The approval configuration for registry records. For details, see the `ApprovalConfiguration` data type.  
Type: [ApprovalConfiguration](API_ApprovalConfiguration.md) object

 ** [authorizerConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-authorizerConfiguration"></a>
The authorizer configuration for the registry. For details, see the `AuthorizerConfiguration` data type.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [authorizerType](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-authorizerType"></a>
The type of authorizer used by the registry. This controls the authorization method for the Search and Invoke APIs used by consumers.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM` 

 ** [createdAt](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-createdAt"></a>
The timestamp when the registry was created.  
Type: Timestamp

 ** [description](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-description"></a>
The description of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [name](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-name"></a>
The name of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [registryArn](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-registryArn"></a>
The Amazon Resource Name (ARN) of the registry.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [registryId](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-registryId"></a>
The unique identifier of the registry.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}` 

 ** [status](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-status"></a>
The current status of the registry. Possible values include `CREATING`, `READY`, `UPDATING`, `CREATE_FAILED`, `UPDATE_FAILED`, `DELETING`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

 ** [statusReason](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-statusReason"></a>
The reason for the current status, typically set when the status is a failure state.  
Type: String

 ** [updatedAt](#API_GetRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetRegistry-response-updatedAt"></a>
The timestamp when the registry was last updated.  
Type: Timestamp

## Errors
<a name="API_GetRegistry_Errors"></a>

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
<a name="API_GetRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetRegistry) 