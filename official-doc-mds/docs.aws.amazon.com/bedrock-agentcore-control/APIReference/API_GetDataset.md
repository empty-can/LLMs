

# GetDataset
<a name="API_GetDataset"></a>

 Retrieves dataset metadata. Use the `datasetVersion` query parameter to retrieve a specific version's metadata. If absent, defaults to DRAFT. For paginated example content, use `ListDatasetExamples`. 

## Request Syntax
<a name="API_GetDataset_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}?datasetVersion={{datasetVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_GetDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-request-uri-datasetId"></a>
 The unique identifier of the dataset to retrieve.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

 ** [datasetVersion](#API_GetDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-request-uri-datasetVersion"></a>
 Version to retrieve: "DRAFT" or a version number. Defaults to DRAFT if absent.   
Pattern: `(DRAFT|[0-9]+)` 

## Request Body
<a name="API_GetDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "datasetArn": "string",
   "datasetId": "string",
   "datasetName": "string",
   "datasetVersion": "string",
   "description": "string",
   "downloadUrl": "string",
   "downloadUrlExpiresAt": number,
   "draftStatus": "string",
   "exampleCount": number,
   "failureReason": "string",
   "kmsKeyArn": "string",
   "schemaType": "string",
   "status": "string",
   "tags": { 
      "string" : "string" 
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-createdAt"></a>
 The timestamp when the dataset was created.   
Type: Timestamp

 ** [datasetArn](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [datasetName](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-datasetName"></a>
 The name of the dataset.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [datasetVersion](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-datasetVersion"></a>
 The resolved version: "DRAFT" (default) or the requested version number.   
Type: String  
Pattern: `(DRAFT|[0-9]+)` 

 ** [description](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-description"></a>
 The description of the dataset.   
Type: String

 ** [downloadUrl](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-downloadUrl"></a>
 Presigned Amazon S3 URL to download the consolidated dataset file for the resolved version. Expires after 5 minutes. Omitted if the file does not yet exist.   
Type: String

 ** [downloadUrlExpiresAt](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-downloadUrlExpiresAt"></a>
 Expiry timestamp for the download URL.   
Type: Timestamp

 ** [draftStatus](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-draftStatus"></a>
 Publish synchronization state. Only authoritative when status is ACTIVE. MODIFIED indicates DRAFT has unpublished changes. UNMODIFIED indicates DRAFT matches the latest published version.   
Type: String  
Valid Values: `MODIFIED | UNMODIFIED` 

 ** [exampleCount](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-exampleCount"></a>
 The number of examples in the DRAFT.   
Type: Long

 ** [failureReason](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-failureReason"></a>
 Populated when status is CREATE\_FAILED, UPDATE\_FAILED, or DELETE\_FAILED. Describes the reason for the failure.   
Type: String

 ** [kmsKeyArn](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-kmsKeyArn"></a>
 AWS KMS key ARN used for server-side encryption on service Amazon S3 writes, if configured.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [schemaType](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-schemaType"></a>
 The schema type declared at create time. Immutable after creation.   
Type: String  
Valid Values: `AGENTCORE_EVALUATION_PREDEFINED_V1 | AGENTCORE_EVALUATION_SIMULATED_V1` 

 ** [status](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-status"></a>
 The current status of the dataset.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [tags](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-tags"></a>
 The tags associated with the dataset.   
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

 ** [updatedAt](#API_GetDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetDataset-response-updatedAt"></a>
 The timestamp when the dataset was last updated.   
Type: Timestamp

## Errors
<a name="API_GetDataset_Errors"></a>

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
<a name="API_GetDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetDataset) 