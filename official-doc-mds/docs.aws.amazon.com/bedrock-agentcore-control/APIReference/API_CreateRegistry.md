

# CreateRegistry
<a name="API_CreateRegistry"></a>

Creates a new registry in your AWS account. A registry serves as a centralized catalog for organizing and managing registry records, including MCP servers, A2A agents, agent skills, and custom resource types.

If you specify `CUSTOM_JWT` as the `authorizerType`, you must provide an `authorizerConfiguration`.

## Request Syntax
<a name="API_CreateRegistry_RequestSyntax"></a>

```
POST /registries HTTP/1.1
Content-type: application/json

{
   "approvalConfiguration": { 
      "autoApproval": {{boolean}}
   },
   "authorizerConfiguration": { ... },
   "authorizerType": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRegistry_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRegistry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-request-approvalConfiguration"></a>
The approval configuration for registry records. Controls whether records require explicit approval before becoming active. See the `ApprovalConfiguration` data type for supported configuration options.  
Type: [ApprovalConfiguration](API_ApprovalConfiguration.md) object  
Required: No

 ** [authorizerConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-request-authorizerConfiguration"></a>
The authorizer configuration for the registry. Required if `authorizerType` is `CUSTOM_JWT`. For details, see the `AuthorizerConfiguration` data type.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [authorizerType](#API_CreateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-request-authorizerType"></a>
The type of authorizer to use for the registry. This controls the authorization method for the Search and Invoke APIs used by consumers, and does not affect the standard CRUDL APIs for registry and registry record management used by administrators.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: No

 ** [clientToken](#API_CreateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-request-description"></a>
A description of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [name](#API_CreateRegistry_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-request-name"></a>
The name of the registry. The name must be unique within your account and can contain alphanumeric characters and underscores.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

## Response Syntax
<a name="API_CreateRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "registryArn": "string"
}
```

## Response Elements
<a name="API_CreateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [registryArn](#API_CreateRegistry_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateRegistry-response-registryArn"></a>
The Amazon Resource Name (ARN) of the created registry.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

## Errors
<a name="API_CreateRegistry_Errors"></a>

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
<a name="API_CreateRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateRegistry) 