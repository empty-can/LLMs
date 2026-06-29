

# UpdateConfigurationBundle
<a name="API_UpdateConfigurationBundle"></a>

Updates a configuration bundle by creating a new version with the specified changes. Each update creates a new version in the version history.

## Request Syntax
<a name="API_UpdateConfigurationBundle_RequestSyntax"></a>

```
PUT /configuration-bundles/{{bundleId}} HTTP/1.1
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
   "parentVersionIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateConfigurationBundle_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bundleId](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-uri-bundleId"></a>
The unique identifier of the configuration bundle to update.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateConfigurationBundle_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [branchName](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-branchName"></a>
The branch name for this version. If not specified, inherits the parent's branch or defaults to `mainline`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`   
Required: No

 ** [bundleName](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-bundleName"></a>
The updated name for the configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}`   
Required: No

 ** [clientToken](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [commitMessage](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-commitMessage"></a>
A commit message describing the changes in this version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

 ** [components](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-components"></a>
The updated component configurations. Creates a new version of the bundle.  
Type: String to [ComponentConfiguration](API_ComponentConfiguration.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 2048.  
Key Pattern: `[a-zA-Z][a-zA-Z0-9_:/.\-]{0,2047}`   
Required: No

 ** [createdBy](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-createdBy"></a>
The source that created this version, including the source name and optional ARN.  
Type: [VersionCreatedBySource](API_VersionCreatedBySource.md) object  
Required: No

 ** [description](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-description"></a>
The updated description for the configuration bundle.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Pattern: `.+`   
Required: No

 ** [kmsKeyArn](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-kmsKeyArn"></a>
Optional KMS key ARN for encrypting component configurations. If provided, components will be encrypted with this key. If the bundle already has a KMS key, this rotates to the new key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [parentVersionIds](#API_UpdateConfigurationBundle_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-request-parentVersionIds"></a>
A list of parent version identifiers for lineage tracking. Regular commits have a single parent. Merge commits have two parents: the target branch parent and the source branch parent. If the branch already exists, the first parent must be the latest version on that branch.  
Type: Array of strings  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

## Response Syntax
<a name="API_UpdateConfigurationBundle_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bundleArn": "string",
   "bundleId": "string",
   "updatedAt": number,
   "versionId": "string"
}
```

## Response Elements
<a name="API_UpdateConfigurationBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bundleArn](#API_UpdateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-response-bundleArn"></a>
The Amazon Resource Name (ARN) of the updated configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [bundleId](#API_UpdateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-response-bundleId"></a>
The unique identifier of the updated configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [updatedAt](#API_UpdateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-response-updatedAt"></a>
The timestamp when the configuration bundle was updated.  
Type: Timestamp

 ** [versionId](#API_UpdateConfigurationBundle_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateConfigurationBundle-response-versionId"></a>
The new version identifier created by this update.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

## Errors
<a name="API_UpdateConfigurationBundle_Errors"></a>

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
<a name="API_UpdateConfigurationBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateConfigurationBundle) 