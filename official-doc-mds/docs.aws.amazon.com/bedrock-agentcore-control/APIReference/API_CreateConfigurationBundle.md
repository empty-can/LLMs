

# CreateConfigurationBundle
<a name="API_CreateConfigurationBundle"></a>

Creates a new configuration bundle resource. A configuration bundle stores versioned component configurations for agent evaluation workflows.

## Request Syntax
<a name="API_CreateConfigurationBundle_RequestSyntax"></a>

```
POST /configuration-bundles/create HTTP/1.1
Content-type: application/json

{
   "branchName": "{{string}}",
   "bundleName": "{{string}}",
   "clientToken": "{{string}}",
   "commitMessage": "{{string}}",
   "components": { 
      "{{string}}" : { 
         "configuration": {{JSON value}}
      }
   },
   "createdBy": { 
      "arn": "{{string}}",
      "name": "{{string}}"
   },
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateConfigurationBundle_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfigurationBundle_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [branchName](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-branchName"></a>
The branch name for version tracking. Defaults to `mainline` if not specified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`   
Required: No

 ** [bundleName](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-bundleName"></a>
The name for the configuration bundle. Names must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}`   
Required: Yes

 ** [clientToken](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [commitMessage](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-commitMessage"></a>
A commit message describing the initial version of the configuration bundle.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

 ** [components](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-components"></a>
A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.  
Type: String to [ComponentConfiguration](API_ComponentConfiguration.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 2048.  
Key Pattern: `[a-zA-Z][a-zA-Z0-9_:/.\-]{0,2047}`   
Required: Yes

 ** [createdBy](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-createdBy"></a>
The source that created this version, including the source name and optional ARN.  
Type: [VersionCreatedBySource](API_VersionCreatedBySource.md) object  
Required: No

 ** [description](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-description"></a>
The description for the configuration bundle.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Pattern: `.+`   
Required: No

 ** [kmsKeyArn](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-kmsKeyArn"></a>
Optional KMS key ARN for encrypting component configurations.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [tags](#API_CreateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-request-tags"></a>
A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateConfigurationBundle_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "bundleArn": "string",
   "bundleId": "string",
   "createdAt": number,
   "versionId": "string"
}
```

## Response Elements
<a name="API_CreateConfigurationBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [bundleArn](#API_CreateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-response-bundleArn"></a>
The Amazon Resource Name (ARN) of the created configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [bundleId](#API_CreateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-response-bundleId"></a>
The unique identifier of the created configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_CreateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-response-createdAt"></a>
The timestamp when the configuration bundle was created.  
Type: Timestamp

 ** [versionId](#API_CreateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateConfigurationBundle-response-versionId"></a>
The initial version identifier of the configuration bundle.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

## Errors
<a name="API_CreateConfigurationBundle_Errors"></a>

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
<a name="API_CreateConfigurationBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle) 