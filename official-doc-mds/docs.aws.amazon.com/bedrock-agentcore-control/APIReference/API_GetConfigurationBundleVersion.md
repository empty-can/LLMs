

# GetConfigurationBundleVersion
<a name="API_GetConfigurationBundleVersion"></a>

Gets a specific version of a configuration bundle by its version identifier.

## Request Syntax
<a name="API_GetConfigurationBundleVersion_RequestSyntax"></a>

```
GET /configuration-bundles/{{bundleId}}/versions/{{versionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfigurationBundleVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bundleId](#API_GetConfigurationBundleVersion_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-request-uri-bundleId"></a>
The unique identifier of the configuration bundle.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [versionId](#API_GetConfigurationBundleVersion_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-request-uri-versionId"></a>
The version identifier of the configuration bundle version to retrieve.  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## Request Body
<a name="API_GetConfigurationBundleVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfigurationBundleVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bundleArn": "string",
   "bundleId": "string",
   "bundleName": "string",
   "components": { 
      "string" : { 
         "configuration": JSON value
      }
   },
   "createdAt": number,
   "description": "string",
   "kmsKeyArn": "string",
   "lineageMetadata": { 
      "branchName": "string",
      "commitMessage": "string",
      "createdBy": { 
         "arn": "string",
         "name": "string"
      },
      "parentVersionIds": [ "string" ]
   },
   "versionCreatedAt": number,
   "versionId": "string"
}
```

## Response Elements
<a name="API_GetConfigurationBundleVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bundleArn](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [bundleId](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-bundleId"></a>
The unique identifier of the configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [bundleName](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-bundleName"></a>
The name of the configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}` 

 ** [components](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-components"></a>
A map of component identifiers to their configurations for this version.  
Type: String to [ComponentConfiguration](API_ComponentConfiguration.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 2048.  
Key Pattern: `[a-zA-Z][a-zA-Z0-9_:/.\-]{0,2047}` 

 ** [createdAt](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-createdAt"></a>
The timestamp when the configuration bundle was created.  
Type: Timestamp

 ** [description](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-description"></a>
The description of the configuration bundle.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Pattern: `.+` 

 ** [kmsKeyArn](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-kmsKeyArn"></a>
KMS key ARN used to encrypt component configurations, if CMK was provided.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [lineageMetadata](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-lineageMetadata"></a>
The version lineage metadata, including parent versions, branch name, and creation source.  
Type: [VersionLineageMetadata](API_VersionLineageMetadata.md) object

 ** [versionCreatedAt](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-versionCreatedAt"></a>
The timestamp when this specific version was created.  
Type: Timestamp

 ** [versionId](#API_GetConfigurationBundleVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConfigurationBundleVersion-response-versionId"></a>
The version identifier of this configuration bundle version.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

## Errors
<a name="API_GetConfigurationBundleVersion_Errors"></a>

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
<a name="API_GetConfigurationBundleVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetConfigurationBundleVersion) 